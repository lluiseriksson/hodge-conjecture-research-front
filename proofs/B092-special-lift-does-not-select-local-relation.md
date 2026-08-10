---
brick_id: B092
status: PROVED
base_field: C modeled by rational Hodge structures
variety: abstract rational nearby/special-stalk data modeling a proper one-parameter collision; no special variety is asserted
smoothness: not applicable to the strict linear countermodel; intended geometric input has smooth generic fiber
projectivity: intended application is projective; projectivity contributes the lift surjectivity but not the missing projection
dimension: arbitrary; ambient 2n in the Hodge application
codimension: middle codimension n in the application
coefficient_field: Q
cohomology_theory: rational mixed Hodge structures, nearby and vanishing-cycle exactness, special-stalk lifts, and a prospective local-relation quotient
hodge_type: every vector space in the countermodel is pure type (0,0)
cycle_class_map: not used; downstream map is CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence in the downstream application
scope: relative
dependencies: B009, B083-B084, B090-B091
claim: Vanishing of the canonical nearby-cycle obstruction and existence of a rational type-(0,0) special lift do not formally determine, or force nonvanishing of, a component in the target local relation space.
falsifier: a formal implication from the B083 exact segment and type-(0,0) structures alone forcing every nonzero nearby class to have a nonzero local-relation component
---

# B092 — A special lift does not select the local relation component

**Status:** PROVED

Consider pure rational Hodge structures of type $(0,0)$

\[
 S=P=R=\mathbf Q,
 \qquad \Phi=0.
\]

Let the B083 exact segment be

\[
 S\xrightarrow{\mathrm{id}}P\xrightarrow{0}\Phi.
\]

The nearby vector $t_\psi=1$ has zero canonical obstruction and the unique
special lift $\beta=1$. Let $R$ model the independently computed B009 local
relation space. Both choices

\[
 \rho_0:S\to R,\quad \rho_0=0,
 \qquad\text{and}\qquad
 \rho_1:S\to R,\quad \rho_1=\mathrm{id}
\]

are rational morphisms of pure type $(0,0)$ and leave the entire nearby/
vanishing-cycle exact segment unchanged. Yet
$\rho_0(\beta)=0$ and $\rho_1(\beta)=1$.

Therefore B083 exactness, B084 invariant-cycle surjectivity, and Hodge type
alone do not define the map from a special lift to the local relation channel
and cannot force its value to be nonzero. Geometry of the actual collision
must construct and compute that map.

## Boundary

This countermodel does not say the geometric map is arbitrary once a family
is fixed. It says the currently audited formal inputs do not supply it. G056
asks for the missing geometric edge map and its detector coordinate.
