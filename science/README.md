# Scientific account

The central distinction is between the optimized one-use coherent-information threshold and the actual unassisted quantum-capacity activation threshold. Both concern a qubit that arrives intact or is destructively measured with one noisy classical outcome record.

For small reporting error $`q`$, actual activation requires intact-transmission odds of order $`q`$ for every finite measurement menu. The greatest optimized one-use threshold attainable with at most $`J`$ settings is instead

```math
\Theta\!\left(q\left[1+\ln\min\{J,1/q\}\right]\right).
```

Thus a growing finite menu permits a logarithmically unbounded activation-threshold separation. This compares thresholds under the same channel; it does not assert an efficient decoder or a useful communication rate at the lower threshold.

| Scientific question | Authoritative account |
|---|---|
| What is supplied, discarded and charged? | [Channel, entropy cost and activation definitions](model.md) |
| Why is the near-pure input regime essential? | [Uniform Haar entropy lower bound](haar_entropy.md) |
| What can at most J settings accomplish? | [Joint setting-count/noise frontier](setting_frontier.md) |
| Why can no code succeed below the universal boundary? | [Exact shareability and capacity converse](shareability.md) |
| Which complete coding argument attains positive capacity? | [All-record repetition and outer coding](coding.md) |
| What does this separation mean physically? | [Resources, examples and limits](interpretation.md) |
| Which ingredients are inherited? | [Related work](../references/RELATED_WORK.md) |
| What do the finite checks establish? | [Verification guide](../verification/README.md) |

The proof route is model → uniform Haar estimate → finite-setting lower/upper bounds → shareability converse and all-record coding → threshold comparison. Shareability can also be read independently: for a general finite POVM it gives an exact k-receiver broadcast criterion in terms of the established measurement noise content.
