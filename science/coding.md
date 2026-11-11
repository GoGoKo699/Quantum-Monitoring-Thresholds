# Collective coding with an explicit finite inner block

This page proves the finite-menu repetition criterion used by the threshold theorem and gives an explicit sufficient block length and positive rate. The construction and the complete record calculation are inherited from [Measurement-Geometry-Superadditivity, P09–P10](https://github.com/GoGoKo699/Measurement-Geometry-Superadditivity/blob/99bdd710abbf7258be941ae83f46b7c9ea9702f8/science/repetition-coding.md#p09). The finite-length bookkeeping below makes its dependence on the number of settings and the strict threshold gap explicit. It is not an efficient-decoding theorem.

## Channel and statement

Let the physical input be a qubit. It survives with probability $`\delta`$; otherwise it is measured and discarded. Write $`p=1-\delta`$. A measured use chooses one of $`J`$ axes $`\mathbf n_j`$, with known probabilities $`w_j>0`$ summing to one, and reports its projective outcome through a binary symmetric channel of error $`0<q<1/2`$. The receiver learns the branch, the chosen axis, and the reported bit. Thus

```math
\mathcal N(\rho)=\delta\rho\ \oplus\ p\sum_{j,s}\operatorname{Tr}(E_{j,s}\rho)|j,s\rangle\langle j,s|,
\qquad
E_{j,s}=\frac{w_j}{2}\bigl[I+(-1)^s\eta\mathbf n_j\cdot\boldsymbol\sigma\bigr],
\quad \eta=1-2q.
```

Channel uses, branch choices, axis choices, and reporting errors are independent. The code is fixed before those choices are realized. The measured system and the true bit are inaccessible. No assistance or postselection is used. All entropies and coherent information are in bits; logarithms denoted $`\ln`$ are natural.

For a unit code direction $`\mathbf u`$, set

```math
\begin{aligned}
a&=\eta^2, &c&=1-a=4q(1-q), &z_j&=\mathbf n_j\cdot\mathbf u,\\
s_j&=\sqrt{1-a z_j^2}, &\kappa_j&=\frac{a(1-z_j^2)}{1-a z_j^2},\\
B&=\sum_j w_j s_j, &K&=\sum_j w_j s_j\kappa_j, &\Lambda(\mathbf u)&=B-K=\sum_j\frac{w_jc}{s_j}.
\end{aligned}
```

The quantities $`B,K,\Lambda`$ depend on the fixed direction. In particular, $`0\leq K<B\leq1`$. Let

```math
\nu_+=\delta+pK,\qquad \nu_-=pB.
```

**Finite-block theorem.** Suppose $`0<\delta<1`$ and

```math
g:=\delta-p\Lambda(\mathbf u)>0.
```

Define

```math
\begin{aligned}
\ell&=\sum_{j=1}^{J}\ln\frac{1+|\eta z_j|}{1-|\eta z_j|},
&x_*&=\frac1{1+e^\ell},
&c_R&=\frac2{\ln2}x_*(1-x_*),\\
\Delta&=\ln\frac{\nu_+}{\nu_-}>0,
&A&=\ln\frac2{c_R}.
\end{aligned}
```

The balanced repetition input of any length $`N`$ has coherent information $`I_N`$ satisfying

```math
I_N\geq\frac{c_R\nu_+^N}{(N+1)^J}-\nu_-^N.
\tag{1}
```

In particular the finite choice

```math
N=\left\lceil 1+\frac2\Delta\left[A+J\ln\left(1+\frac{2J}{\Delta}\right)\right]\right\rceil
\tag{2}
```

obeys

```math
I_N\geq\frac{c_R\nu_+^N}{2(N+1)^J}>0,
\qquad
Q(\mathcal N)\geq\frac{I_N}{N}\geq
\frac{c_R\nu_+^N}{2N(N+1)^J}>0.
\tag{3}
```

Consequently, with $`L=\min_{\|\mathbf u\|=1}\Lambda(\mathbf u)`$, the strict inequality $`\delta>pL`$ suffices for positive unassisted quantum capacity. This is a sufficient condition; equality and possible useful short blocks outside it are not resolved here. The endpoint $`\delta=1`$ is the identity channel and needs no repetition argument.

## Proof: retain every branch and record

Let $`|\mathbf u_+\rangle,|\mathbf u_-\rangle`$ be the eigenstates of $`\mathbf u\cdot\boldsymbol\sigma`$. The inner encoding is the isometry

```math
|0\rangle\longmapsto|\mathbf u_+\rangle^{\otimes N},\qquad
|1\rangle\longmapsto|\mathbf u_-\rangle^{\otimes N}.
```

Its balanced input is

```math
\rho_N=\tfrac12|\mathbf u_+\rangle\langle\mathbf u_+|^{\otimes N}
+\tfrac12|\mathbf u_-\rangle\langle\mathbf u_-|^{\otimes N}.
```

Although this average density operator is separable, a purification has a coherent logical reference. The isometry encodes an unknown qubit into two codewords; it does not clone it.

For a measured record $`y=(j,s)`$, the conditional probabilities under the two codewords are

```math
P_\pm(j,s)=\frac{w_j}{2}[1\pm(-1)^s\eta z_j].
```

For a record $`\omega=(y_1,\ldots,y_m)`$ on $`m`$ measured sites, write

```math
P_\pm(\omega)=\prod_{i=1}^mP_\pm(y_i),\quad
r_\omega=\frac{P_+(\omega)+P_-(\omega)}2,\quad
x_\omega=\frac{P_-(\omega)}{P_+(\omega)+P_-(\omega)},\quad
\chi_\omega=\prod_{i=1}^m\kappa_{j_i}.
```

When at least one physical qubit survives, the two surviving codeword states are orthogonal. The conditional joint reference–receiver density matrix, in its two-dimensional support, has diagonal entries $`1-x_\omega,x_\omega`$ and off-diagonal magnitude $`\sqrt{\chi_\omega x_\omega(1-x_\omega)}`$. This follows by multiplying the measured-site matrix elements of the effects: their squared off-diagonal-to-diagonal ratio is $`\kappa_j`$. Phases do not change the eigenvalues.

For $`0\leq\chi,x\leq1`$, define

```math
e_\chi(x)=\frac{1-\sqrt{1-4(1-\chi)x(1-x)}}2,\qquad
D_\chi(x)=h_2(x)-h_2(e_\chi(x)).
```

The conditional joint entropy is $`h_2(e_{\chi_\omega}(x_\omega))`$. Define the full measured-record sums

```math
A_m=\sum_\omega r_\omega h_2(x_\omega),\qquad
R_m=\sum_\omega r_\omega D_{\chi_\omega}(x_\omega),\qquad
C_m=A_m-R_m,
```

with $`A_0=R_0=1`$. For at least one survivor the coherent-information contribution is $`R_m`$. For the all-measured branch it is $`-C_N`$: there is no quantum system left at the receiver. The orthogonal flags and complete classical records cancel in the entropy difference. Summing every mask therefore gives the exact identity

```math
I_N=\sum_{m=0}^{N}\binom Nm\delta^{N-m}p^mR_m-p^N A_N.
\tag{4}
```

The $`m=N`$ term combines with the subtraction to give $`-p^NC_N`$. In particular, this unfavorable branch has not been omitted.

### Entropy and likelihood bounds

Two elementary inequalities suffice:

```math
h_2(x)\leq2\sqrt{x(1-x)},\qquad
D_\chi(x)\geq\frac2{\ln2}\chi x(1-x)\geq0.
\tag{5}
```

For the first, the function $`f(r)=h_2((1-\sqrt{1-r^2})/2)`$ is convex on $`[0,1]`$ with endpoints $`0,1`$, hence is at most its chord $`r`$. Convexity follows from $`\ln((1+z)/(1-z))\geq2z`$, with $`z=\sqrt{1-r^2}`$. For the second, dephasing the conditional qubit gives the relative-entropy difference $`D_\chi(x)`$; Pinsker's inequality in bits and the trace norm $`2\sqrt{\chi x(1-x)}`$ of its off-diagonal part give the displayed coefficient.

The first inequality and product structure yield

```math
A_m\leq\sum_\omega\sqrt{P_+(\omega)P_-(\omega)}
=\left(\sum_{j,s}\sqrt{P_+(j,s)P_-(j,s)}\right)^m=B^m.
\tag{6}
```

To lower-bound $`R_m`$, relabel the signs within each axis for the proof so that

```math
\pi_j^+=(1+|\eta z_j|)/2\geq\pi_j^-=(1-|\eta z_j|)/2\geq q.
```

First condition on the axis counts $`m_j`$, with $`\sum_jm_j=m`$. For each axis keep, in the lower-bound sum only, one central sign-count class: the two sign counts differ by at most one. There are at least $`2^{m_j}/(m_j+1)`$ sign strings in this class. The full record log-likelihood ratio then has absolute value at most $`\ell`$, so

```math
x_\omega(1-x_\omega)\geq x_*(1-x_*).
```

Also $`r_\omega\geq\sqrt{P_+(\omega)P_-(\omega)}`$. For each sign string that geometric mean contributes $`(s_j/2)^{m_j}`$, conditional on its axes, and $`\chi_\omega`$ contributes $`\kappa_j^{m_j}`$. Thus (5), the central-class multiplicity, and then the multinomial sum over axes imply

```math
\begin{aligned}
R_m&\geq c_R\sum_{m_1+\cdots+m_J=m}
\binom m{m_1,\ldots,m_J}\prod_j
\frac{(w_js_j\kappa_j)^{m_j}}{m_j+1}\\
&\geq\frac{c_R}{(m+1)^J}\left(\sum_j w_js_j\kappa_j\right)^m
=\frac{c_RK^m}{(m+1)^J}.
\end{aligned}
\tag{7}
```

Every omitted summand is nonnegative. This selection is only a proof of a lower bound, not a postselection step by the encoder or decoder. A setting with $`\kappa_j=0`$ contributes zero whenever it occurs, consistently with (7). At $`m=0`$ the bound holds because $`c_R\leq1`$; powers with exponent zero are taken as one, including when $`K=0`$.

Insert (6) and (7) into (4), and use $`(m+1)^J\leq(N+1)^J`$. The binomial theorem gives (1). Finally,

```math
\nu_+-\nu_-=\delta-p(B-K)=g>0.
```

To check (2), apply $`\ln y\leq\alpha y-\ln\alpha-1`$ at $`y=N+1`$, with $`\alpha=\Delta/(2J)`$. The choice (2) implies

```math
N\Delta\geq J\ln(N+1)+A.
```

Indeed $`\ln(1+2J/\Delta)\geq\ln(2J/\Delta)-1`$. Therefore $`\nu_-^N\leq c_R\nu_+^N/[2(N+1)^J]`$, establishing the first inequality in (3).

Fix this finite inner block. The coherent-information coding theorem, applied to independent uses of the superchannel $`\mathcal N^{\otimes N}`$, gives asymptotically achievable rates arbitrarily close to $`I_N/N`$ from below. This is the separate outer coding limit and proves the remaining assertions. A positive limit of $`I_N/N`$ as the inner length tends to infinity is neither claimed nor required. See [Devetak](https://arxiv.org/abs/quant-ph/0304127v6) and the [source comparison](../references/RELATED_WORK.md).

## Explicit dependence on setting count and noise

Since $`\ell\leq J\ln((1-q)/q)`$, a direction-independent lower bound is

```math
c_R\geq\underline c_R:=\frac1{2\ln2}\left(\frac q{1-q}\right)^J.
\tag{8}
```

One may replace $`c_R`$ by $`\underline c_R`$ everywhere in (1)–(3), and replace $`A`$ in (2) by

```math
\overline A=\ln(4\ln2)+J\ln\frac{1-q}{q}.
```

This makes the guarantee explicit without evaluating a potentially small posterior probability. Moreover

```math
\Delta=\ln(\nu_+/\nu_-)\geq\frac{\nu_+-\nu_-}{\nu_+}\geq g,
```

because $`\nu_+\leq1`$. Thus a strict margin $`g\geq\tau q`$, for fixed $`\tau>0`$, and a finite isotropic approximation with $`J=O(q^{-2})`$, give a sufficient inner block length

```math
N=O_\tau\!\left(q^{-3}\ln\frac1q\right).
\tag{9}
```

For such a family one can replace $`\Delta`$ by $`\tau q`$ in (2) to select a block from the known gap bound alone. The resulting guaranteed rate is still the explicit quantity in (3) with (8); it can be extremely small.

For the finite equal-weight sphere menus used in this project, $`K`$ is bounded below by a positive constant for sufficiently small $`q`$. Indeed, $`s_j\geq|\mathbf u\times\mathbf n_j|`$, the cube-face continuous distribution has density at least $`\pi/6`$ relative to uniform sphere area, and its mesh error is at most $`h=O(q)`$ in this dense-menu regime. Thus $`B\geq\pi^2/24-h`$, uniformly in $`\mathbf u`$. Also $`\Lambda(\mathbf u)\leq\sqrt c\leq2\sqrt q`$ for every menu, because $`s_j\geq\sqrt c`$. Consequently $`\nu_+\geq K=B-\Lambda\geq k_0>0`$ for sufficiently small $`q`$. The conservative rate guarantee from (3), (8), and (9) is therefore at least

```math
\exp\!\left[-O_\tau\!\left(q^{-3}\ln\frac1q\right)\right]
```

for sufficiently small $`q`$. This lower bound demonstrates positivity, not a useful practical rate or an optimal rate scaling. The threshold statement $`\delta_Q=\Theta(q)`$ concerns the location of the positive-capacity boundary; it does not assert $`Q=\Theta(q)`$.

The physical costs include the finite menu, its reliable setting label of $`\lceil\log_2J\rceil`$ bits per measured site, the reported bit, branch flags, and the $`N`$ physical inputs per inner logical qubit. The proof supplies no efficient outer encoder, decoder, or finite outer-block error bound.
