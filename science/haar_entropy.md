# A uniform entropy cost for isotropic measurement axes

[Model](model.md) · [Setting frontier](setting_frontier.md) · [Collective coding](coding.md)

The one-use benchmark must optimize over every qubit input, including states that approach purity as the detector error vanishes. A calculation at the maximally mixed input alone cannot establish that benchmark. This page proves the uniform estimate needed for the setting-count frontier.

The channel and its conditional-reference entropy cost are defined in the [model](model.md). The detector flips the outcome bit with common probability $`0<q<1/2`$. The measurement axis is reliably reported; the measured qubit and true outcome are inaccessible. The isotropic axis distribution on this page is an analytical comparison measure. [A finite construction](setting_frontier.md#finite-menu-lower-bound) realizes the same order without a continuous setting label.

## Statement

<a id="uniform-haar-bound"></a>
Let $`C_{\mathrm H}(\rho,q)`$ be the mean conditional-reference entropy for a uniformly distributed Bloch axis, and write $`h_2`$ for binary entropy in bits. Then, for every qubit state and $`0<q\leq1/16`$,

```math
C_{\mathrm H}(\rho,q)\geq\frac{q\ln(1/q)}{64}\,S(\rho).
```

At the maximally mixed state, $`C_{\mathrm H}(I/2,q)=h_2(q)`$. Consequently

```math
\frac{q\ln(1/q)}{64}
\leq \Gamma_{\mathrm H}(q)
:=\inf_{S(\rho)>0}\frac{C_{\mathrm H}(\rho,q)}{S(\rho)}
\leq h_2(q)
\leq2q\ln(1/q).
```

In particular, $`\Gamma_{\mathrm H}(q)=\Theta(q\ln(1/q))`$. The constants are uniform in the input spectrum. No equality $`\Gamma_{\mathrm H}=h_2(q)`$ is asserted or needed.

## Conditional states and normalization

By rotational invariance, take the smaller input eigenvalue to be $`t\in[0,1/2]`$ and its Bloch-vector length to be $`r=1-2t`$. Set

```math
\eta=1-2q,\qquad K=t(1-t)q(1-q).
```

If $`x`$ is the cosine of the angle between the input Bloch direction and the measurement axis, the two reported probabilities are

```math
p_\pm(x)=\frac{1\pm\eta r x}{2}.
```

For the canonical purification of $`\rho`$, the unnormalized conditional reference matrix is $`A_\pm=\sqrt\rho\,E_\pm^{\mathsf T}\sqrt\rho`$. Its trace is $`p_\pm`$ and its determinant is $`K`$. Thus the determinant of the normalized conditional state is

```math
D_\pm(x)=\frac{K}{p_\pm(x)^2}.
```

Its smaller eigenvalue is $`e(D)=(1-\sqrt{1-4D})/2`$. Uniform spherical measure makes $`x`$ uniform on $`[-1,1]`$. Exchanging the two outcomes under $`x\mapsto-x`$ gives the useful normalization

```math
C_{\mathrm H}(t,q)
=\int_0^1\left[p_-(x)h_2(e(D_-(x)))
+p_+(x)h_2(e(D_+(x)))\right]dx.
```

At $`t=0`$ the reference is pure and both sides of the claimed inequality vanish. The ratio defining $`\Gamma`$ uses $`t>0`$.

## An elementary entropy estimate

For $`0<D\leq1/4`$, the identity $`D=e(1-e)`$ implies $`D\leq e\leq2D`$. Therefore

```math
\begin{aligned}
h_2(e)
&\geq e\log_2(1/e)\\
&\geq D\log_2(1/(2D))\\
&\geq\frac D2\log_2(1/D).
\end{aligned}
```

The middle step uses both $`e\geq D`$ and $`\log_2(1/e)\geq\log_2(1/(2D))\geq0`$. It does not assume that $`e\log(1/e)`$ is increasing over the entire interval. The final step uses $`\log_2(1/D)\geq2`$.

## Inputs close to purity

Assume $`0<t\leq1/16`$, and define

```math
A=\ln(1/t),\quad B=\ln(1/q),\quad
b=1-\eta r=2(t+q-2tq),\quad L=\ln(1/b).
```

Retain only the negative-outcome contribution. Substituting $`y=1-\eta r x`$, so that $`p_-=y/2`$, into the entropy estimate yields

```math
\begin{aligned}
C_{\mathrm H}(t,q)
&\geq\frac{K}{\eta r\ln2}
\int_b^1\frac1y\ln\frac{y^2}{4K}\,dy\\
&=\frac{K}{\eta r\ln2}\,
L\ln\frac b{4K}.
\end{aligned}
```

All conditional determinants are physical: for example, $`b^2-16K=4(t-q)^2\geq0`$. No approximation in the input eigenvalue was made in this integral.

Because $`t,q\leq1/16`$, both $`A`$ and $`B`$ are at least $`\ln16`$. The bounds

```math
2\max(t,q)\leq b\leq4\max(t,q),\qquad K\leq tq
```

give

```math
L\geq\tfrac12\min(A,B),\qquad
\ln\frac b{4K}\geq\tfrac34\max(A,B).
```

Also $`K\geq(15/16)^2tq`$ and $`1/(\eta r)\geq1`$. Hence

```math
C_{\mathrm H}(t,q)
\geq\frac{(15/16)^2(3/8)}{\ln2}\,tqAB.
```

Finally,

```math
h_2(t)\leq\frac{t(A+1)}{\ln2},\qquad A\geq\ln16,
```

so this regime in fact gives $`C_{\mathrm H}/h_2(t)\geq qB/8`$. The weaker constant $`1/64`$ leaves room to combine it with the remaining spectra.

## Remaining input spectra

Now let $`1/16\leq t\leq1/2`$ and restrict the axis integral to $`0\leq x\leq1/2`$. Both outcome probabilities lie in $`[1/4,3/4]`$. On this interval,

```math
D_\pm\leq4q\leq1/4,\qquad
\ln(1/D_\pm)\geq B-\ln4\geq B/2,
```

and

```math
K\geq\frac{225}{4096}q.
```

For either outcome, the elementary entropy estimate therefore gives

```math
p_\pm h_2(e(D_\pm))
\geq\frac{p_\pm D_\pm}{4\ln2}B
\geq\frac{K}{3\ln2}B.
```

There are two outcomes and an integration interval of length $`1/2`$. Thus

```math
C_{\mathrm H}(t,q)
\geq\frac{225}{12288\ln2}\,qB
>\frac{qB}{64}.
```

Since $`h_2(t)\leq1`$, this proves the required bound throughout the remaining regime, including the maximally mixed endpoint.

## Upper bound and limiting order

At $`t=1/2`$, every conditional reference state has eigenvalues $`q,1-q`$, so its entropy is $`h_2(q)`$. Also

```math
h_2(q)\leq\frac{q[\ln(1/q)+1]}{\ln2}
\leq2q\ln(1/q)\qquad(0<q\leq1/16).
```

The lower estimate holds before optimizing over $`t`$, and its constant is independent of $`t`$. It therefore covers joint sequences in which the input approaches purity arbitrarily rapidly as $`q\downarrow0`$. A nearly pure expansion taken at a fixed direction would not by itself supply this uniform conclusion.

The determinant formula and one-use entropy criterion are inherited from the [measurement-channel model](model.md). The addition here is the uniform isotropic lower bound and its use in the [finite-setting frontier](setting_frontier.md). Neither finite numerical sampling nor the maximally mixed upper bound establishes an exact optimizer.
