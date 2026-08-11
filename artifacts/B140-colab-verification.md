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
