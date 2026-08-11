---
brick_id: B251
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=8, primitive ruling difference zeta=a-b, standard A=O_Q(1), and H=O_Q(2)
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: the standard quadratic embedding, residual orthogonal quadrics, tangent quotient spaces, self-adjoint annihilators, rank-one maps, and projective-four-space contact bounds are projective
dimension: dim X=d=2n>=8; no standard candidate exists at h_Z(1)=5d-2, so the layers s=8d-6 and s=8d-5 are excluded
codimension: the primitive codimension-n ruling difference supplies a valid universal input; B249 excludes every nonstandard polarization at this rank
coefficient_field: Q for zeta and C for tangent jets, symmetric tensors, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B231, B235-B237, B245-B250, S081
claim: On (Q^d,a-b), d even and at least eight, the standard polarization cannot realize h_Z(1)=5d-2 with every marked tangent osculator absorbed. Hence G174 and its adjacent odd layer are NO-GO. The next balanced signature is s=8d-4, delta_1=4d-2, N=10d-2, and h_Z(1)=5d-1=N/2.
falsifier: a residual-Q^(d-2) rank 3(d-2)+2 span surviving B237, an unclassified mixed branch, failure of the K-membership rank dichotomy, a common eigenvector outside J-perp, a final tangent contribution below d-4, or a different next balanced signature
---

# B251 — One dimension beyond slope-eight equality is impossible

Assume the standard polarization and

\[
 \dim S=h_Z(1)=5d-2. \tag{1}
\]

Choose a nonorthogonal marked pair \(v,w\) and put
\(U=\langle v,w\rangle^\perp\).

## The residual branch recurses to B237

If every residual marked point lies in \(U\), then modulo
\(T_v\oplus T_w\) the available rank is

\[
 (5d-2)-(2d+2)=3d-4. \tag{2}
\]

For \(D=d-2\), this is \(3D+2\), exactly the standard rank excluded by
B237 on the smaller quadric \(Q(U)\); B235-B236 exclude all smaller
ranks. Thus this branch is impossible.

## A third point meets the hyperbolic plane

Choose \(r\notin U\), and put

\[
 S_0=T_v+T_w+T_r,\qquad
 R=\langle v,w,r\rangle,\qquad
 W=R^\perp. \tag{3}
\]

B237 gives \(\dim S_0=3d+2\). Choose a marked \(t\notin R\).

### The case \(t\notin W\)

Here \(T_t\) contributes \(d-1\), so

\[
 S_1=S_0+T_t,\qquad \dim S_1=4d+1. \tag{4}
\]

Its annihilator is \(\operatorname{Sym}^2K\), where

\[
 K=W\cap t^\perp,\qquad \dim K=d-2. \tag{5}
\]

Choose a marked \(u\notin K^\perp\). Contraction of
\(\operatorname{Sym}^2K\) at \(u\), modulo \(\mathbf Cu\), has rank
\(d-3\) when \(u\in K\) and \(d-2\) otherwise. Only \(d-3\) dimensions
remain in (1), so tangent absorption forces

\[
 u\in K. \tag{6}
\]

Put \(J=K\cap u^\perp\). Then \(\dim J=d-3\), and every rank-one map
\(E_z(x)=B(z,x)z\), \(z\in J\), remains in the annihilator after
adding \(T_u\). Since \(T_u\) fills \(S\), all marked points lie in
\(\mathbf P(J^\perp)\simeq\mathbf P^4\), of quadratic point rank at
most fifteen. This contradicts (1).

### The case \(t\in W\)

Now \(T_t\) contributes \(d-2\), giving

\[
 S_1=S_0+T_t,\qquad \dim S_1=4d, \tag{7}
\]

with annihilator

\[
 L=\{A\in\operatorname{Sym}^2W:At\in\mathbf Ct\}. \tag{8}
\]

Its contact locus is \(R\cup\mathbf Ct\). Choose a marked
\(u\) outside it and retain \(K=t^\perp\cap W\).

If \(u\in K^\perp\), B245 gives one new dimension and leaves
\(\operatorname{Sym}^2K\) as annihilator. Choose a marked
\(x\notin K^\perp\). Only \(d-3\) dimensions remain. The same
contraction dichotomy forces \(x\in K\), after which
\(J=K\cap x^\perp\) has dimension \(d-3\) and its rank-one maps confine
all contact to \(\mathbf P(J^\perp)\). This is again impossible.

It remains to suppose

\[
 u\notin K^\perp. \tag{9}
\]

If \(u\notin K\), contraction of
\(\operatorname{Sym}^2K\subset L\) contributes \(d-2\) dimensions and
fills \(S\). For \(J=K\cap u^\perp\), all \(E_z\), \(z\in J\), remain
in the annihilator, so the same projective-four-space contradiction
applies.

Finally suppose \(u\in K\). The subspace
\(\operatorname{Sym}^2K\) contributes \(d-3\) dimensions. Again put
\(J=K\cap u^\perp\), \(\dim J=d-3\). The full tangent \(T_u\) can
contribute either \(d-3\) or \(d-2\) dimensions.

If it contributes \(d-2\), it fills \(S\), and the surviving \(E_z\)
give the projective-four-space contradiction. If it contributes only
\(d-3\), then

\[
 \dim(S_1+T_u)=5d-3, \tag{10}
\]

leaving one dimension. Not all marked points lie in \(J^\perp\),
because their point rank is \(5d-2>15\). Choose a marked
\(x\notin J^\perp\). The linear span of the maps \(E_z\), \(z\in J\),
is \(\operatorname{Sym}^2J\); its contraction at \(x\), modulo
\(\mathbf Cx\), has rank at least

\[
 \dim J-1=d-4>1. \tag{11}
\]

Thus \(T_x\) cannot fit in the final one-dimensional quotient.

Every standard branch is impossible at (1). The layers \(s=8d-6\)
and \(s=8d-5\) share that maximal integral rank. The next balanced
signature is

\[
 s=8d-4,\qquad
 \delta_1=4d-2,\qquad
 N=10d-2,\qquad
 h_Z(1)=5d-1=N/2. \tag{12}
\]

B251 is a necessary special-input obstruction. It constructs no
configuration, ODP package, rational detector, specified pairing,
algebraic cycle, proof, or disproof of HC.
