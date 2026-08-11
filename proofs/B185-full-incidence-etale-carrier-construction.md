---
brick_id: B185
status: PROVED
base_field: C
variety: the full complete-linear-system critical incidence near an ordered collection of distinct ordinary double points on an arbitrary smooth projective complex variety
smoothness: the ambient variety and parameter chart are smooth; every tracked critical point has invertible Hessian; the chosen R critical-value differentials are independent
projectivity: the construction begins with the full projective universal family and uses only algebraic affine charts, line-bundle trivializations, fiber products, localizations, and marked components
dimension: parameter dimension d; N labelled ODPs; critical-value rank R; carrier dimension d-R; finite presentation in M affine variables with equation and numerator degree bounded by E
codimension: the basis-value carrier is smooth of codimension R and its projective degree is bounded by E^M; conormal nonvanishing is visible by order at most E^(M+1)-1
coefficient_field: C for algebraic critical incidences and conormal modules; Q remains required for downstream Hodge detectors
cohomology_theory: relative critical loci, algebraic etale morphisms, fiber products, Jacobian criterion, affine and projective Bezout, Kahler differentials, and ODP vanishing cycles
hodge_type: none asserted; rational type (0,0) and the specified nonzero Saito pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is only downstream; no algebraic cycle or detector is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B157-B184, G113-G117, S015, S065, S072
claim: For any fixed ordered full-incidence ODP configuration and any rank-R basis of its critical-value differentials, the product of the labelled algebraic critical incidences contains a canonical marked smooth algebraic carrier analytically identifying with the basis-node germ. Cleared escape values are regular polynomial numerators on it. From any finite presentation in M variables of degree at most E at least two, Bezout gives carrier degree at most E^M, so B184 yields the explicit conormal certificate order E^(M+1)-1.
falsifier: failure of the labelled product incidence to be etale at an ODP tuple, singularity of the basis-value cut despite differential independence, an escape value not represented regularly after unit clearing, a component degree exceeding E^M, or failure of the analytic carrier to identify with the labelled basis-node germ
---

# B185 — The full incidence supplies the étale carrier

Let \(P\subset |L|\) be an affine parameter chart of dimension \(d\) in
the full complete linear system. Let \(p_1,\ldots,p_N\) be distinct ODPs of
the central member.

Choose an affine algebraic neighborhood \(U_i\) of each \(p_i\), trivialize
\(L\) there, and choose pairwise disjoint small analytic neighborhoods
inside the \(U_i^{an}\). Write \(f_i(t,x_i)\) for the resulting regular
local equation of the universal member. Its relative critical locus is

\[
 C_i=\{d_{U_i}f_i=0\}\subset P\times U_i. \tag{1}
\]

At \(c_i=(0,p_i)\), the derivative of (1) in the \(x_i\)-variables is the
Hessian of the central member. It is invertible because \(p_i\) is an ODP.
The algebraic Jacobian criterion therefore makes

\[
 \rho_i:(C_i,c_i)\longrightarrow(P,0) \tag{2}
\]

étale. The critical value

\[
 v_i=f_i|_{C_i} \tag{3}
\]

is regular on the marked critical incidence.

## Labelled product and basis cut

Form the fiber product

\[
 C=C_1\times_P\cdots\times_P C_N
\]

at \(c=(c_1,\ldots,c_N)\). It is étale over \(P\) at \(c\), and it carries
all \(N\) labels and all regular value functions \(v_i\).

Let \(B\subset\{1,\ldots,N\}\) have size \(R\), with
\(\{dv_b(c):b\in B\}\) independent. Define the marked carrier

\[
 V_B=\text{the germ at }c\text{ of }
 \{v_b=0:b\in B\}\subset C. \tag{4}
\]

Since \(C\) is smooth of dimension \(d\) and the displayed differentials
are independent, \(V_B\) is smooth of dimension \(d-R\).

After analytification and shrinking, the étale map \(C\to P\) is a local
biholomorphism at \(c\). Under that biholomorphism, (4) is exactly B158's
basis-node germ \(F_B\). For every \(i\notin B\),

\[
 v_i|_{V_B}=\epsilon_{B,i}. \tag{5}
\]

Thus the full labelled incidence itself supplies G117's algebraic carrier;
no value resultant, analytic idempotent, or elimination of the labels is
needed.

## Uniform finite-presentation bound

Choose one affine embedding containing the marked component of \(V_B\).
Replace each required localization \(h\ne0\) by a Rabinowitsch equation
\(q_hh-1=0\), and clear only denominators certified nonzero at \(c\).
The result is a finite system in \(M\) affine variables. Let
\(E\ge2\) bound:

1. the degree of every defining polynomial, including the Rabinowitsch
   equations;
2. the degree of every cleared escape numerator \(N_i\).

The marked irreducible component \(\overline V_B\) has

\[
 \deg\overline V_B\le E^M. \tag{6}
\]

Indeed, at the generic point of a component of codimension \(r\le M\),
\(r\) sufficiently general linear combinations of the defining equations
cut that component properly. Successive projective Bézout bounds its degree
by \(E^r\le E^M\). Equivalently, S072 gives a fully mechanical
Gröbner/Hilbert-polynomial audit from the same finite presentation.

B183 identifies the cleared numerator ideal with the escape ideal. Applying
B184 with

\[
 \delta=E^M,\qquad e=E
\]

shows that a nonzero conormal defect is visible by order at most

\[
 D_{\mathrm{car}}-1,\qquad
 D_{\mathrm{car}}:=E^{M+1}. \tag{7}
\]

This invocation assumes \(d-R\ge1\), as in B184. If \(d-R=0\), the smooth
carrier germ is a point, its local ring is \(\mathbf C\), and every escape
value already vanishes at that point; hence \(K_B=0\) directly.

Hence

\[
 j^{D_{\mathrm{car}}-1}\beta_{K_B}=0
 \Longrightarrow H_\tau=0. \tag{8}
\]

## Scope guard

B185 closes only the carrier-existence and finite-degree parts of G117 for
a fixed proposed ordered ODP configuration. It does not construct that
class-directed configuration for an arbitrary Hodge class, prove any jet
in (8) vanishes, or supply rational type and a nonzero Saito pairing.
