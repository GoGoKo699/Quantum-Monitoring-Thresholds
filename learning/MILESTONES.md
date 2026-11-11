# Thirty milestones for Quantum Monitoring Thresholds

[Scientific account](../science/README.md) · [Preskill source bridge](PRESKILL_BRIDGE.md) · [Exact model](../science/model.md)

This is a common understanding map for the scientific project. It has two phases: **M01–M12 build the background framework**, and **M13–M30 assemble the argument and its consequences**. The 12/18 allocation gives the entropy, channel-capacity and measurement-access distinctions enough space before the new setting-count law is developed. Within each phase, individual objects and mechanisms lead to a global account of the task.

The single educational anchor is John Preskill, [*Quantum Shannon Theory*, arXiv:1604.07450v5](https://arxiv.org/abs/1604.07450v5). Page numbers below are the source's printed pages, not PDF viewer indices. The [bridge](PRESKILL_BRIDGE.md) fixes the version, translates notation and records the sign correction needed when reading Eq. (10.368): throughout this project coherent information is $`H(B)-H(E)`$. Anchor passages provide the foundations; the project-specific proofs live in the linked scientific pages.

## Phase 1 — Background and preliminaries

### M01 — One physical use and its accessible outputs

- **Central question:** What reaches the receiver when a qubit is sometimes transmitted and otherwise destructively measured?
- **Understanding target:** Distinguish the intact quantum register, reliable branch and axis labels, noisy reported sign, and inaccessible measured qubit and true outcome. Explain why a readable postmeasurement qubit would define a different task.
- **Dependencies and story role:** Entry point. Establishes the physical objects before introducing entropy or capacity.
- **Conceptual connection:** A channel is defined by accessible outputs and discarded systems, rather than by a verbal label such as “measurement noise.”
- **Source pointers:** Preskill §10.6.1, “How much can we learn from a measurement?” (p. 40), and §10.6.6, “Entanglement-breaking channels” (p. 50); [supplied channel](../science/model.md#the-supplied-channel); [access limits](../science/interpretation.md#why-access-details-matter).

### M02 — Mixed states, purification and a reference

- **Central question:** How can an apparently mixed input describe transmission of an unknown quantum state?
- **Understanding target:** Explain the role of a purification and why preserving correlations with a reference tests quantum transmission. Distinguish this mathematical reference from a noiseless receiver-side register bypassing the channel.
- **Dependencies and story role:** Uses M01. Turns the physical input/output description into the reference-based language used by all later entropy calculations and fidelity bounds.
- **Conceptual connection:** A mixed average input can belong to a coherent encoded reference–input state; a separable average density matrix does not by itself remove logical coherence.
- **Source pointers:** Preskill §10.2, “Von Neumann Entropy” (p. 13), and §10.7.2, “The decoupling principle” (p. 53); [conditional-reference cost](../science/model.md#the-conditional-reference-entropy-cost); [repetition input and purification](../science/coding.md#proof-retain-every-branch-and-record).

### M03 — Noisy measurement records as POVM effects

- **Central question:** Which measurement effects describe a correct projective measurement followed by a flipped classical report?
- **Understanding target:** Interpret $`E_{b,s}=[I+(-1)^s(1-2q)\mathbf n_b\cdot\boldsymbol\sigma]/2`$, identify the minimum effect eigenvalue $`q`$, and distinguish an axis weight from a conditional outcome effect.
- **Dependencies and story role:** Uses M01–M02. Provides the local operator from which both entropy costs and all-code converses will follow.
- **Conceptual connection:** Classical reporting errors change the receiver's effective POVM even when the underlying destructive measurement is projective.
- **Source pointers:** Preskill §10.6.1 (p. 40); [channel effects and weights](../science/model.md#the-supplied-channel); [general finite POVM](../science/shareability.md#channel-and-noise-content).

### M04 — Conditional reference entropy and unnormalized entropy

- **Central question:** What uncertainty remains in the reference after a reported measurement outcome?
- **Understanding target:** Explain the positive matrix $`\sqrt\rho E^{\mathsf T}\sqrt\rho`$ in an input eigenbasis, its trace as an outcome probability, and the function $`g(A)=\operatorname{Tr}(A)S(A/\operatorname{Tr}(A))`$. Distinguish averaging conditional entropies from taking the entropy of the average state.
- **Dependencies and story role:** Uses M02–M03. Introduces the cost $`C_{\mathsf E}`$ before using it in a channel benchmark.
- **Conceptual connection:** Keeping probabilities inside a homogeneous entropy function makes later operator comparisons valid even for inputs close to purity.
- **Source pointers:** Preskill §10.2.1, “Mathematical properties of $`H(\rho)`$” (p. 15), and §10.2.2, “Mixing, measurement, and entropy” (p. 16); [entropy-cost definition](../science/model.md#the-conditional-reference-entropy-cost); [entropy transfer](../science/setting_frontier.md#transfer-the-operator-comparison-through-entropy).

### M05 — Reliable flags and the sign of coherent information

- **Central question:** Why does the flagged channel have coherent information $`\delta S(\rho)-pC_{\mathsf E}(\rho,q)`$?
- **Understanding target:** Explain the direct-sum entropy rule, why common classical flag entropies cancel, and why conditional reference entropy is a loss rather than a positive contribution. Use the convention $`I_c=H(B)-H(E)`$ consistently.
- **Dependencies and story role:** Uses M01–M04. Assembles local branch contributions into the exact one-use identity.
- **Conceptual connection:** A physical classical record can help the decoder while still leaving quantum uncertainty unavailable to it.
- **Source pointers:** Preskill Eqs. (10.212)–(10.213) (p. 42), §10.7.1 (p. 51), and Eq. (10.275) (p. 53); [exact coherent-information identity](../science/model.md#the-conditional-reference-entropy-cost); [source sign note](PRESKILL_BRIDGE.md).

### M06 — Optimizing the one-use benchmark

- **Central question:** What must be proved before declaring optimized one-use coherent information zero?
- **Understanding target:** Interpret $`\Gamma_{\mathsf E}=\inf C_{\mathsf E}/S`$ and the odds $`x=\delta/p`$. Explain why a favorable calculation at one input cannot establish a zero benchmark and why the infimum must include inputs whose spectra and directions depend on $`q`$.
- **Dependencies and story role:** Uses M05. Converts the exact entropy identity into the first threshold to be compared.
- **Conceptual connection:** A global optimization has different quantifiers from a chosen-probe witness, including at the pure-state boundary where both numerator and denominator vanish.
- **Source pointers:** Preskill §10.7.1 and Eq. (10.273) (pp. 51–52); [optimized mixed-input ratio](../science/model.md#the-conditional-reference-entropy-cost); [uniform-bound statement](../science/haar_entropy.md#uniform-haar-bound).

### M07 — Quantum capacity and two distinct block limits

- **Central question:** How does one positive finite coding block imply positive asymptotic quantum capacity?
- **Understanding target:** Distinguish optimized one-use coherent information, a selected finite inner block, and the separate outer coding limit. Explain why positive capacity does not mean every one-use task succeeds, a practical rate is large, or a decoder is efficient.
- **Dependencies and story role:** Uses M02 and M05–M06. Introduces the second threshold without identifying it with the one-use benchmark.
- **Conceptual connection:** Regularization permits collective effects; the order in which a finite inner code and an asymptotic outer code are chosen matters.
- **Source pointers:** Preskill Eq. (10.278) (p. 53) and §10.9.4, “Quantum channel capacity revisited” (p. 75); [actual capacity threshold](../science/model.md#the-actual-capacity-threshold); [finite inner-block theorem](../science/coding.md#channel-and-statement); [bridge sign correction](PRESKILL_BRIDGE.md).

### M08 — No cloning, antidegradability and shared outputs

- **Central question:** Why can a channel that lets its environment reproduce the receiver's output not transmit arbitrary quantum information reliably?
- **Understanding target:** Explain antidegradability and the equivalent two-receiver extension picture. Distinguish a zero asymptotic rate statement from a finite-block fidelity ceiling for a fixed logical qubit.
- **Dependencies and story role:** Uses M02 and M07. Supplies the global obstruction against which the coding construction will be compared.
- **Conceptual connection:** Entanglement monogamy turns an output-simulation property into an all-code limitation.
- **Source pointers:** Preskill §10.5.3, “Entanglement monogamy” (p. 39), and §10.7.3, “Degradable channels” (p. 56), including Eq. (10.309) (p. 58); [shareability theorem](../science/shareability.md#exact-shareability-theorem); [finite-block consequences](../science/shareability.md#finite-block-fidelity-consequences).

### M09 — The input-independent part of a measurement

- **Central question:** How much of a POVM can be separated into a record that carries no input information?
- **Understanding target:** Interpret $`\gamma=\sum_y\lambda_{\min}(E_y)`$ and the decomposition into a trivial measurement plus residual positive effects. Explain why this established noise-content quantity equals $`2q`$ for every noisy projective-axis menu.
- **Dependencies and story role:** Uses M03–M04 and M08. Connects local detector effects to a channel-wide obstruction while keeping the known resource quantity distinct from its new application.
- **Conceptual connection:** Minimum effect eigenvalues simultaneously describe an uninformative measurement component and the part available to an exact shared-output construction.
- **Source pointers:** Preskill §10.6.1 and §10.6.6 (pp. 40, 50) for measurement and channel context; [noise content and attribution](../science/shareability.md#channel-and-noise-content); [related measurement quantities](../references/RELATED_WORK.md#ideal-monitoring-imperfect-records-and-the-all-code-obstruction).

### M10 — Axes, coding directions and a finite setting menu

- **Central question:** Which geometric choices belong to the apparatus, and which belong to the code?
- **Understanding target:** Distinguish the supplied axes $`\mathbf n_b`$, their known probabilities, the code direction $`\mathbf u`$, and the future random setting label. Explain why neither the encoder nor the code direction may depend on the future realized labels.
- **Dependencies and story role:** Uses M01, M03 and M07. Adds the geometrical resource that makes the project's threshold separation variable.
- **Conceptual connection:** Optimizing a code for a known channel differs from receiving the channel's random choices before encoding.
- **Source pointers:** Preskill §10.6.1 (p. 40) and §10.7.1 (p. 51); [finite ensemble definition](../science/model.md#the-supplied-channel); [coding direction and loss](../science/coding.md#channel-and-statement); [supplied apparatus](../science/interpretation.md#the-supplied-apparatus).

### M11 — Uniform estimates and charged asymptotic families

- **Central question:** What does a statement uniform in both detector error and setting budget actually require?
- **Understanding target:** Distinguish fixed-menu small-error behavior from a family in which the menu grows with decreasing error. Explain the roles of input-uniform bounds, finite setting labels, and the transformation from odds $`x`$ to intact fraction $`\delta=x/(1+x)`$.
- **Dependencies and story role:** Uses M06–M10. Prepares the quantifiers and resource accounting before the joint theorem is assembled.
- **Conceptual connection:** A supremum over menus and an infimum over all input states cannot be replaced by a fixed-geometry example or a sampled numerical minimum.
- **Source pointers:** Preskill §10.7.1 and §10.9.4 (pp. 51, 75) for operational coding context; [setting budget and limit order](../science/model.md#the-setting-budget-and-order-of-limits); [finite-menu theorem](../science/setting_frontier.md#joint-frontier-theorem).

### M12 — The complete question and its two benchmarks

- **Central question:** Which two quantities does this project compare under exactly the same supplied channel?
- **Understanding target:** Give one coherent account of the destructive interface, conditional-reference cost, globally optimized one-use threshold, actual capacity activation threshold, and setting-count resource. Identify which statement would change if records, assistance or encoding timing changed.
- **Dependencies and story role:** Integrates M01–M11. Ends the background phase with the complete operational question rather than another isolated prerequisite.
- **Conceptual connection:** Entropy optimization, coding, no cloning and geometry describe different parts of one information-transmission experiment.
- **Source pointers:** Preskill §§10.6.6–10.7.3 (pp. 50–58) and §10.9.4 (p. 75); [scientific account](../science/README.md); [model](../science/model.md); [meaning and limits](../science/interpretation.md).

## Phase 2 — Narrative and innovation

### M13 — Why two receivers cannot both get the intact branch

- **Central question:** What does the pure maximally entangled Choi block force in a shared-output extension?
- **Understanding target:** Explain why a rank-one marginal factorizes from all other receivers, and why a sector containing two intact quantum outputs would contradict that support condition.
- **Dependencies and story role:** Uses M02 and M08–M09. Begins the project argument from a local structural fact about one flagged block.
- **Conceptual connection:** The no-cloning obstruction can be proved as a positivity and support statement, before invoking an asymptotic capacity theorem.
- **Source pointers:** Preskill §10.5.3 (p. 39) and §10.7.3 (p. 56); [shareability necessity](../science/shareability.md#necessity).

### M14 — The exact multi-receiver shareability hierarchy

- **Central question:** When can the classical record accommodate all the other receivers in a shared channel?
- **Understanding target:** Reconstruct the condition $`(k-1)\delta\leq p\gamma`$ from the positive classical residual effects, and explain the matching instrument that sends the input intact to at most one receiver and classical labels to the rest.
- **Dependencies and story role:** Uses M09 and M13. Joins the local Choi constraint to a complete necessary-and-sufficient broadcast criterion.
- **Conceptual connection:** The established measurement noise content becomes the exact resource available for a shared-output construction in this flagged channel.
- **Source pointers:** Preskill §10.5.3 and §10.7.3 (pp. 39, 56) for monogamy and channel context; [exact theorem](../science/shareability.md#exact-shareability-theorem); [sufficient construction and endpoints](../science/shareability.md#sufficiency).

### M15 — From shareability to bounds on every code

- **Central question:** Which storage and rate limitations survive arbitrary encoding, blocklength and deterministic decoding?
- **Understanding target:** Explain the logical fidelity bound $`F_e\leq(D+k-1)/(Dk)`$, including $`F_e\leq3/4`$ for a logical qubit in the antidegradable region. Distinguish it from the separate upper bound $`Q\leq[\delta-p\gamma]_+\log_2d`$ obtained by a flagged rank-one enhancement.
- **Dependencies and story role:** Uses M07–M09 and M13–M14. Converts the structural theorem into unconditional operational statements.
- **Conceptual connection:** Shareability is stable under channel composition, while an enhanced receiver channel supplies a capacity bound by data processing.
- **Source pointers:** Preskill §10.2.4, “Monotonicity of mutual information” (p. 19), §10.7.3 (p. 56), and Eq. (10.281) (p. 54); [finite-block fidelity](../science/shareability.md#finite-block-fidelity-consequences); [capacity upper bound](../science/shareability.md#universal-capacity-upper-bound).

### M16 — A repetition code that counts every record

- **Central question:** How can a finite inner code preserve useful quantum coherence without selecting favorable measurement outcomes?
- **Understanding target:** Explain the antipodal-product-codeword isometry, the conditional reference–receiver states, and the exact mask-and-record sum for coherent information. Identify the negative contribution of the all-measured branch.
- **Dependencies and story role:** Uses M02, M05, M07 and M10. Introduces the inherited achievable mechanism alongside the all-code obstruction.
- **Conceptual connection:** Correlated codewords preserve logical reference coherence even though their balanced average state is separable; a complete entropy sum replaces postselection.
- **Source pointers:** Preskill §10.7.1 (p. 51) and §10.9.4 (p. 75); [complete record calculation](../science/coding.md#proof-retain-every-branch-and-record); [inherited construction](../references/RELATED_WORK.md#exact-inherited-channel-and-coding-construction).

### M17 — Why a strict gap gives one finite positive block

- **Central question:** How can favorable exponential terms overcome the record-counting polynomial without discarding failures?
- **Understanding target:** Explain the roles of $`\nu_+>\nu_-`$, the factor $`(N+1)^J`$, and the finite block-length choice. Distinguish existence of a useful finite block from a positive limit of its rate as the inner length grows.
- **Dependencies and story role:** Uses M07 and M16. Completes the achievable implication needed for the threshold comparison.
- **Conceptual connection:** A fixed finite superchannel can have positive coherent information even when a particular sequence of growing inner-code rates tends to zero.
- **Source pointers:** Preskill Eq. (10.278) (p. 53) and §10.9.4 (pp. 75–76); [finite-block statement](../science/coding.md#channel-and-statement); [record-overlap bounds](../science/coding.md#entropy-and-likelihood-bounds).

### M18 — The actual activation scale is linear in record error

- **Central question:** Why is the positive-capacity activation threshold of order $`q`$ for every finite menu?
- **Understanding target:** Combine the universal obstruction $`x\leq2q`$ with the repetition criterion and $`c\leq L\leq(c/\eta)\arcsin\eta`$. Explain why averaging over a coding direction is valid even for a fixed, nonuniform apparatus menu.
- **Dependencies and story role:** Uses M14–M17. Assembles the first global narrative result before introducing the harder one-use geometry optimization.
- **Conceptual connection:** Exact no-cloning structure and an inherited complete coding construction constrain the same actual channel threshold from opposite sides.
- **Source pointers:** Preskill §10.7.3 (p. 56) and §10.9.4 (p. 75); [actual threshold](../science/model.md#the-actual-capacity-threshold); [collective activation bounds](../science/setting_frontier.md#collective-coding-and-the-actual-activation-threshold).

### M19 — Why isotropic measurements need an input-uniform proof

- **Central question:** Why does the maximally mixed input suggest a logarithm without proving the optimized threshold?
- **Understanding target:** Explain that $`C(I/2,q)=h_2(q)`$ supplies an upper bound on $`\Gamma`$, while a lower bound must control all spectra and directions. Identify the potential escape through inputs becoming pure as $`q`$ shrinks.
- **Dependencies and story role:** Uses M06 and M11, with M18 fixing the comparison scale. Introduces the decisive uncertainty in the one-use argument.
- **Conceptual connection:** A symmetric channel need not have the maximally mixed state as the optimizer of a ratio; the desired conclusion is uniform order, not an unproved exact optimizer.
- **Source pointers:** Preskill §10.2.1 (p. 15) and §10.7.1 (p. 51); [uniform isotropic statement](../science/haar_entropy.md#uniform-haar-bound); [upper bound and limit order](../science/haar_entropy.md#upper-bound-and-limiting-order).

### M20 — A local determinant controls each conditional entropy

- **Central question:** How do input purity, detector noise and axis alignment enter a conditional reference state?
- **Understanding target:** Interpret $`D_\pm=t(1-t)q(1-q)/p_\pm^2`$ and $`D\leq e(D)\leq2D`$. Explain how a lower bound on binary entropy is obtained without assuming an invalid monotonicity of $`e\log(1/e)`$.
- **Dependencies and story role:** Uses M03–M04 and M19. Reduces the isotropic estimate to local positive quantities whose angular integral can be controlled.
- **Conceptual connection:** The determinant of a two-dimensional conditional state links physical access probabilities to the small-eigenvalue entropy responsible for the logarithm.
- **Source pointers:** Preskill §10.2.1–§10.2.2 (pp. 15–16); [conditional states and normalization](../science/haar_entropy.md#conditional-states-and-normalization); [elementary entropy estimate](../science/haar_entropy.md#an-elementary-entropy-estimate).

### M21 — The logarithm survives the near-pure limit

- **Central question:** Why can nearly pure inputs not avoid the isotropic entropy cost?
- **Understanding target:** Explain the change of variable $`y=1-\eta r x`$, the product of logarithms in the retained-outcome integral, and how the two possible relative sizes of input impurity and detector error are covered by common bounds.
- **Dependencies and story role:** Uses M11 and M19–M20. Supplies the load-bearing part of the uniform one-use lower bound.
- **Conceptual connection:** Isotropic axes contribute at many angular scales; normalization by the input entropy leaves the detector logarithm even when input impurity is much smaller than $`q`$.
- **Source pointers:** Preskill §10.2.1–§10.2.2 (pp. 15–16) for entropy properties; [inputs close to purity](../science/haar_entropy.md#inputs-close-to-purity). The angular estimate is supplied by the project proof.

### M22 — A uniform isotropic threshold, without an exact optimizer

- **Central question:** How do the near-pure and remaining spectra combine into a global $`\Theta(q\ln(1/q))`$ result?
- **Understanding target:** Explain why the complementary spectral regime can be bounded on a fixed interval of angles, then combine it with M21 and the maximally mixed upper bound. State which exact equality remains unnecessary and unproved.
- **Dependencies and story role:** Uses M19–M21. Integrates the local entropy estimates into the global isotropic benchmark.
- **Conceptual connection:** Covering all input spectra before optimization justifies simultaneous input-purity and detector-noise limits.
- **Source pointers:** Preskill §10.2.1 (p. 15) and §10.7.1 (p. 51); [remaining spectra](../science/haar_entropy.md#remaining-input-spectra); [complete isotropic bound](../science/haar_entropy.md#uniform-haar-bound).

### M23 — The upper limit imposed by at most J settings

- **Central question:** How can a coding direction exploit the gaps left by a finite measurement menu?
- **Understanding target:** Explain the excluded-cap construction, why its remaining spherical region has positive measure, and how averaging the nearly pure cost there gives an upper bound for every menu and every choice of weights.
- **Dependencies and story role:** Uses M10–M11 and M19. Establishes the universal side of the joint setting-count law rather than only analyzing a symmetric example.
- **Conceptual connection:** A finite geometric budget limits how often a code direction must approach measurement poles; the resulting logarithm is bounded by both setting count and detector error.
- **Source pointers:** Preskill §10.6.1 and §10.7.1 (pp. 40, 51) for measurement/coding context; [arbitrary-menu upper bound](../science/setting_frontier.md#upper-bound-for-every-finite-menu).

### M24 — A finite equal-weight apparatus instead of a continuous record

- **Central question:** How can finitely many known axes retain the relevant isotropic geometry?
- **Understanding target:** Describe the six-face midpoint mesh, its at-most-$`J`$ equally likely labels, and the comparison density with uniform spherical area. Account for label length and angular mesh scale.
- **Dependencies and story role:** Uses M10–M11 and M22–M23. Constructs a physical finite-menu candidate for the matching lower bound.
- **Conceptual connection:** A continuous distribution can guide a proof while the channel used by the theorem has finite controls and finite classical labels.
- **Source pointers:** Preskill §10.6.1 (p. 40) for measurement-menu context; [finite-menu construction](../science/setting_frontier.md#finite-menu-lower-bound); [apparatus resources](../science/interpretation.md#the-supplied-apparatus). The cube geometry is supplied locally.

### M25 — Transfer entropy bounds without losing nearly pure inputs

- **Central question:** Why compare a coarse mesh at error $`q`$ with an isotropic measurement at a slightly larger error?
- **Understanding target:** Explain the operator inequality $`E_{\mathbf m,s}(q)\succeq\alpha E_{\mathbf n,s}(q+h)`$, positive congruence, and homogeneity/positive-semidefinite monotonicity of $`g`$. Identify why an additive continuity error divided by a vanishing input entropy would be inadequate.
- **Dependencies and story role:** Uses M04, M20–M22 and M24. Makes the finite construction preserve the uniform lower bound at all input purities.
- **Conceptual connection:** A multiplicative operator comparison is a stronger tool here than an input-independent additive entropy error.
- **Source pointers:** Preskill §10.2.1–§10.2.2 (pp. 15–16) for entropy properties; [relaxed-error comparison](../science/setting_frontier.md#compare-a-coarse-mesh-at-error-q-with-an-isotropic-model-at-larger-error); [entropy transfer](../science/setting_frontier.md#transfer-the-operator-comparison-through-entropy).

### M26 — The matching law for every setting budget

- **Central question:** How do the finite construction and arbitrary-menu bound cover all $`J`$ and small $`q`$ uniformly?
- **Understanding target:** Assemble $`\Gamma_J^*=\Theta(q[1+\ln\min\{J,1/q\}])`$. Explain the roles of the large-menu mesh, the small-menu baseline, and universal constants rather than interpreting the conservative cutoff as a minimum required apparatus.
- **Dependencies and story role:** Uses M22–M25. Integrates the upper and lower mechanisms into the main joint theorem.
- **Conceptual connection:** Two limiting regimes and a simple baseline provide one statement valid for arbitrary simultaneous menu/noise sequences.
- **Source pointers:** Preskill §10.7.1 (p. 51) for the optimized benchmark; [joint theorem](../science/setting_frontier.md#joint-frontier-theorem); [uniform constants and small menus](../science/setting_frontier.md#uniform-constants-including-small-menus).

### M27 — An unbounded gap under the same channel

- **Central question:** In what precise sense does collective coding improve the activation threshold by a logarithm?
- **Understanding target:** Combine M18 and M26 at the same fixed $`q`$ and menu, then compare a family of such channels. Distinguish the optimized one-use threshold from the actual activation threshold and from the achieved communication rate.
- **Dependencies and story role:** Uses M12, M18 and M26. Reaches the main physical consequence of the project.
- **Conceptual connection:** An optimized one-use entropic certificate can fail over a growing interval even though an unassisted collective code has strictly positive capacity there.
- **Source pointers:** Preskill Eq. (10.278) (p. 53) and §10.9.4 (p. 75); [setting budget and same-channel ratio](../science/model.md#the-setting-budget-and-order-of-limits); [physical consequence](../science/interpretation.md#what-changes).

### M28 — Endpoints and changes of access

- **Central question:** Which nearby scenarios preserve the theorem, and which change the task?
- **Understanding target:** Explain the perfect-record and input-independent-record endpoints, a fixed-axis example, and why ideal remeasurement, advance survivor knowledge, feedback assistance or favorable-mask conditioning can evade the stated comparison.
- **Dependencies and story role:** Uses M01, M08, M15 and M27. Tests the global interpretation against physical boundary cases without extending the theorem to different resources.
- **Conceptual connection:** A mathematical limit in the same channel is different from giving the receiver or encoder a new information path.
- **Source pointers:** Preskill §10.7.3 (p. 56), including the erasure-channel discussion, and §10.5.3 (p. 39); [endpoint example](../science/interpretation.md#a-simple-endpoint-check); [access distinctions](../science/interpretation.md#why-access-details-matter); [shareability endpoints](../science/shareability.md#endpoints).

### M29 — Price the apparatus and the finite coding block

- **Central question:** What has been paid for before interpreting a positive-capacity activation result?
- **Understanding target:** Combine finite setting count, angular resolution, reliable label bits, inner block size and the explicit achievable-rate lower bound. Explain why a rate bound that can be extremely small does not establish $`Q=\Theta(q)`$, efficient outer decoding or a laboratory advantage.
- **Dependencies and story role:** Uses M07, M11, M17, M24 and M27–M28. Reconciles the theorem's threshold consequence with its complete relevant resource account.
- **Conceptual connection:** The location at which capacity becomes positive and the cost of transmitting useful information above that threshold are separate scientific quantities.
- **Source pointers:** Preskill §10.7.1 and §10.9.4 (pp. 51, 75); [explicit finite-block dependence](../science/coding.md#explicit-dependence-on-setting-count-and-noise); [coding costs](../science/interpretation.md#the-coding-cost); [established scope](../science/interpretation.md#established-scope-and-open-quantities).

### M30 — The complete scientific account

- **Central question:** What does the field learn after all inherited ingredients, assumptions and remaining gaps are stated?
- **Understanding target:** Explain the whole route from destructive noisy records to the exact shareability obstruction, complete collective coding, uniform entropy estimate, finite-menu frontier and logarithmic threshold separation. Identify the inherited channel and coding arguments, the new joint-order contribution, and the unresolved exact-capacity and efficiency questions.
- **Dependencies and story role:** Integrates M13–M29 with the background synthesis M12. Ends the narrative with the complete contribution and its qualified meaning.
- **Conceptual connection:** The new result comes from joining a uniform spectral estimate, a finite geometric resource law and an all-code boundary; neither a new channel name nor the existence of superadditivity alone supplies that conclusion.
- **Source pointers:** Preskill §§10.7.1–10.7.3 and §10.9.4 (pp. 51–58, 75–76); [scientific account](../science/README.md); [related-work boundaries](../references/RELATED_WORK.md); [resources and limits](../science/interpretation.md); [verification scope](../verification/README.md).
