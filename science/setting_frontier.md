# How many measurement settings change the communication threshold?

[Model](model.md) · [Uniform isotropic bound](haar_entropy.md) · [Collective coding](coding.md)

The same physical channel has two benchmarks: coherent information optimized over every single-qubit input, and positive quantum capacity with collective coding. Their separation depends on how the number of available measurement settings grows as detector records become more accurate. The channel and repetition mechanism are inherited; the result here is their joint setting-count and detector-error frontier.

## Definitions and result

Let $`\mathcal E=\{(w_j,\mathbf n_j)\}_{j=1}^{K}`$ be a known finite axis ensemble, with $`w_j>0`$ and $`\sum_jw_j=1`$. The axis label and intact-versus-measured flag are reliable. Each destructive outcome record has common BSC error $`q`$. The measured qubit and true outcome are inaccessible. The [model](model.md) defines the exact conditional-reference cost $`C_{\mathcal E}(\rho,q)`$ and

```math
\Gamma_{\mathcal E}(q)
=\inf_{S(\rho)>0}\frac{C_{\mathcal E}(\rho,q)}{S(\rho)},
\qquad
\Gamma_J^*(q)=\sup_{|\mathcal E|\leq J}\Gamma_{\mathcal E}(q).
```

The supremum allows arbitrary known weights and axes. It allows fewer than $`J`$ settings. Repeated or sign-reversed labeled axes may be merged without changing the measurement channel, up to outcome relabeling.

Write $`\delta=1-p`$ for intact-transmission probability. For $`p>0`$, the supplied channel has odds $`x=\delta/p`$. Its optimized one-use coherent information is zero exactly when $`x\leq\Gamma_{\mathcal E}(q)`$. This optimization is over all input states, not only a fixed probe or the maximally mixed state.

<a id="joint-frontier-theorem"></a>
**Joint frontier.** There are universal positive constants such that, for every integer $`J\geq1`$ and $`0<q\leq1/64`$,

```math
\frac1{10000}\,q\!\left[1+\ln\min\{J,1/q\}\right]
\leq\Gamma_J^*(q)
\leq8q\!\left[1+\ln\min\{J,1/q\}\right].
```

The numerical constants are conservative. In particular,

```math
\Gamma_J^*(q)
=\Theta\!\left(q\,[1+\ln\min\{J,1/q\}]\right),
```

uniformly in the simultaneous choices of $`q`$ and $`J`$.

For every finite ensemble, its actual positive-quantum-capacity activation odds $`x_c(\mathcal E,q)`$ obey

```math
2q\leq x_c(\mathcal E,q)
\leq L_{\mathcal E}(q)
\leq\frac{4q(1-q)}{1-2q}\arcsin(1-2q)
=\Theta(q).
```

The exact all-code boundary between these bounds is not determined. Together, these statements show that the greatest one-use-to-capacity threshold ratio permitted by $`J`$ settings has order $`1+\ln\min\{J,1/q\}`$. This is a capacity-activation result; it gives no uniform lower bound on the resulting rate or efficient-decoding guarantee.

## Upper bound for every finite menu

Set $`\eta=1-2q`$ and $`c=4q(1-q)`$. For an input approaching purity along Bloch direction $`\mathbf u`$, the [conditional-entropy formula](model.md) gives

```math
G_{\mathcal E}(\mathbf u)
=\sum_j\frac{w_jc}{1-\eta^2(\mathbf n_j\!\cdot\!\mathbf u)^2},
\qquad
\Gamma_{\mathcal E}(q)\leq\min_{\|\mathbf u\|=1}G_{\mathcal E}(\mathbf u).
```

For completeness, at fixed $`q>0`$ the normalized conditional determinant for a smaller input eigenvalue $`t`$ is $`tq(1-q)/p_\pm^2+O(t^2)`$. Its entropy has leading term $`[tq(1-q)/p_\pm^2]\log_2(1/t)`$. Summing the probability-weighted outcomes and dividing by $`h_2(t)`$ yields the displayed $`G`$. This expansion is used only for the upper bound; the [uniform lower bound](haar_entropy.md) does not exchange the purity and detector-error limits.

Choose an auxiliary uniformly random direction $`\mathbf u`$. For each of the at most $`J`$ axes, remove the caps

```math
|\mathbf n_j\!\cdot\!\mathbf u|>1-\varepsilon,
\qquad\varepsilon=\frac1{2J}.
```

Each two-cap set has normalized spherical measure $`\varepsilon`$. The remaining region $`R`$ has measure at least $`1/2`$. For any fixed axis,

```math
\int_R\frac{c\,d\mu(\mathbf u)}{1-\eta^2(\mathbf n_j\!\cdot\!\mathbf u)^2}
\leq\frac c\eta\operatorname{artanh}\!\left[\eta\!\left(1-\frac1{2J}\right)\right].
```

