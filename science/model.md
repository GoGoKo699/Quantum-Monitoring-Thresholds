# Destructive monitoring and its two activation thresholds

An encoded qubit sometimes remains quantum and otherwise leaves only a noisy classical measurement record. The intact fraction and the record quality are independent resources. This account compares the globally optimized single-use coherent-information threshold with the threshold for positive unassisted quantum capacity.

## The supplied channel

Fix a known finite ensemble of unit Bloch vectors

```math
\mathsf E=\{(w_b,\mathbf n_b):1\leq b\leq m\},
\qquad w_b>0,\quad\sum_b w_b=1.
```

With probability $`\delta`$ the physical qubit arrives intact. With probability $`p=1-\delta`$ it is destructively measured along an independently drawn axis $`b`$. If the true sign is $`r\in\{0,1\}`$, the receiver sees $`s=r\oplus z`$, with an independent Bernoulli reporting error $`\Pr(z=1)=q`$. Put

```math
0<q<\frac12,
\qquad \eta=1-2q,
\qquad c=1-\eta^2=4q(1-q),
\qquad E_{b,s}(q)=\frac{I+(-1)^s\eta\mathbf n_b\cdot\boldsymbol\sigma}{2}.
```

The receiver channel is

```math
\mathcal N_{\delta,q,\mathsf E}(\rho)
=\delta\rho\ \oplus\ p\sum_{b,s}w_b\operatorname{Tr}(E_{b,s}(q)\rho)|b,s\rangle\langle b,s|.
```

The direct sum supplies a reliable intact/measured flag. Axis labels are reliable too. The measured qubit, the true outcome and the error bit are inaccessible. There is one acquisition per measured qubit. Encoding precedes every realized mask, axis and outcome. Repeated physical uses are independent copies of this fixed channel.

Encoder and decoder operations are otherwise unrestricted and noiseless. The task uses no preshared entanglement, feedback assistance, postselection or retained quantum register bypassing the exposed block. Classical randomness and computation are unrestricted. A reference used to define entanglement transmission does not supply a receiver with a noiseless bypass.

This channel model is inherited from [Measurement Geometry and Coherent-Information Superadditivity](https://github.com/GoGoKo699/Measurement-Geometry-Superadditivity/tree/99bdd710abbf7258be941ae83f46b7c9ea9702f8); its direct-sum architecture is an established incomplete-erasure channel. The [related-work account](../references/RELATED_WORK.md) separates these ingredients from the present joint noise/setting-count law.

## The conditional-reference entropy cost

All entropies are in bits, while $`\ln`$ is the natural logarithm. For a positive operator $`A`$, define

```math
g(A)=\operatorname{Tr}(A)S\!\left(\frac{A}{\operatorname{Tr}(A)}\right),
\qquad g(0)=0.
```

For an input state $`\rho`$, set

```math
C_{\mathsf E}(\rho,q)
=\sum_{b,s}w_b\,g\!\left(\sqrt\rho E_{b,s}(q)\sqrt\rho\right).
```

The operators in this expression have the spectra of the unnormalized conditional reference states, up to transposition in a purification basis. Thus $`C_{\mathsf E}`$ is the average conditional reference entropy in the measured branch. Reliable flag entropies cancel in coherent information, yielding the exact identity

```math
I_c(\rho,\mathcal N)=\delta S(\rho)-pC_{\mathsf E}(\rho,q).
```

For a pure input both terms vanish. Define the optimized mixed-input ratio

```math
\Gamma_{\mathsf E}(q)
=\inf_{\rho:\,S(\rho)>0}\frac{C_{\mathsf E}(\rho,q)}{S(\rho)},
\qquad
Q^{(1)}(\mathcal N)=\max_\rho I_c(\rho,\mathcal N).
```

For $`\delta<1`$, the intact-transmission **odds** are $`x=\delta/p`$. Then

```math
Q^{(1)}(\mathcal N)=0\quad\Longleftrightarrow\quad x\leq\Gamma_{\mathsf E}(q),
\qquad
Q^{(1)}(\mathcal N)>0\quad\Longleftrightarrow\quad x>\Gamma_{\mathsf E}(q).
```

The infimum includes input spectra approaching purity and directions that depend on $`q`$. A calculation at the maximally mixed state alone is insufficient for a zero-$`Q^{(1)}`$ claim. Also, $`Q^{(1)}`$ is an optimized entropic achievable-rate benchmark; it is not an operational one-shot capacity and does not characterize every single-use task.

## The actual capacity threshold

Let $`Q(\mathcal N)`$ be the unassisted asymptotic quantum capacity per physical channel use, and write

```math
\mathcal N_{x,q,\mathsf E}:=\mathcal N_{x/(1+x),q,\mathsf E},
\qquad
x_c(\mathsf E,q):=\inf\{x\geq0:Q(\mathcal N_{x,q,\mathsf E})>0\}.
```

Capacity is nondecreasing in $`x`$. To simulate a smaller intact fraction, the receiver can destructively measure an independently selected part of the intact branch using the supplied ensemble, relabeling it as measured. This is receiver post-processing.

The [shareability converse](shareability.md) and [inherited all-record coding construction](coding.md) establish, for every finite ensemble,

```math
2q\leq x_c(\mathsf E,q)\leq L_{\mathsf E}(q),
\qquad
L_{\mathsf E}(q):=
\min_{\|\mathbf u\|=1}\sum_b
\frac{w_b c}{\sqrt{1-\eta^2(\mathbf n_b\cdot\mathbf u)^2}}.
```

The upper bound concerns the infimum activation threshold: capacity is positive for every strict $`x>L_{\mathsf E}`$. It does not settle capacity at equality or the region between the two bounds. Averaging over a uniform auxiliary coding direction gives

```math
c\leq L_{\mathsf E}(q)
\leq\frac{c}{\eta}\arcsin\eta.
```

Hence $`x_c(\mathsf E,q)=\Theta(q)`$ uniformly over all finite menus at sufficiently small $`q`$. Uniformity here concerns the threshold bounds. Inner block lengths, rates and decoders need not be uniform over menus.

## The setting budget and order of limits

For at most $`J\geq1`$ known axes, define

```math
\Gamma_J^*(q)=\sup_{\mathsf E:\,|\mathsf E|\leq J}\Gamma_{\mathsf E}(q).
```

The [setting frontier](setting_frontier.md) proves the joint law

```math
\Gamma_J^*(q)
=\Theta\!\left(q\left[1+\ln\min\{J,1/q\}\right]\right),
```

with constants independent of $`q,J`$ for all sufficiently small $`q`$. Combining it with the uniform actual threshold gives

```math
\sup_{|\mathsf E|\leq J}
\frac{\Gamma_{\mathsf E}(q)}{x_c(\mathsf E,q)}
=\Theta\!\left(1+\ln\min\{J,1/q\}\right).
```

Each ratio compares the same fixed channel, error and menu. One may then study a family with shrinking $`q`$ and growing $`J`$. For the constructed dense meshes with angular resolution $`O(q)`$ and $`J=\Theta(q^{-2})`$ labels, the single-use threshold is $`\Theta(q\ln(1/q))`$ while the true activation threshold is $`\Theta(q)`$. The corresponding intact-fraction thresholds are obtained by $`\delta=x/(1+x)`$ and have the same small-$`q`$ orders.

First fix a finite channel, choose a useful finite inner block, and take the separate asymptotic outer-coding limit. Only afterward compare the small-noise/menu family. A continuous Haar ensemble is an analytical tool; the final construction uses finite settings and finite labels.

The [resource account](interpretation.md) states the setting-generation, angular precision, label and block-length costs and the limitations of this activation result.
