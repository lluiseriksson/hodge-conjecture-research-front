---
brick_id: B174
status: PROVED
base_field: C
variety: an arbitrary analytic tracked critical-value germ together with any global-residue identity split into tracked and auxiliary terms
smoothness: the parameter germ is smooth; no additional geometric smoothness is needed for the local-algebra statement
projectivity: not used; the theorem audits the coefficient algebra after any valid projective or affine residue identity has been obtained
dimension: N tracked functions tau_i of central differential rank R<N; arbitrary number of auxiliary critical points
codimension: lifting N-R central differential relations is equivalent to surjectivity of syzygy evaluation at the origin
coefficient_field: C
cohomology_theory: analytic local algebra, syzygy modules, and Grothendieck-residue identities
hodge_type: none asserted
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used; no cycle or detector is constructed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B156, B172-B173, G100
claim: For every identity c dot tau + rho=0, rho belongs to I_tau automatically. Its coefficient-representation fiber is an affine torsor under Syz(tau), and translation by c is an affine bijection onto Syz(tau). Hence constructing adjusted representations that lift all central relations is exactly G100.
falsifier: a coefficient representation of rho whose adjusted row is not a syzygy, a syzygy not obtained from a representation, or an auxiliary ideal-membership certificate that yields a new central row without an existing syzygy
---

# B174 — Auxiliary residue representations are the syzygy torsor

Let

\[
 \tau=(\tau_1,\ldots,\tau_N)\in\mathcal O^N
\]

be any analytic germ, and suppose a residue calculation gives

\[
 c\cdot\tau+\rho=0,\qquad c=(c_1,\ldots,c_N)\in\mathcal O^N. \tag{1}
\]

Equation (1) already proves

\[
 \rho=-c\cdot\tau\in I_\tau. \tag{2}
\]

Define the coefficient-representation fiber

\[
 \operatorname{Rep}_\tau(\rho)
 =
 \{b\in\mathcal O^N:b\cdot\tau=\rho\}
\]

and the analytic syzygy module

\[
 \operatorname{Syz}(\tau)
 =
 \{s\in\mathcal O^N:s\cdot\tau=0\}.
\]

The vector \(-c\) is the canonical point of
\(\operatorname{Rep}_\tau(\rho)\). For every representation \(b\),

\[
 (b+c)\cdot\tau=\rho+c\cdot\tau=0.
\]

Conversely, every \(s\in\operatorname{Syz}(\tau)\) gives the
representation \(b=s-c\). Therefore

\[
 \boxed{
 \operatorname{Rep}_\tau(\rho)
 \xrightarrow[\sim]{\ b\mapsto b+c\ }
 \operatorname{Syz}(\tau)
 } \tag{3}
\]

is an affine bijection, with inverse \(s\mapsto s-c\). In particular:

1. the canonical representation \(b=-c\) gives the zero syzygy;
2. a different representation contains exactly the information of the
   corresponding pre-existing syzygy;
3. representations whose adjusted central rows span
   \(\ker(d\tau_0)^*\) exist exactly when syzygy evaluation already
   surjects onto that relation space.

By B156, item 3 is equivalent to \(H_\tau=0\), hence to G100's analytic
factorization. Auxiliary ideal membership cannot be a smaller obstruction.

## Explicit hidden-generator guard

Take

\[
 \tau=(x,x+y^2).
\]

Its central differential relation is \((1,-1)\), but every analytic
syzygy is a multiple of

\[
 (x+y^2,-x),
\]

because \(x,x+y^2\) is a regular sequence and its first syzygy module is
the Koszul module. Hence every syzygy vanishes at the origin. For any
chosen row \(c\), define
\(\rho=-c\cdot\tau\). Then \(\rho\in I_\tau\) and \(-c\) is a coefficient
representation, but every adjusted representation row still vanishes at
the origin. The missing central relation is not created by the auxiliary
identity.

## Scope guard

B174 does not invalidate the exact-selector syzygies of B172 or the
duality of B173. It proves only that allowing a nonzero auxiliary term and
then invoking its membership in \(I_\tau\) adds no information. A useful
residue theorem would have to construct a nonzero syzygy by additional
geometry, which is precisely the unresolved gate.