Average the weighted sum on $`R`$ to obtain the explicit bound

```math
\Gamma_{\mathcal E}(q)
\leq\frac{2c}{\eta}\operatorname{artanh}\!\left[\eta\!\left(1-\frac1{2J}\right)\right].
```

Since

```math
1-\eta\!\left(1-\frac1{2J}\right)=2q+\frac\eta{2J},
```

one has

```math
2\operatorname{artanh}z
\leq\min\!\left\{\ln(1/q),\ln J+\ln(4/\eta)\right\},
\quad z=\eta\!\left(1-\frac1{2J}\right).
```

On $`q\leq1/64`$, $`\eta\geq31/32`$, $`c/\eta\leq128q/31`$ and $`\ln(4/\eta)<3/2`$. Writing $`M=\ln\min\{J,1/q\}`$, the minimum is at most $`M+3/2\leq(3/2)(1+M)`$. The upper bound is therefore less than $`8q(1+M)`$. This proves the upper theorem bound for arbitrary weights and geometry. A fixed finite menu cannot produce a divergent small-$`q`$ ratio.

## Finite menu lower bound

<a id="finite-menu-lower-bound"></a>
The construction uses a finite equal-weight grid, so its setting probabilities need no continuum sampler or area-weight lookup.

For $`J\geq6`$, take $`m=\lfloor\sqrt{J/6}\rfloor`$. On each face of the cube $`[-1,1]^3`$, subdivide its two free coordinates into $`m\times m`$ equal squares. Radially project each square midpoint onto the unit sphere and assign every resulting label weight $`1/(6m^2)`$. There are $`6m^2\leq J`$ labels. Antipodal representatives can be merged if distinct unoriented measurement bases are counted.

Radial projection on a cube face is Lipschitz with constant at most one, because the face's fixed coordinate has magnitude one. Each spherical cell and its representative are therefore separated by at most

```math
h=\frac{2\sqrt2}{m}\leq\frac{16}{\sqrt J}.
```

Before discretization, choose a cube face uniformly and its two free coordinates uniformly in $`[-1,1]^2`$, then radially project. Call the resulting spherical measure $`\nu`$. On a face with coordinates $`u,v`$,

```math
d\nu=\frac{du\,dv}{24},\qquad
d\mu=\frac{du\,dv}{4\pi(1+u^2+v^2)^{3/2}}.
```

Thus $`d\nu/d\mu\geq\pi/6`$. The continuous comparison cost satisfies

```math
C_\nu(\rho,q')\geq\frac\pi6 C_{\mathrm H}(\rho,q').
```

Cube-face seams have measure zero and do not affect this comparison.

### Compare a coarse mesh at error $`q`$ with an isotropic model at larger error

Let $`q'=q+h`$, assume $`q'\leq1/16`$, and set

```math
\alpha=\frac q{q'+h/2}.
```

For a cell representative $`\mathbf m`$ and any direction $`\mathbf n`$ in its cell, write $`E_{\mathbf n,s}(q)=[I+(-1)^s(1-2q)\mathbf n\cdot\boldsymbol\sigma]/2`$. Then

```math
E_{\mathbf m,s}(q)\succeq\alpha E_{\mathbf n,s}(q').
```

To check the operator inequality, put $`\eta'=1-2q'`$. The Bloch-vector triangle inequality gives

```math
\|\eta\mathbf m-\alpha\eta'\mathbf n\|
\leq\eta-\alpha\eta'+\alpha\eta' h,
```

while

```math
1-\alpha-(\eta-\alpha\eta'+\alpha\eta'h)
=2q-2\alpha q'-\alpha\eta'h\geq0.
```

This proves positivity of the scalar part minus the Bloch-vector norm. It is valid even when $`h`$ exceeds the original detector error $`q`$.

### Transfer the operator comparison through entropy

For a positive matrix $`A`$, define the unnormalized entropy

```math
g(A)=\operatorname{Tr}(A)\,S\!\left(A/\operatorname{Tr}(A)\right),\qquad g(0)=0.
```

It is homogeneous and concave. Therefore $`g(A+B)\geq g(A)+g(B)`$, and its nonnegativity implies monotonicity in positive-semidefinite order. Passing the effect inequality through the positive congruence $`E\mapsto\sqrt\rho E\sqrt\rho`$ gives the same inequality for each entropy contribution. Integrating each cell proves, uniformly over all input states,

```math
C_{\mathrm{mesh}}(\rho,q)
\geq\alpha C_\nu(\rho,q')
\geq\frac\pi6\alpha C_{\mathrm H}(\rho,q').
```

