# Meaning, resources and limits

## What changes

The receiver may retain only a small random fraction of the physical quantum systems while receiving noisy classical records from the rest. A common single-use benchmark says no positive coherent-information rate is available below a geometry-dependent survivor threshold. A collective code can remain useful at a smaller survivor fraction.

The [joint frontier](setting_frontier.md) quantifies the largest possible gap. At fixed small reporting error $`q`$ and setting budget $`J`$, the optimized single-use threshold can exceed the actual capacity activation threshold by order $`1+\ln\min\{J,1/q\}`$. A dense finite menu realizes the logarithmic regime. The [all-code converse](shareability.md) shows that changing geometry or using larger codes cannot reduce the actual activation scale below order $`q`$.

The channel and repetition-code mechanism are inherited from [Measurement Geometry and Coherent-Information Superadditivity](https://github.com/GoGoKo699/Measurement-Geometry-Superadditivity/tree/99bdd710abbf7258be941ae83f46b7c9ea9702f8). The present advance concerns their joint small-noise/growing-apparatus regime and the coding-independent boundary. Fixed-interior-error full-span results alone do not establish this limit.

## A simple endpoint check

For one fixed measurement axis, a perpendicular nearly pure input gives the exact inherited ratio $`\Gamma=c=4q(1-q)`$. At $`q=0.1`$, this is $`0.36`$ in intact-transmission odds. An intact fraction $`\delta=0.3`$ has odds $`3/7>0.36`$, so positive one-use coherent information is possible. At $`\delta=0.1`$, the odds are $`1/9<2q`$, and every deterministic code is inside the antidegradable region. These are distinct channel points, illustrating how the definitions and converse are used.

A fixed finite menu cannot produce an unbounded small-noise ratio: a coding direction can avoid its finitely many poles. The excluded-cap proof makes this quantitative. A growing mesh prevents that avoidance at enough angular scales to generate the logarithm.

## The supplied apparatus

The finite construction uses known projective measurement settings, independent setting draws, accurate setting labels and one noisy sign per measured qubit. The menu is fixed before encoding. It is not chosen from the input or from future realized measurement outcomes.

The constructed six-face spherical grid at angular resolution $`O(q)`$ uses $`J=\Theta(q^{-2})`$ labels. Its axis labels cost $`O(\log(1/q))`$ reliable classical bits per measured use. The [frontier proof](setting_frontier.md) gives a finite description and sampling route. The result measures quantum capacity per physical qubit channel use; it does not treat the classical label cost, basis controls or detector calibration as a laboratory-runtime advantage.

## The coding cost

The [coding proof](coding.md) counts every mask and report, including the all-measured event. It gives an explicit sufficient finite inner-block length and a strictly positive achievable-rate lower bound. The outer code is asymptotic. The bound can be very small, especially for a growing menu close to its activation frontier.

The repetition isometry uses known one-qubit basis changes and a linear number of entangling gates in the inner length. This does not make the outer decoder efficient. Ideal preparation, storage and known control operations are part of the model; additional faults can change the result.

## Why access details matter

If measured systems remain available for ideal remeasurement, the true sign can be recovered and this destructive channel no longer describes the experiment. Knowing realized survivor locations before encoding also changes the problem. Preshared entanglement, feedback-assisted distillation, retained bypass memory and conditioning on favorable masks are additional resources. The theorems make no claim about those modified tasks.

The ideal-record endpoint is consistent: at $`q=0`$, the measured branch has pure conditional reference states, and the degradable channel has capacity $`\delta`$ qubits per use. Any fixed positive $`q`$ instead leaves an all-code zero-capacity interval near total destructive monitoring. This is a statement about the stated channel interface, not a contradiction of ideal-outcome monitored-code theorems.

## Established scope and open quantities

Established are the joint setting/noise order, the actual activation scale, the exact finite-POVM shareability hierarchy and explicit finite-block coding bounds. Exact capacity and leading transition constants remain open between the no-cloning and construction boundaries. The proof does not establish an optimal rate, an efficient outer decoder, a fault-tolerant implementation or experimental crossover.

Numerical evidence suggesting an exact Haar ratio $`\Gamma=h_2(q)`$ is not used by the analytical theorem. The uniform bounds proved here suffice. The [verification guide](../verification/README.md) distinguishes these finite checks from the universal arguments.
