# Reproducibility and verification scope

Run from the repository root with Python 3.10 or newer:

```bash
python -m pip install -r requirements.txt
python verification/check_science.py --output build/science-checks.json
python verification/check_docs.py
```

The scientific suite independently checks conditional-reference determinants against direct positive matrices, the binary-entropy bound used in the Haar proof, coarse-mesh effect comparisons, explicit k-receiver Choi extensions and all their required marginals, uniform Haar lower bounds on a finite input/noise grid, and the sufficient finite-block inequality in log form. The seed and tested grids are fixed in the script. Tolerances are numerical, with double precision and roundoff allowed at zero eigenvalues.

The documentation check verifies local links and anchors, mathematical delimiter/fence structure, scientific file ownership and the public-source scope. It does not inspect hosted GitHub rendering. Hosted mathematical and visual review is a separate final check.

These calculations support the particular finite cases they execute. The all-input, all-menu, all-block and asymptotic conclusions rely on the written proofs. A sampled minimum of the Haar entropy ratio does not prove its exact value; the conjectured equality with binary entropy is not used. A passing numerical run does not certify literature priority, practical communication rates, decoder efficiency or hardware feasibility.

The core proofs and their dependencies are mapped in [the scientific entrypoint](../science/README.md). The [coding account](../science/coding.md) explains why the capacity implication uses a finite inner block followed by asymptotic outer coding.
