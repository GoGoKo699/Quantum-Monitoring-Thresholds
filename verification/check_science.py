"""Finite checks of the monitoring proofs; no numerical proof of capacity."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.special import xlogy

LN2 = math.log(2)


def h2(x):
    x = np.clip(x, 0.0, 1.0)
    return -(xlogy(x, x) + xlogy(1-x, 1-x))/LN2


def entropy(a):
    ev = np.linalg.eigvalsh((a+a.conj().T)/2).clip(0)
    return float(-np.sum(xlogy(ev, ev))/LN2)


def haar_cost(q, r):
    if r == 0:
        return float(h2(q))
    eta = 1-2*q
    u = 4*q*(1-q)*(1-r*r)

    def integrand(z):
        a = u/z**2
        # Stable small eigenvalue, avoiding 1-sqrt(1-a) cancellation.
        lam = a/(2*(1+math.sqrt(max(0.0, 1-a))))
        return z*float(h2(lam))

    lo, hi = 1-eta*r, 1+eta*r
    points = np.geomspace(lo, hi, 48)
    val = sum(quad(integrand, float(a), float(b), epsabs=1e-15,
                   epsrel=2e-9)[0] for a, b in zip(points[:-1], points[1:]))
    return val/(2*eta*r)


def trace_to_recipient(omega, d, out, k, j):
    dims = [d] + [out]*k
    a = omega.reshape(dims+dims)
    for idx in range(k, 0, -1):
        if idx != j+1:
            half = a.ndim//2
            a = np.trace(a, axis1=idx, axis2=idx+half)
    return a.reshape(d*out, d*out)


def broadcast_check(d, outcomes, k, seed):
    rng = np.random.default_rng(seed)
    raw = []
    for _ in range(outcomes):
        z = rng.normal(size=(d, d))+1j*rng.normal(size=(d, d))
        raw.append(z.conj().T@z+0.2*np.eye(d))
    ev, u = np.linalg.eigh(sum(raw))
    inv = (u/np.sqrt(ev))@u.conj().T
    effects = [inv@a@inv for a in raw]
    minima = np.array([np.linalg.eigvalsh(e)[0] for e in effects])
    gamma = float(minima.sum())
    delta = gamma/(gamma+k-1)
    p = 1-delta
    tau = minima/gamma
    out = d+outcomes
    omega = np.zeros((d*out**k, d*out**k), complex)

    def ix(a, recipients):
        return np.ravel_multi_index((a, *recipients), (d, *([out]*k)))

    for i in range(k):
        for y in range(outcomes):
            for a in range(d):
                row = [d+y]*k
                row[i] = a
                for b in range(d):
                    col = [d+y]*k
                    col[i] = b
                    omega[ix(a, row), ix(b, col)] += delta*tau[y]/d
    for y, e in enumerate(effects):
        residual = p*e-(k-1)*delta*tau[y]*np.eye(d)
        for a in range(d):
            for b in range(d):
                omega[ix(a, [d+y]*k), ix(b, [d+y]*k)] += residual.T[a, b]/d

    phi = np.zeros(d*out, complex)
    for a in range(d):
        phi[a*out+a] = 1/math.sqrt(d)
    target = delta*np.outer(phi, phi.conj())
    for y, e in enumerate(effects):
        inds = [a*out+d+y for a in range(d)]
        target[np.ix_(inds, inds)] += p*e.T/d
    return {
        'dimension': d, 'outcomes': outcomes, 'receivers': k,
        'gamma': gamma, 'boundary_delta': delta,
        'trace_error': float(abs(np.trace(omega)-1)),
        'minimum_eigenvalue': float(np.linalg.eigvalsh(omega)[0]),
        'marginal_errors': [float(np.linalg.norm(
            trace_to_recipient(omega, d, out, k, j)-target)) for j in range(k)]}


def run_checks():
    assertions = 0
    worst_entropy_slack = 1.0
    for e in np.r_[np.geomspace(1e-24, 0.25, 180), np.linspace(.25, .5, 60)]:
        det = e*(1-e)
        slack = float(h2(e) - det*math.log(1/det)/(2*LN2))
        assert slack >= -1e-14
        worst_entropy_slack = min(worst_entropy_slack, slack)
        assertions += 1

    # Independent direct conditional-reference matrix vs analytic determinant.
    rng = np.random.default_rng(3947)
    pauli = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]])
    worst_det = 0.0
    worst_effect = 0.0
    for _ in range(200):
        t = 10**rng.uniform(-10, math.log10(.5))
        q = 10**rng.uniform(-8, math.log10(1/64))
        n = rng.normal(size=3); n /= np.linalg.norm(n)
        sr = np.diag(np.sqrt([1-t, t]))
        for sign in [-1, 1]:
            effect = (np.eye(2)+sign*(1-2*q)*np.einsum('i,ijk->jk', n, pauli))/2
            a = sr@effect@sr
            prob = float(np.trace(a).real)
            actual = float(np.linalg.det(a/prob).real)
            expected = t*(1-t)*q*(1-q)/prob**2
            worst_det = max(worst_det, abs(actual-expected))
            assert abs(actual-expected) < 2e-13
            assertions += 1
        # Critical coarse-mesh/larger-noise comparison, at varied h/q ratios.
        h = 10**rng.uniform(-9, -2)
        q2 = q+h
        m = n+rng.normal(size=3)*h/3
        m /= np.linalg.norm(m)
        dist = np.linalg.norm(m-n)
        alpha = q/(q2+h/2)
        if dist <= h:
            e1 = (np.eye(2)+(1-2*q)*np.einsum('i,ijk->jk', m, pauli))/2
            e2 = (np.eye(2)+(1-2*q2)*np.einsum('i,ijk->jk', n, pauli))/2
            minev = float(np.linalg.eigvalsh(e1-alpha*e2)[0])
            worst_effect = min(worst_effect, minev)
            assert minev > -1e-13
            assertions += 1

    broadcasts = [broadcast_check(2, 3, 2, 1), broadcast_check(2, 3, 3, 2),
                  broadcast_check(3, 3, 2, 3)]
    for b in broadcasts:
        assert b['trace_error'] < 1e-12
        assert b['minimum_eigenvalue'] > -1e-12
        assert max(b['marginal_errors']) < 1e-12
        assertions += 3

    haar = []
    for q in [1/64, 1e-2, 1e-3, 1e-4, 1e-5]:
        radii = np.unique(np.r_[np.linspace(0, .99, 28), 1-np.geomspace(1e-10, .01, 18)])
        values = [haar_cost(q, float(r))/float(h2((1-r)/2)) for r in radii]
        lower = q*math.log(1/q)/64
        assert min(values) >= lower-1e-12
        assertions += 1
        eta = 1-2*q
        loss = 4*q*(1-q)*math.asin(eta)/eta
        haar.append({'q': q, 'sampled_input_count': len(radii),
                     'minimum_sampled_ratio': min(values),
                     'proved_Haar_lower_bound': lower,
                     'maximally_mixed_ratio': float(h2(q)),
                     'Haar_repetition_loss': loss})

    # Verify the stated sufficient block bound in log form, without underflow.
    worst_block_slack = math.inf
    for settings in [1, 3, 6, 100, 1000]:
        for log_gap in [1e-5, .001, .1, 1, 5]:
            for cost in [1, 10, 1000]:
                n = math.ceil(1+2/log_gap*(cost+settings*math.log1p(2*settings/log_gap)))
                slack = log_gap*n-cost-settings*math.log(n+1)
                assert slack >= -1e-9
                worst_block_slack = min(worst_block_slack, slack)
                assertions += 1
    return {'status': 'pass', 'assertion_count': assertions,
            'scope': 'Finite checks, not universal proof, capacity computation, or novelty certification.',
            'conditional_determinant_max_error': worst_det,
            'effect_comparison_min_eigenvalue': worst_effect,
            'entropy_inequality_min_slack': worst_entropy_slack,
            'block_bound_min_log_slack': worst_block_slack,
            'broadcast_checks': broadcasts, 'haar_grid_checks': haar}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = run_checks()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
