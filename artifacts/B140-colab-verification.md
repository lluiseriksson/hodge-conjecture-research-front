# B140 Colab verification record

Date: 2026-08-11

## Resource incident and local guard

- The original exact-rational SymPy rank experiment exceeded the local
  30-second ceiling in process 26908.
- That exact PID was terminated; a process-tree check found no remaining
  child and no other `verify_B140_quintic_linear_floor.py` process.
- The B140 verifier was not relaunched locally. Its repository version now
  uses a bounded modular row reduction; the expensive exact-rational variant
  is quarantined in `experiments/B140_exact_vandermonde_colab.py`.

## Decisive bounded certificate

- Surface: Colab Pro+.
- Runtime: Python 3, CPU, high RAM.
- Notebook: `B140_bounded_certificate_colab.ipynb`.
- Observed terminal line:

  ```text
  COLAB PASS: B140 bounded modular certificate
  ```

- Scope: for each \(t=5,\ldots,9\), the check verifies the S059 arithmetic
  \(5(t-2)-1=5t-11\), full column rank \(4t+1\) of the rational-normal
  quartic evaluation matrix by reduction modulo 1009, nullity one for
  \(4t+2\) points, and the component/first-jet asymptotic inequalities.
- Why the modular result is exact: rank \(4t+1\) modulo a prime gives a
  nonzero maximal minor over \(\mathbf Z\), hence the same full column rank
  over \(\mathbf Q\).

## Non-decisive exact-Q stress test

- Surface: a separate Colab Pro+ CPU/high-RAM notebook named
  `B140_exact_vandermonde_colab.ipynb`.
- The original SymPy computation was moved there unchanged. It reported
  `t=5: rank=21, nullity=1` and was left isolated from the local machine.
- This slow stress test is supplementary. B140 does not depend on its
  completion: the bounded modular maximal-minor certificate already proves
  the tested rational ranks exactly.

Neither computation proves the geometric bounded-component lemma or the
Hodge Conjecture. They check only finite threshold, rank, and asymptotic
arithmetic used as consistency guards in B140.

## Published cold-clone suite

- Input commit: `ea8e2806d89a31b121db188a8afcd2df11937774`.
- A fresh depth-one clone of `origin/main` was created inside the separate
  Colab Pro+ CPU/high-RAM runtime.
- The cloned SHA matched the input commit exactly.
- All `verify_*.py` scripts passed:

  ```text
  COLD COLAB SUITE PASS: 89/89 in 16.131s
  ## main...origin/main
  ```

- The final status line contains no changed paths. This confirms a clean
  cold clone. The later evidence-record commit changes documentation only;
  its exact SHA receives a second cold-clone run before handoff.

## Latest exact published-suite reproduction

- Input commit:
  `41a49863a9cf8f487c9b0959d4aab559e37a2079`.
- Surface: a new Colab Pro+ Python 3 CPU/high-RAM runtime with 50.99 GiB
  visible memory.
- The notebook cloned the repository with `--no-checkout`, checked out that
  full SHA in detached mode, asserted the SHA, and required exactly 94
  `verification/verify_*.py` scripts.
- Every verifier ran in its own Python process with a 300-second individual
  timeout. The terminal certificate was:

  ```text
  EXACT_RESULT=PASS 94/94 elapsed_seconds=17.761 cold_clone_clean=yes
  ```

- Python was 3.12.13 on x86_64. The final `git status --porcelain` was
  empty. The runtime was disconnected and deleted after capture.
- This is a computational consistency certificate for the published
  parent of B146. It does not prove any analytic brick or the Hodge
  Conjecture; the next commit adds one lightweight verifier and therefore
  requires a new exact 95-script reproduction in the next high-RAM cycle.