Apply the [uniform isotropic bound](haar_entropy.md#uniform-haar-bound). Since $`q'\geq h`$, one has $`\alpha q'\geq2q/3`$. Hence

```math
\Gamma_{\mathrm{mesh}}(q)
\geq\frac\pi{576}\,q\ln\frac1{q+h}.
```

### Uniform constants, including small menus

Take $`q_0=1/64`$ and $`J_0=2^{20}`$. For $`J\geq J_0`$, the preceding mesh has $`h\leq1/64`$ and $`q'=q+h\leq1/32`$. Also $`\ln(1/h)\geq\frac3{10}\ln J`$. Let $`B=\ln(1/q)`$. Then

```math
\begin{aligned}
\ln\frac1{q+h}
&\geq\min\{B,\ln(1/h)\}-\ln2\\
&\geq\tfrac18\min\{B,\ln J\}\\
&\geq\tfrac1{10}\left[1+\ln\min\{J,1/q\}\right].
\end{aligned}
```

For the middle step, $`\ln(1/h)\geq(\ln J)/2-\ln16\geq3(\ln J)/10`$ follows from $`\ln J\geq20\ln2`$. Thus $`\min\{B,\ln(1/h)\}\geq3\min\{B,\ln J\}/10`$, and subtracting $`\ln2`$ leaves at least one eighth of that minimum, since it is at least $`\ln64`$. The last step uses $`\min\{B,\ln J\}\geq\ln64>4`$. Thus the mesh lower bound is stronger than the theorem's constant $`1/10000`$.

For $`1\leq J<J_0`$, one fixed axis suffices. Its effects split as

```math
E_s(q)=(1-2q)P_s+2q\,I/2.
```

Superadditivity of $`g`$ shows that the trivial-measurement component alone contributes $`2qS(\rho)`$ to the cost. Hence $`\Gamma\geq2q`$, whereas $`1+\ln\min\{J,1/q\}\leq1+\ln J_0`$. This again implies the stated theorem constant. The sharper inherited single-axis value is unnecessary here. The large cutoff only makes the proof constants explicit; it is not a claimed minimum experimental menu size.

## Collective coding and the actual activation threshold

The [all-record repetition construction](coding.md) uses the direction-dependent loss

```math
L_{\mathcal E}(q)
=\min_{\|\mathbf u\|=1}
\sum_j\frac{w_jc}{\sqrt{1-\eta^2(\mathbf n_j\cdot\mathbf u)^2}}.
```

Every kernel is at least $`c`$. Its uniform average over $`\mathbf u`$ is $`(c/\eta)\arcsin\eta`$, independently of the measurement axis. Therefore

```math
c\leq L_{\mathcal E}(q)\leq\frac c\eta\arcsin\eta=\Theta(q).
```

For every fixed supplied finite ensemble and error, the inherited coding theorem selects a finite inner block with positive coherent information when $`x>L_{\mathcal E}`$, then applies asymptotic outer coding. The selected block length and rate can depend strongly on the channel. This theorem supplies positivity, not a uniform rate or efficient decoder.

For the converse, the [shareability theorem's antidegradability consequence](shareability.md) applies to every finite POVM. Its threshold is the sum of the smallest effect eigenvalues. For the present noisy projective-axis effects, that sum is $`2q`$, independent of the axes and weights. Consequently no code can approach reliable unconditional quantum transmission when $`x\leq2q`$.

Quantum capacity is nondecreasing in $`x`$: the receiver can simulate a smaller intact fraction by applying the same known noisy measurement to an appropriate fraction of intact outputs. Defining

```math
x_c(\mathcal E,q)=\inf\{x\geq0:Q(\mathcal N_{x,\mathcal E,q})>0\}
```

therefore gives the activation bounds stated above. Endpoint equality and the exact constant between $`2q`$ and $`L_{\mathcal E}`$ are left open.

## What is added, and what is supplied

The incomplete-erasure channel framework, its conditional-reference formula and the finite all-record repetition mechanism are existing ingredients. In particular, a positive repetition block for the present channel is not a new result. The addition is a matching joint law for the optimized one-use threshold under arbitrary finite setting budgets, together with its comparison to the uniformly linear all-code activation scale.

All benchmarks use the same supplied $`q`$ and the same menu before taking any asymptotic limit. The code is chosen from known channel parameters, never from future realized axes or outcomes. A change of menu with $`q`$ is an explicit resource, rather than a fixed-geometry theorem silently extrapolated to a singular limit.

The construction has at most $`J`$ equally likely labels, needs $`\lceil\log_2 J\rceil`$ reliably delivered setting bits per measured use, and has angular mesh scale $`O(J^{-1/2})`$. A representative is described by a cube face and two integer grid indices; normalization determines its direction. The theorem assumes these known settings and noiseless unrestricted encoding/decoding. It does not claim a gate-count, calibration-cost or laboratory-runtime advantage. Approximate controls must be checked against their actual POVM effects; a label count alone does not establish such implementation accuracy.
