# Related work and source boundaries

The result concerns unassisted communication through a specified memoryless channel: a qubit is either transmitted intact or destructively measured, and the receiver receives only a noisy classical measurement record in the measured branch. Reliable branch and setting labels are part of the model. The measured qubit, true outcome, and detector-noise bit are unavailable. These access assumptions distinguish the result from models in which measured systems can be interrogated again.

The main contribution is the joint setting-count and detector-error law for the globally optimized one-use coherent-information threshold,

```math
\Gamma_J^*(q)=\Theta\!\left(q\left[1+\ln\min\{J,1/q\}\right]\right),
```

compared with the uniformly linear $`\Theta(q)`$ scale at which collective unassisted quantum capacity becomes positive. Here the supremum in $`\Gamma_J^*`$ is over all known menus with at most $`J`$ settings, and the one-use benchmark is optimized over every input state. A growing finite menu can therefore produce an unbounded logarithmic separation of activation thresholds. This is a statement about threshold location, not a lower bound of order $`q`$ on the communication rate. See the [setting frontier](../science/setting_frontier.md), [uniform isotropic entropy bound](../science/haar_entropy.md), and [finite-block coding proof](../science/coding.md).

## Exact inherited channel and coding construction

The closest source is the public repository [Measurement-Geometry-Superadditivity](https://github.com/GoGoKo699/Measurement-Geometry-Superadditivity), inspected at commit [`99bdd710abbf7258be941ae83f46b7c9ea9702f8`](https://github.com/GoGoKo699/Measurement-Geometry-Superadditivity/tree/99bdd710abbf7258be941ae83f46b7c9ea9702f8). Its [complete proof](https://github.com/GoGoKo699/Measurement-Geometry-Superadditivity/blob/99bdd710abbf7258be941ae83f46b7c9ea9702f8/docs/COMPLETE_PROOF.md) already contains the same noisy classical-record channel. Its contributions used here are:

| Source passage | Supplied result | Use in this repository |
|---|---|---|
| P01 | Exact conditional-reference entropy expression and global single-use criterion $`I_c=\delta S(\rho)-pC(\rho)`$, with positive one-use coherent information exactly when $`\delta/p>\Gamma`$ | Defines the benchmark being compared |
| P09 | Balanced repetition isometry, conditional states for every record, and an exact coherent-information sum including the all-measured branch | Supplies the collective mechanism |
| P09.4–P10 | Polynomial record-overlap bounds for each fixed finite menu; a positive finite repetition block when $`\delta/p>L`$; an outer coding limit | Supplies achievability, reproduced self-contained with explicit sufficient block length and rate in [coding.md](../science/coding.md) |
| P11.1 | For coplanar menus, including a single axis, $`\Gamma=L=4q(1-q)`$ | Shows that a fixed-axis linear activation scale is already inherited |

That source also proves a finite-menu geometric separation at each fixed interior error. Its existence of a collective advantage, and the repetition construction itself, are not new claims here. The addition is a matching law in the joint limit of changing error and setting budget, with an upper bound for every menu and a finite equal-weight construction attaining the order. The lower bound is uniform over input purity, including inputs whose smaller eigenvalue tends to zero together with $`q`$. Averaging the inherited repetition loss over code directions yields an $`O(q)`$ sufficient activation scale for every finite menu. The exact antidegradability criterion supplies the corresponding all-code obstruction.

## Generalized erasure channels and superadditivity

[Siddhu and Griffiths, *Positivity and nonadditivity of quantum capacities using generalized erasure channels*](https://arxiv.org/abs/2003.00583v2), IEEE Transactions on Information Theory **67**, 4533–4545 (2021), develop the channel-gluing framework that contains a flagged identity branch combined with another channel. In particular, their Eq. (35) treats a complementary generalized-erasure construction. This framework is directly relevant; an identity-plus-measurement form alone is not a new channel idea. Their worked dephasing-complement example sends nonorthogonal pure quantum states in its auxiliary branch, whereas the present measured branch sends mixed classical records. Replacing one by the other changes rank and the entropy near pure inputs, so their positive one-use conclusion for arbitrarily small identity weight does not transfer to full-rank noisy records.

[Leditzky, Leung, and Smith, *Dephrasure channel and superadditivity of coherent information*](https://arxiv.org/abs/1806.08327v3), Physical Review Letters **121**, 160501 (2018), establish superadditivity and analyze repetition codes for a channel combining dephasing with erasure. This is important coding precedent. The channel output and measured-record entropy cost differ from those studied here. Moreover, an improvement in a repetition-code rate or a failure of single-letter capacity does not itself give the joint finite-setting activation law. [Bhalerao and Leditzky](https://arxiv.org/abs/2508.09978v1) study permutation-invariant code improvements for several channels; this is further context for the distinction between improving achievable rates and shifting a positivity boundary.

The final step from one positive finite block to a positive asymptotic rate is the standard coherent-information coding theorem. We use [Devetak, *The private classical capacity and quantum capacity of a quantum channel*](https://arxiv.org/abs/quant-ph/0304127v6), IEEE Transactions on Information Theory **51**, 44–55 (2005). The inner repetition length is held finite before taking the independent outer coding limit. No efficient outer decoder or finite outer-block error estimate is supplied.

## Ideal monitoring, imperfect records, and the all-code obstruction

[Lee and Yoshida, *Randomly Monitored Quantum Codes*](https://journals.aps.org/prxquantum/abstract/10.1103/6s65-ylvw), PRX Quantum **7**, 020352 (2026), analyze how measurements destroy encoded information and obtain maximal measurement thresholds for broad code families with ideal records. Their result motivates asking what finite record errors do. Our obstruction requires the destructive-access model stated above and applies to unconditional quantum transmission, including fixed-dimensional logical storage. It is not a claim that every monitored-circuit transition disappears under arbitrarily small readout noise.

For a general finite POVM $`\{E_y\}`$, the scalar

```math
\gamma(E)=\sum_y\lambda_{\min}(E_y)
```

is an existing measurement quantity. It is the greatest weight of a trivial measurement that can be separated from the POVM, equivalently one minus its weight of informativeness. See [Ducuara and Skrzypczyk, *Weight of informativeness, state exclusion games and excludible information*](https://arxiv.org/abs/1908.10347v1). The same smallest-eigenvalue structure occurs in measurement reversal: [Oi, *Unlearning quantum information*](https://strathprints.strath.ac.uk/49382/), European Physical Journal D **68**, 259 (2014), bounds the total probability of reversing a measurement through its minimum singular values. The quantity $`\gamma`$ is not introduced here as a new resource monotone.

The same scalar is the established POVM noise content and the measurement-channel quantum Doeblin coefficient: [George, Hirche, Nuradha, and Wilde, *Quantum Doeblin Coefficients: Interpretations and Applications*](https://arxiv.org/abs/2503.22823v3), Quantum **10**, 2115 (2026), Proposition 35. The general notions of channel self-compatibility and the equivalence between two-self-compatibility and antidegradability are reviewed by [Heinosaari and Miyadera, *Incompatibility of quantum channels*](https://arxiv.org/abs/1608.01794v2), Journal of Physics A **50**, 135302 (2017), Section 4.3.

The [shareability proof](../science/shareability.md) establishes the exact criterion for the present flagged identity-plus-record channel: for every integer $`k\geq2`$, a joint channel to $`k`$ receivers with the original channel at every marginal exists if and only if $`(k-1)\delta\leq p\gamma(E)`$. Antidegradability is the case $`k=2`$. For noisy qubit projective records, $`\gamma(E)=2q`$, independently of the menu. Necessity follows from the structure of a symmetric extension of the Choi state, and sufficiency constructs such an extension. The resulting obstruction is uniform in code length. The standard singlet-fraction bound for extendible states also gives a fidelity ceiling for any fixed logical dimension, a stronger storage statement than merely writing $`Q=0`$. Compatibility and extension bounds for isotropic states are treated by [Johnson and Viola, *Compatible quantum correlations: Extension problems for Werner and isotropic states*](https://doi.org/10.1103/PhysRevA.88.032323), Physical Review A **88**, 032323 (2013).

## Conditional entropy, covariance, and information combining

The measured-branch cost is a conditional entropy, closely related to entropy reduction of an inefficient quantum measurement. [Jacobs, *A bound on the mutual information, and properties of entropy reduction, for quantum channels with inefficient measurements*](https://arxiv.org/abs/quant-ph/0412006), Journal of Mathematical Physics **47**, 012102 (2006), proves concavity and, for unitarily covariant measurements, Schur concavity of entropy reduction. Applied to an isotropic noisy measurement, this gives an additive bound of the form

```math
C(\rho,q)\geq S(\rho)-1+h_2(q).
```

It does not give the uniform multiplicative lower bound $`C(\rho,q)/S(\rho)\gtrsim q\ln(1/q)`$: the additive bound becomes vacuous for sufficiently pure inputs. [Shirokov, *Entropy reduction of quantum measurements*](https://arxiv.org/abs/1011.3127v3), Journal of Mathematical Physics **52**, 052202 (2011), develops the general entropy-reduction framework. Our use of homogeneous conditional entropy and its positive-semidefinite monotonicity belongs to this standard framework; the evaluated isotropic bound and its finite-menu transfer are the specific estimates required here.

[Hirche and Reeb, *Bounds on Information Combining With Quantum Side Information*](https://arxiv.org/abs/1706.09752v2), IEEE Transactions on Information Theory **64**, 4739–4757 (2018), give quantum information-combining inequalities for binary classical–quantum variables. Their XOR setting with independent uniform classical inputs is different from the arbitrary input spectrum and angular averaging in the present entropy ratio. We do not claim a general quantum Mrs. Gerber lemma. General conditional contraction theory is also developed by [Hirche, George, Nuradha, and Wilde](https://arxiv.org/abs/2608.27171v1); an evaluation of the particular singular setting/error frontier remains necessary to obtain the theorem here.

## Background texts

The following are three independently useful routes into the prerequisites. Links identify exact published editions or an exact arXiv revision; source manuscripts are linked rather than redistributed.

| Text and version | Relevant background |
|---|---|
| [John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018](https://cs.uwaterloo.ca/~watrous/TQI/) | Channels and instruments; state and channel distance; entropy; entanglement; quantum channel capacity, especially Chapters 2, 3, 5, 6, and 8 |
| [John Preskill, *Quantum Shannon Theory*, arXiv:1604.07450v5, 8 July 2025](https://arxiv.org/abs/1604.07450v5) | Entropy, entanglement, measurements, coherent information, decoupling, and coding; the version pin avoids silently using an older chapter |
| [Mark M. Wilde, *Quantum Information Theory*, second edition, Cambridge University Press, 2017](https://doi.org/10.1017/9781316809976) | Conditional entropy and coherent information, data processing, channel coding, and degradability; this citation is to the published second edition, not a later evolving author draft |

Machine-readable metadata, source versions, and the role of each reference are recorded in [bibliography.json](bibliography.json). The comparisons above delimit the scientific claims; they do not assert an exhaustive literature classification.
