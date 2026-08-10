---
brick_id: B029
status: PROVED
base_field: C
variety: X = P^2 x P^2 with a line C = P^1 x {q} and a divisor Y in |O_X(m,m)|
smoothness: X and C are smooth; the conclusion is that Y cannot have only isolated singularities under the stated incidence
projectivity: X, C, and Y are projective
dimension: dim_C X = 4, dim_C Y = 3, and dim_C C = 1
codimension: C has codimension 3 in X; the Hodge application has middle codimension 2
coefficient_field: C for sections, first jets, and evaluation ranks; Q for the later Hodge application
cohomology_theory: coherent sheaves, restriction and conormal first jets; no Hodge-theoretic conclusion is asserted
hodge_type: not applicable to the isolation obstruction; the target G013 relation would have rational type (0,0) after Tate twist
cycle_class_map: CH^2(X)_Q -> H^4(X,Q(2)); no cycle is constructed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B028 and the conormal first-jet calculation below
claim: If a section of O_X(m,m) is singular at more than m distinct points of C, then it vanishes to second order along C and C lies in the singular locus; in particular, the collinear configurations with positive B028 adjoint defect cannot be node schemes of a nodal member.
falsifier: a section of O_X(m,m) singular at more than m distinct points of C but smooth at some point of C
---

# B029 - Collinear adjoint defect destroys isolated nodality

Let

\[
 X=\mathbf P^2\times\mathbf P^2,
 \qquad A=\mathcal O_X(m,m),
 \qquad C=\ell\times\{q\}\simeq\mathbf P^1,
\]

where \(\ell\subset\mathbf P^2\) is a line. Let \(s\in H^0(X,A)\), and
suppose its zero divisor \(Y_s\) is singular at a set
\(\Delta\subset C\) of \(N>m\) distinct points.

## Restriction and first normal derivatives

Because \(A|_C\simeq\mathcal O_{\mathbf P^1}(m)\) and \(s\) vanishes at all
points of \(\Delta\), the inequality \(N>m\) forces

\[
 s|_C=0.
\]

Thus the first normal term of \(s\) is a section of

\[
 (I_C/I_C^2)\otimes A|_C
 \simeq N_{C/X}^{\vee}\otimes A|_C.
\]

The normal bundle splits as

\[
 N_{C/X}\simeq
 N_{\ell/\mathbf P^2}\oplus
 (T_q\mathbf P^2\otimes\mathcal O_C)
 \simeq \mathcal O_C(1)\oplus\mathcal O_C^{\oplus2}.
\]

Consequently

\[
 N_{C/X}^{\vee}\otimes A|_C
 \simeq
 \mathcal O_C(m-1)\oplus\mathcal O_C(m)^{\oplus2}.
\]

At every point of \(\Delta\), singularity of \(Y_s\) says that all first
normal derivatives vanish. A section of any displayed summand that vanishes
at \(N>m\) distinct points is zero. Hence the full first normal term vanishes
identically, so

\[
 s\in H^0(X,I_C^2\otimes A).
\]

Both \(s\) and its differential therefore vanish at every point of \(C\).
Thus

\[
 C\subseteq\operatorname{Sing}(Y_s),
\]

and \(Y_s\) cannot have only isolated ordinary double points.

## Consequence for the B028 line configuration

For the adjoint bundle

\[
 F=K_X\otimes A^2=\mathcal O_X(2m-3,2m-3),
\]

restriction to \(C\) is surjective onto
\(H^0(C,\mathcal O_C(2m-3))\). Distinct points on \(C\) have positive
\(F\)-evaluation defect only when

\[
 N>h^0(C,\mathcal O_C(2m-3))=2m-2.
\]

Such an \(N\) is certainly greater than \(m\). Therefore every collinear
configuration in this model that enters the positive-adjoint-defect half of
the G013 window forces \(C\) into the singular locus. It cannot be realized
as the node set of a nodal member.

## Scope guard

The obstruction is specific to this carrier and linear system. It does not
exclude distributed point configurations, zero-dimensional
Cayley-Bacharach-type configurations, or other incidence geometries satisfying
G013. It proves only that adjoint dependence obtained by overloading this
low-degree curve is incompatible with isolated nodality.
