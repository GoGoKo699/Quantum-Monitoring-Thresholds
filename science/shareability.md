# Shareability and universal coding bounds

The intact quantum branch limits how many receivers can share the channel. The relevant property of the classical record is its **noise content**: the largest input-independent component of its POVM. This gives an exact shareability criterion, finite-block fidelity bounds, and a capacity upper bound.

## Channel and noise content

Let $`d\geq2`$ and let $`(E_y)_{y\in Y}`$ be a finite POVM on $`\mathbb C^d`$. Write

```math
\mathcal M(\rho)=\sum_y\operatorname{Tr}(E_y\rho)|y\rangle\langle y|,
\qquad
\mathcal N_\delta(\rho)=\delta\rho\ \oplus\ p\mathcal M(\rho),
\qquad p=1-\delta.
```

The two output summands have orthogonal, reliably accessible flags. The first is a $`d`$-dimensional quantum register; the second contains only a classical record. Define

```math
\gamma(\mathcal M):=\sum_y\lambda_{\min}(E_y)\in[0,1].
```

This scalar is the established POVM noise content and, for measurement channels, the quantum Doeblin coefficient; see [George et al., Proposition 35](https://arxiv.org/html/2503.22823v3). Indeed, $`\gamma(\mathcal M)`$ is the largest $`s`$ for which

```math
\mathcal M=s\mathcal R_\tau+(1-s)\mathcal F,
\qquad
\mathcal R_\tau(\rho)=\operatorname{Tr}(\rho)\sum_y\tau_y|y\rangle\langle y|,
```

with $`\tau`$ a probability distribution and $`\mathcal F`$ a measurement channel. Positivity requires $`s\tau_y I\leq E_y`$, hence $`s\leq\sum_y\lambda_{\min}(E_y)`$. Equality is attained, when $`\gamma>0`$, by $`\tau_y=\lambda_{\min}(E_y)/\gamma`$.

For the noisy qubit axis ensemble,

```math
E_{b,s}=w_b\frac{I+(-1)^s(1-2q)\mathbf n_b\cdot\boldsymbol\sigma}{2},
\qquad 0\leq q\leq\frac12,
```

one has $`\gamma(\mathcal M)=2q`$, for every choice of axes and positive weights. The threshold below therefore does not depend on their geometry.

## Exact shareability theorem

A channel is **$`k`$-self-compatible** if a channel to $`k`$ receivers exists whose marginal at every receiver is the original channel. Averaging over receiver permutations makes this extension symmetric. Self-compatibility at $`k=2`$ is equivalent to antidegradability; these standard notions and their relation are reviewed by [Heinosaari and Miyadera, Section 4.3](https://arxiv.org/pdf/1608.01794).

**Theorem.** For every integer $`k\geq2`$,

```math
\boxed{\quad
\mathcal N_\delta\text{ is }k\text{-self-compatible}
\quad\Longleftrightarrow\quad
(k-1)\delta\leq p\,\gamma(\mathcal M).
\quad}
```

### Necessity

Use the normalized Choi convention

```math
J_{AB}=(\operatorname{id}_A\otimes\mathcal N_\delta)(\Phi_d),
\qquad
\Phi_d=|\Phi_d\rangle\langle\Phi_d|,
\qquad
|\Phi_d\rangle=d^{-1/2}\sum_{i=1}^d|i,i\rangle.
```

Its flagged blocks are

```math
J_{A Q}=\delta\Phi_d,
\qquad
J_{A C}=\frac p d\sum_y E_y^{\mathsf T}\otimes|y\rangle\langle y|.
```

Suppose a joint channel exists, and let $`\Omega_{A B_1\cdots B_k}`$ be its normalized Choi state. At each receiver pinch only between the quantum and classical flags, and dephase the classical labels. This leaves every desired marginal unchanged: the channel has no coherence between these output sectors. It does **not** dephase the quantum register inside its intact branch. Thus the joint state may be assumed block diagonal in its flag pattern and classical labels. Also average it over receiver permutations.

Conditioning on receiver $`i`$ having a quantum output gives a positive operator with marginal $`\delta\Phi_{A Q_i}`$. A rank-one marginal forces factorization:

```math
\Omega_{Q_i}=\delta\Phi_{A Q_i}\otimes\sigma_{\widehat i},
```

where $`\sigma_{\widehat i}`$ is normalized. This follows because every vector orthogonal to $`|\Phi_d\rangle`$ has zero expectation in the marginal, so positivity removes the entire corresponding support of the joint operator.

There can be no sector in which two distinct receivers $`i,j`$ both have quantum outputs. To see this, project the preceding factorization onto receiver $`j`$'s quantum flag. After tracing out $`Q_i`$, its $`A Q_j`$ marginal has the product form

```math
\delta\frac{I_A}{d}\otimes\sigma_{Q_j}.
```

It is a positive contribution to the required rank-one marginal $`\delta\Phi_{A Q_j}`$. If $`\sigma_{Q_j}\ne0`$, this product has rank at least $`d\geq2`$ and cannot be supported in that one-dimensional maximally entangled subspace. Therefore $`\sigma_{Q_j}=0`$. All sectors with two or more quantum receivers vanish.

Consequently, whenever receiver $`i`$ gets the intact input, every other receiver gets an input-independent classical output. Symmetry supplies one probability distribution $`\tau_y`$ for the marginal classical label of any other receiver. For a fixed receiver $`j`$, its classical marginal receives contributions from the $`k-1`$ mutually exclusive events in which another receiver gets the quantum input. Their sum is

```math
\frac{(k-1)\delta}{d}\,I_A\otimes\sum_y\tau_y|y\rangle\langle y|.
```

Subtracting these contributions from $`J_{A C_j}`$ leaves a positive operator. Each label block therefore obeys

```math
pE_y^{\mathsf T}-(k-1)\delta\tau_y I\succeq0.
```

Taking minimum eigenvalues and summing over $`y`$ proves

```math
(k-1)\delta\leq p\sum_y\lambda_{\min}(E_y).
```

### Sufficiency

If $`\delta=0`$, measure $`\mathcal M`$ once and copy its classical outcome to all receivers. Otherwise the stated inequality requires $`\gamma>0`$. Set

```math
\tau_y=\frac{\lambda_{\min}(E_y)}{\gamma},
\qquad
F_y=pE_y-(k-1)\delta\tau_y I\succeq0.
```

The following instrument defines a symmetric joint channel:

- For each receiver $`i`$, an alternative of subnormalized probability $`\delta`$ sends the unknown input intact to $`i`$. Draw $`y\sim\tau`$ independently of the input and give that same classical label to every other receiver.
- In the remaining alternative, apply the positive effects $`F_y`$ and give label $`y`$ to every receiver.

The residual effects sum to

```math
\sum_y F_y=\bigl[p-(k-1)\delta\bigr]I=(1-k\delta)I.
```

This is positive because $`\gamma\leq1`$ and the theorem's inequality implies $`k\delta\leq1`$. The total instrument is trace preserving. At any receiver, the quantum marginal is $`\delta\operatorname{id}`$, and its classical effect for label $`y`$ is

```math
(k-1)\delta\tau_y I+F_y=pE_y.
```

The desired marginal is therefore exactly $`\mathcal N_\delta`$.

### Endpoints

For $`\delta>0`$, the largest shareability order is

```math
k_{\max}=\left\lfloor1+\frac{p\gamma}{\delta}\right\rfloor,
```

where $`k_{\max}=1`$ means that no nontrivial extension exists. At $`\delta=0`$ every finite order is possible. If $`\gamma=0`$ and $`\delta>0`$, no order $`k\geq2`$ is possible. If the record is completely input independent, $`\gamma=1`$, the criterion reduces to $`k\delta\leq1`$, the flagged erasure-channel result.

For symmetric noisy qubit records the exact antidegradability boundary is

```math
\boxed{\quad
\delta\leq2q(1-\delta)
\quad\Longleftrightarrow\quad
\delta\leq\frac{2q}{1+2q}.
\quad}
```

At perfect acquisition $`q=0`$, the channel is not antidegradable for any $`\delta>0`$. This statement alone does not establish positive capacity for an arbitrary POVM; the exact perfect-record capacity for rank-one measurement effects follows below.

## Finite-block fidelity consequences

The extension property is preserved by tensor products and arbitrary channel pre- and postprocessing. In particular, if $`\mathcal E`$ encodes a logical system of dimension $`D`$ into $`n`$ physical inputs and $`\mathcal D`$ is a deterministic decoder, then

```math
\mathcal L=\mathcal D\circ\mathcal N_\delta^{\otimes n}\circ\mathcal E
```

is $`k`$-self-compatible whenever $`\mathcal N_\delta`$ is. Apply the physical extension independently at each input, group all outputs belonging to the same recipient, and apply the same decoder separately at every recipient.

The standard maximally entangled overlap bound for a $`k`$-extendible state is

```math
\boxed{\qquad
F_e(\mathcal L):=\operatorname{Tr}\!\left[\Phi_D
(\operatorname{id}\otimes\mathcal L)(\Phi_D)\right]
\leq\frac{D+k-1}{Dk}.
\qquad}
```

For completeness, let $`P_i=\Phi_{R B_i}\otimes I_{\widehat i}`$ on a joint logical-output extension. Write $`P_i=V_iV_i^\dagger`$, where $`V_i`$ inserts $`|\Phi_D\rangle`$ on $`R B_i`$. The maximally entangled contraction gives $`\|V_i^\dagger V_j\|_\infty=1/D`$ for $`i\ne j`$. The block Gram operator consequently satisfies

```math
\left\|\sum_iP_i\right\|_\infty
\leq1+\frac{k-1}{D}.
```

Symmetry gives $`kF_e=\operatorname{Tr}[(\sum_iP_i)\Omega]`$, proving the displayed bound. This is the usual cloning/shareability inequality, rather than a separate coding theorem; see [Johnson and Viola](https://arxiv.org/abs/1305.1342) and the use of extendibility in processor bounds by [Kaur et al.](https://doi.org/10.1103/PhysRevLett.123.070502).

In particular, throughout the antidegradable wedge, **every blocklength and every deterministic code transmitting one logical qubit obeys $`F_e\leq3/4`$**. More generally, using $`k_{\max}`$ shows that at fixed logical dimension $`D`$, the upper bound tends to $`1/D`$ when $`\delta/(p\gamma)\to0`$, independently of $`n`$. Saturation of this general shareability bound by a code for the present channel is not asserted.

## Universal capacity upper bound

The noise-content decomposition also gives a quantitative bound outside the antidegradable region:

```math
\boxed{\qquad
Q(\mathcal N_\delta)
\leq\bigl[\delta-p\gamma(\mathcal M)\bigr]_+\log_2 d,
\qquad [x]_+=\max\{x,0\}.
\qquad}
```

### A flagged enhancement

Put $`\gamma=\gamma(\mathcal M)`$. When $`0<\gamma<1`$, write

```math
E_y=\gamma\tau_y I+(1-\gamma)F_y,
\qquad
\tau_y=\lambda_{\min}(E_y)/\gamma.
```

The $`F_y`$ form a POVM. Refine every $`F_y`$ into rank-one positive effects by spectral decomposition, with refined label $`z=(y,a)`$. Let $`\mathcal R`$ denote this rank-one measurement channel. Coarse-graining $`z\mapsto y`$ returns the residual measurement. Define

```math
\beta=p(1-\gamma),\qquad \varepsilon=p\gamma,
```

and the enhanced channel

```math
\mathcal H(\rho)
=\delta\rho\ \oplus\ \beta\mathcal R(\rho)
\ \oplus\ \varepsilon\operatorname{Tr}(\rho)|e\rangle\langle e|.
```

The receiver now receives the branch distinguishing an intact input, a refined rank-one measurement, and an erasure. The original channel is a postprocessing of $`\mathcal H`$: retain its quantum branch, coarse-grain the refined measurement label, prepare $`y\sim\tau`$ on the erasure branch, and merge the two classical branches. Thus $`Q(\mathcal N_\delta)\leq Q(\mathcal H)`$.

At $`\gamma=0`$, use an arbitrary $`\tau`$, refine $`(E_y)`$ itself and set $`\varepsilon=0`$. At $`\gamma=1`$, the residual measurement has zero weight and is omitted. These conventions cover every endpoint without division by zero.

### Capacity of the enhancement

A rank-one measurement channel is self-complementary. If its effects are $`|v_z\rangle\langle v_z|`$, its Kraus operators may be chosen as $`K_z=|z\rangle\langle v_z|`$. The complementary output has entries

```math
\operatorname{Tr}(K_z\rho K_{z'}^\dagger)
=\delta_{zz'}\langle v_z|\rho|v_z\rangle,
```

which reproduce the same classical measurement output. A complementary channel of $`\mathcal H`$, after harmless relabeling of orthogonal flags, is therefore

```math
\mathcal H^c(\rho)
=\delta\operatorname{Tr}(\rho)|e'\rangle\langle e'|
\ \oplus\ \beta\mathcal R(\rho)
\ \oplus\ \varepsilon\rho.
```

If $`\delta\geq\varepsilon`$, a degrading map sends a fraction $`\varepsilon/\delta`$ of the intact output to the intact complementary branch. It replaces the remaining intact outputs and the erased outputs by $`|e'\rangle`$, and keeps the measurement output. Their constant-output weights sum to $`\delta-\varepsilon+\varepsilon=\delta`$, as required. Hence $`\mathcal H`$ is degradable.

If $`\delta\leq\varepsilon`$, reverse this construction: from the complementary intact branch retain a fraction $`\delta/\varepsilon`$, keep its measurement branch, and replace all remaining outputs by $`|e\rangle`$. This simulates $`\mathcal H`$ and makes it antidegradable. If both weights vanish, only the self-complementary measurement branch remains.

For every input state,

```math
I_c(\rho,\mathcal H)=(\delta-\varepsilon)S(\rho).
```

Indeed, the branch Shannon entropies cancel because the direct and complementary branch probabilities differ only by a permutation, and the measurement-output entropy is identical on both sides. Additivity of coherent information for degradable channels gives

```math
Q(\mathcal H)=\bigl[\delta-\varepsilon\bigr]_+\log_2d.
```

The antidegradable side has zero capacity by no-cloning. The degradable single-letter theorem is an established ingredient; see [Devetak and Shor](https://arxiv.org/abs/quant-ph/0311131) and [Cubitt, Ruskai and Smith](https://www.dr-qubit.org/publications/degradability.pdf). Substituting $`\varepsilon=p\gamma`$ proves the upper bound.

For noisy destructive qubit measurements this becomes

```math
\boxed{\qquad
Q(\mathcal N_{\delta,q})
\leq\bigl[\delta-2q(1-\delta)\bigr]_+.
\qquad}
```

At $`q=0`$, the measured branch consists of rank-one effects and is self-complementary. The original channel itself is then degradable, with $`I_c=\delta S(\rho)`$ and exact capacity $`Q=\delta`$ qubits per physical use. At $`q=1/2`$, the record is input independent; the bound reduces to the usual erasure capacity $`[2\delta-1]_+`$. At intermediate error it is an upper bound, not an exact formula for $`Q`$.

## Scope of the converse

These statements concern independent uses of the specified channel, with encoding before the realized survival mask, basis choices and outcomes. The decoder may use all delivered classical records. It cannot recover the discarded systems or hidden true outcomes, and it has no quantum register that bypassed the channel. The fidelity statements are unconditional and deterministic. Heralded recovery, preshared entanglement, or two-way sender–receiver assistance are different tasks and can evade these bounds.

The direct-sum channel architecture is part of the established incomplete-erasure framework of [Siddhu and Griffiths, Equation (35)](https://arxiv.org/html/2003.00583v2). The application here evaluates its exact shareability hierarchy for a classical measurement branch and uses a rank-one flagged enhancement to bound unassisted capacity. It does not identify the entire zero-capacity region: failure of antidegradability does not imply positive quantum capacity.
