# Quantum Monitoring Thresholds

**How many surviving qubits are needed when destructive measurements leave noisy outcome records?**

Each physical qubit either arrives intact or is destructively measured along a known random axis. The receiver gets the axis and an imperfect sign, but cannot recover the measured qubit or its true outcome.

For reporting error $`q`$ and at most $`J`$ known measurement settings, this project establishes the joint law

```math
\Gamma_J^*(q)
=\Theta\!\left(q\left[1+\ln\min\{J,1/q\}\right]\right).
```

Here $`\Gamma_J^*`$ is the largest globally optimized one-use coherent-information activation threshold among the allowed menus. By contrast, the actual unassisted positive-quantum-capacity threshold is $`\Theta(q)`$ for every finite menu. Dense finite menus therefore produce an unbounded logarithmic separation between these two thresholds under the same supplied channel.

**[Read the scientific account](science/README.md)** · [Exact model and claims](science/model.md) · [Joint setting/noise theorem](science/setting_frontier.md) · [Reproduce the finite checks](verification/README.md)

| Result | Meaning | Proof |
|---|---|---|
| Joint setting/noise law | Maximum one-use threshold is of order $`q[1+\ln\min\{J,1/q\}]`$ | [Setting frontier](science/setting_frontier.md) |
| Uniform actual activation scale | Positive capacity needs and admits intact-transmission odds of order $`q`$ | [Coding](science/coding.md) and [converse](science/shareability.md) |
| Exact arbitrary-POVM shareability | Noise content fixes the number of receivers that can share the flagged channel | [Shareability theorem](science/shareability.md) |
| Finite apparatus and block account | Explicit setting labels, angular resolution and a sufficient finite coding block | [Resources and limits](science/interpretation.md) |

The channel model and all-record repetition mechanism are inherited from [Measurement Geometry and Coherent-Information Superadditivity](https://github.com/GoGoKo699/Measurement-Geometry-Superadditivity/tree/99bdd710abbf7258be941ae83f46b7c9ea9702f8). The new result concerns the joint small-noise/growing-menu regime and its coding-independent boundary. [Attribution and comparison](references/RELATED_WORK.md) identify the imported arguments.

The capacity claim guarantees a positive asymptotic rate. The explicit lower bound can be very small, and no efficient outer decoder or laboratory-runtime advantage is established. Reliable branch/axis labels, inaccessible measured systems, independent errors, and encoding before the random measurement choices are essential. [Full scope](science/model.md) · [Interpretation](science/interpretation.md).

## Reproduce

```bash
python -m pip install -r requirements.txt
python verification/check_science.py --output build/science-checks.json
python verification/check_docs.py
```

The finite suite checks selected matrices, entropy inequalities, quadratures and block bounds. Universal claims rely on the analytical proofs. [Verification scope](verification/README.md).

## Purpose and contact

This repository serves as a record of the work and a guide for the author's self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
