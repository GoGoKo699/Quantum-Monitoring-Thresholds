# Learning through the monitoring problem

The learning route uses one educational source: John Preskill, [*Quantum Shannon Theory*, arXiv:1604.07450v5, 8 July 2025](https://arxiv.org/abs/1604.07450v5). The project asks how much intact quantum transmission is needed when the other physical inputs leave only noisy classical measurement records.

The [Preskill bridge](PRESKILL_BRIDGE.md) identifies relevant source sections and printed pages, translates notation, and works through two explicit channel points. It distinguishes a positive coherent-information witness, an activation threshold, a capacity bound, and an achievable communication rate.

The [30 milestones](MILESTONES.md) form the detailed route. M01–M12 establish the background needed to read the problem; M13–M30 follow the scientific argument and its resource account. Each milestone has a mathematical target, dependencies, a role in the argument, and source pointers. They are ordered by conceptual dependence rather than by a calendar.

| Route | Purpose |
|---|---|
| [Preskill bridge](PRESKILL_BRIDGE.md) | Connect the selected chapter to this channel, with a notation crosswalk and a complete numerical example |
| [M01–M30](MILESTONES.md) | Follow the background and the proof through explicit mathematical targets |
| [Scientific entrypoint](../science/README.md) | Read the authoritative model, statements, and proofs |
| [Model and definitions](../science/model.md) | Fix which systems and records exist, what is inaccessible, and which threshold is being optimized |
| [References and attribution](../references/RELATED_WORK.md) | Separate the inherited channel/coding ingredients from this project's contribution |
| [Verification scope](../verification/README.md) | Reproduce the finite checks and understand their limits |

The central chain is conditional reference entropy → a uniform bound over all input purities → a finite-setting frontier → shareability obstruction and collective coding → comparison of activation thresholds. The shareability theorem can also be read independently.

The source provides the general information-theoretic background. The local scientific pages contain the channel-specific Haar estimate, finite-menu construction, exact shareability calculation, and complete all-record coding argument. Capacity here is unassisted and asymptotic. A positive rate need not be large, and existence of an outer code does not imply efficient decoding.
