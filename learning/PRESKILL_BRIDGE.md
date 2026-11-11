# From Preskill's chapter to destructive monitoring

[Learning route](README.md) · [30 milestones](MILESTONES.md) · [Scientific account](../science/README.md)

The educational source is John Preskill, [*Quantum Shannon Theory*, arXiv:1604.07450v5](https://arxiv.org/abs/1604.07450v5), dated 8 July 2025. Its title page says “Updated June 2025”; the arXiv revision is the version pin. Links below point to that revision. This page supplies an original bridge to the monitoring problem; the author's chapter remains available at its source under its stated personal-use terms.

## Source map

Page numbers are the chapter's printed pages. PDF-viewer page numbers include six earlier pages.

| Relevant v5 passage | Background connection | Local work that remains |
|---|---|---|
| [§§10.2.1–10.2.4, pp. 15–20](https://arxiv.org/pdf/1604.07450v5#page=21) | Entropy, conditioning, and processing | Evaluate the reference state conditional on a noisy report in the [model](../science/model.md) |
| [§§10.6.1–10.6.2, pp. 40–42](https://arxiv.org/pdf/1604.07450v5#page=46), especially Eqs. (10.212)–(10.213) | Measurement records as classical registers | Keep the reported bit distinct from the hidden true bit; cancel the flag entropies correctly |
| [§10.6.6, pp. 50–51](https://arxiv.org/pdf/1604.07450v5#page=56) | Entanglement loss in a measurement branch | Analyze the direct sum with an intact branch, rather than treating the entire channel as a measurement |
| [§10.7.1, pp. 51–53](https://arxiv.org/pdf/1604.07450v5#page=57), Eqs. (10.273)–(10.278) | Optimized coherent information and regularization | Optimize over every input before comparing the [one-use threshold](../science/model.md) with capacity activation |
| [§10.5.3, p. 39](https://arxiv.org/pdf/1604.07450v5#page=45), and [§10.7.3, pp. 56–58](https://arxiv.org/pdf/1604.07450v5#page=62), especially Eq. (10.309) | Restrictions on sharing and environment simulation | Prove the exact finite-POVM [shareability criterion](../science/shareability.md), including its finite-block fidelity consequence |
| [§10.7.2, pp. 53–56](https://arxiv.org/pdf/1604.07450v5#page=59), and [§10.9.4, pp. 75–76](https://arxiv.org/pdf/1604.07450v5#page=81) | Decoupling and unassisted achievability | Select a positive finite [inner block](../science/coding.md) before taking the separate outer coding limit |

The [uniform Haar estimate](../science/haar_entropy.md) and [joint setting/noise law](../science/setting_frontier.md) require further channel-specific analysis. The chapter's general entropy and capacity tools do not evaluate these quantities.

## Notation crosswalk and a sign check

| Preskill v5 | This repository | Meaning |
|---|---|---|
| $`H(\rho)`$, $`H(A)`$ | $`S(\rho)`$, $`S(A)`$ | Von Neumann entropy in bits |
| $`H_2(t)`$ | $`h_2(t)`$ | Binary entropy |
| $`R`$ | $`R`$ | Purifying reference; it is not a receiver bypass |
| $`B`$, $`E`$ in a dilation | Receiver output, environment | The environment is not available to the decoder; $`E_{b,s}`$ elsewhere denotes a POVM effect |
| $`I_c(R\rangle B)`$ | $`I_c(\rho,\mathcal N)`$ | $`S(B)-S(RB)`$ for an input purification |
| $`Q_1(\mathcal N)`$, Eq. (10.273) | $`Q^{(1)}(\mathcal N)`$ | Coherent information maximized over one physical input |
| $`\bar R`$ | Communication rate | Logical qubits per physical channel use, not survival probability $`\delta`$ |

Preskill calls $`Q_1`$ the “one-shot quantum capacity.” Here it is called optimized one-use coherent information to distinguish it from an operational finite-use capacity with a specified error tolerance.

There is a sign slip in v5 Eq. (10.368), printed p. 76: its middle entropy difference is reversed. Eq. (10.275) and the exponent in Eq. (10.367) consistently give the achievable rate $`H(B)-H(E)-o(1)=I_c-o(1)`$. All formulas here use that sign.

## The first bridge: derive the cost of a noisy record

Take an input $`\rho_A`$ with a pure reference–input state $`|\psi\rangle_{RA}`$. The physical channel either sends $`A`$ intact with probability $`\delta`$, or measures it destructively with probability $`p=1-\delta`$. Its measured branch returns a reliable setting label and a noisy reported sign. There is one acquisition, after encoding; the measured qubit and true sign are inaccessible.

Absorb the known setting weights into the effects, writing $`\widetilde E_y=w_bE_{b,s}`$ for $`y=(b,s)`$. In an input eigenbasis, the unnormalized conditional reference block has the spectrum of

```math
A_y=\sqrt\rho\,\widetilde E_y^{\mathsf T}\sqrt\rho,
\qquad r_y=\operatorname{Tr}A_y,
\qquad \rho_R^y=A_y/r_y.
```

The transpose is fixed by the purification convention. Equivalently one may transpose the entire reference block; its spectrum is unchanged. Zero-probability terms contribute zero. Define

```math
C(\rho,q)=\sum_y r_yS(\rho_R^y).
```

Let $`Y`$ denote the complete measured record. The direct-sum entropy rule gives

```math
\begin{aligned}
S(B)&=h_2(\delta)+\delta S(\rho)+pH(Y),\\
S(RB)&=h_2(\delta)+p\bigl[H(Y)+C(\rho,q)\bigr].
\end{aligned}
```

The intact joint reference–input state is pure. Subtraction therefore gives the exact inherited formula

```math
I_c(\rho,\mathcal N)=\delta S(\rho)-pC(\rho,q).
```

The conditional quantum entropy $`C`$ is the quantity that enters this expression. Substituting the Shannon entropy of the reporting error, or conditioning on the unavailable true sign, would describe a different calculation.

For mixed inputs define

```math
\Gamma_{\mathsf E}(q)=\inf_{S(\rho)>0}\frac{C(\rho,q)}{S(\rho)},
\qquad x=\frac\delta{1-\delta}.
```

Every pure input has coherent information zero. Consequently $`Q^{(1)}=0`$ exactly when $`x\leq\Gamma_{\mathsf E}`$. A maximally mixed probe can supply a positive witness, but a negative value at that probe cannot establish the all-input zero statement.

## The second bridge: identify the channel-specific steps

| Step in the local argument | Mathematical task beyond the background |
|---|---|
| [Uniform isotropic entropy](../science/haar_entropy.md) | Control $`C/S`$ for every spectrum, including smaller input eigenvalues that vanish with $`q`$; establish the $`q\ln(1/q)`$ order without interchanging these limits |
| [Finite menu and matching upper bound](../science/setting_frontier.md) | Transfer an operator comparison through homogeneous entropy, construct a charged finite grid, and use excluded caps to bound every menu of at most $`J`$ settings |
| [Exact shareability](../science/shareability.md) | Use a pure intact Choi block to exclude two simultaneous quantum receivers; account for the input-independent classical noise and construct a matching joint channel |
| [Collective coding](../science/coding.md) | Compute every survivor mask and report, including the all-measured branch; compare the two exponential bases with explicit finite-menu prefactors |

For the converse, the established POVM noise content is $`\gamma=\sum_y\lambda_{\min}(\widetilde E_y)`$. The local calculation proves exact $`k`$-receiver compatibility when $`(k-1)\delta\leq p\gamma`$. At $`k=2`$ it yields antidegradability. The finite-dimensional fidelity ceiling then rules out reliable fixed-logical-size storage as well as positive-rate transmission in that region. For noisy projective qubit records, $`\gamma=2q`$ for every menu.

For achievability, first hold $`q`$, the menu, and the channel probabilities fixed. Select a finite repetition length $`N`$ with $`I_N>0`$. Then apply an outer code to $`m`$ independent copies of that $`N`$-use superchannel and take $`m\to\infty`$. The total number of physical uses is $`mN`$, and the resulting capacity lower bound is $`I_N/N`$. The inner block alone need not transmit with high fidelity, and its rate need not stay positive as $`N\to\infty`$.

Together, the finite-setting and coding arguments compare two thresholds for the same supplied channel. For a setting budget $`J`$, the largest possible one-use threshold has order $`q[1+\ln\min\{J,1/q\}]`$, while actual capacity activation has order $`q`$. The setting menu and its reliable label are resources; a changed menu is charged explicitly.

## Worked example: one axis, two survivor fractions

Fix one destructive measurement axis, $`Z`$, and reporting error $`q=0.1`$. The receiver learns the intact/measured flag and, on measured sites, one noisy sign. The encoding precedes the independent branch and outcome choices. No measured qubit can be reread.

The parameters are

```math
\eta=1-2q=0.8,\qquad c=4q(1-q)=0.36,\qquad\gamma=2q=0.2.
```

For a single axis the inherited exact one-use entropy ratio is $`\Gamma=c`$; a perpendicular code direction also has repetition loss $`L=c`$. Thus the optimized one-use activation fraction is

```math
\delta_1=\frac{c}{1+c}=\frac9{34}\approx0.264706.
```

The shareability obstruction and repetition achievability bound the actual activation fraction by

```math
\frac{\gamma}{1+\gamma}=\frac16
\ \leq\ \delta_c\ \leq\ \frac9{34}.
```

These bounds do not locate the exact $`\delta_c`$ in the intervening interval. In particular, an exact one-use threshold is not automatically an exact capacity threshold.

### At $`\delta=0.3`$: a positive witness and a rate interval

Here $`p=0.7`$ and $`x=3/7>0.36`$, so $`Q^{(1)}>0`$ and $`Q>0`$. To exhibit an actual witness, choose an input diagonal in the $`X`$ basis with eigenvalues $`1-t,t`$, where $`t=0.01`$. The two reported signs each have probability $`1/2`$. Each conditional reference state has smaller eigenvalue

```math
e(t)=\frac{1-\sqrt{1-4ct(1-t)}}2
\approx0.00357679345.
```

Therefore

```math
\begin{aligned}
S(\rho)&=h_2(0.01)\approx0.08079313590,\\
C(\rho,0.1)&=h_2(e(t))\approx0.03422000319,\\
I_c&=0.3\,h_2(0.01)-0.7\,h_2(e(t))
\approx0.000283938535>0.
\end{aligned}
```

This particular witness and the flagged-enhancement upper bound give

```math
0.000283938535\ldots
\ \leq\ Q^{(1)}(\mathcal N)
\ \leq\ Q(\mathcal N)
\ \leq\delta-p\gamma=0.16.
```

Rates strictly below the displayed witness are achievable in the asymptotic coding sense. Neither endpoint in this interval is claimed to be the exact capacity. The small lower bound supplies no efficient decoder or laboratory-runtime conclusion.

For comparison, the maximally mixed probe gives

```math
I_c(I/2,\mathcal N)=0.3-0.7h_2(0.1)
\approx-0.02829691551.
```

The negative value at this probe coexists with the positive biased-input witness. This explicitly shows why global input optimization matters.

### At $`\delta=0.1`$: an unconditional all-code obstruction

Now $`p=0.9`$ and $`x=1/9<\gamma=0.2`$. Equivalently $`\delta=0.1<p\gamma=0.18`$. The channel is antidegradable, hence $`Q=0`$ and $`Q^{(1)}=0`$. Every deterministic block code carrying one logical qubit obeys $`F_e\leq3/4`$, for every physical block length. This conclusion uses the shareability proof and does not depend on whether a chosen probe has negative coherent information.

The two survivor fractions describe two distinct channel points. They check the meanings of a threshold, a witness, a rate bound, and an all-code obstruction. The single-axis example does not itself exhibit the logarithmically growing threshold separation; that result requires the joint small-error and growing-menu analysis.

The [30 milestones](MILESTONES.md) develop these bridges and then follow the full proof. Exact source attributions for inherited results remain in the [related-work account](../references/RELATED_WORK.md).
