---
brick_id: B080
status: PROVED
base_field: C
variety: the B058 projective plane-net hyperplane family and any semistable proper model used in B071
smoothness: generic hyperplane fibers are smooth; the semistable source stack is regular
projectivity: the hyperplane family and semistable pushdown are projective
dimension: ambient variety 2n, hyperplane fiber 2n-1, parameter base 2, and total space 2n+1
codimension: divisor and point supports have base codimensions 1 and 2; terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: rational derived direct image, perverse normalization, intersection complexes, and strict-support shifts
hodge_type: the detector is rational type (0,0) after Q(n); this brick computes degrees only
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B057-B058, B077-B078, G043-G044
claim: In total normalized degree -1, a codimension-c support can contribute at decomposition shift b=1-c; this includes full support at b=1, the relation/divisor position b=0, and point support at b=-1. B078 parity allows all three.
falsifier: a different total-space dimension, a different perverse shift for R^(2n-1), or a support-stalk normalization not giving b=1-c
---

# B080 — Exact detector/support shift normalization

**Status:** PROVED

Let $h:\mathcal X\to B$ be the plane-net hyperplane family. The base has
dimension $2$, the smooth fibers have dimension

\[
 m=2n-1,
\]

and the total space has dimension

\[
 D=m+2=2n+1.
\]

On the smooth locus, put $L=R^m h_*\mathbf Q$. In the normalized direct
image $Rh_*\mathbf Q_{\mathcal X}[D]$, the middle local system occurs as

\[
 L[D-m]=L[2],
\]

which is perverse on the smooth base. If
$P=j_{!*}L[2]$, then the local relation group written elsewhere as
$H^1(j_{!*}L)_p$ is

\[
 H^{-1}(P_p).
\]

Equivalently it is raw total-direct-image degree

\[
 D-1=2n.
\]

## Which strict-support shifts can contribute?

Let $V\subset B$ have codimension $c$, so
$\dim V=2-c$, and consider a decomposition term

\[
 IC_V[-b].
\]

At a generic point of $V$, $IC_V$ is the constant local system shifted by
$\dim V$, hence the term is nonzero in normalized cohomological degree

\[
 i=b-\dim V.
\]

It meets the detector degree $i=-1$ exactly when

\[
 b=\dim V-1=1-c.
\]

Thus the base-plane possibilities are

\[
 \begin{array}{c|c|c}
 c&V&b\\ \hline
 0&\text{full base}&1\\
 1&\text{divisor}&0\\
 2&\text{point}&-1.
 \end{array}
\]

Substitution into B078's toric parity expression gives

\[
 b+D-\dim V
 =(\dim V-1)+D-\dim V
 =D-1=2n,
\]

which is even. Therefore toric parity allows every support codimension that
can meet the detector degree; it excludes neither divisor nor point support.

## Consequence and boundary

G043 cannot be closed by parity, even after the detector shift is normalized
correctly. B121 records the consequence of the previously omitted $c=0$
row: the full-support $b=1$ term is the constant ambient
$E_\infty^{-2,1}$ grade and must be separated from the relation grade by the
canonical perverse filtration. B080 determines possible degrees, not
multiplicities or selected-class coordinates.
