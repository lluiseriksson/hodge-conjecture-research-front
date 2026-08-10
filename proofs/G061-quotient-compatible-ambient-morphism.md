---
brick_id: G061
status: EXPLORATORY
base_field: C with all coefficient objects and maps over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, a prescribed primitive rational Hodge class, its B058 detector c, and the actual G055 projective collision
smoothness: X and generic hyperplane fibers smooth; target clean nodal; semistable source regular where required
projectivity: plane-net family, collision, proper pushdown, and map to X projective
dimension: ambient 2n; hyperplane fibers 2n-1; plane base 2; collision base 1
codimension: middle codimension n; target nodal stratum of positive codimension
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, proper pushforward, nearby cycles, relative thimble homology, perverse filtration, B022 quotients, and primitive ambient homology
hodge_type: morphism and detector restricted to rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009-B010, B022, B058, B081-B083, B093-B098, G047-G060, NG069-NG074
claim: Construct rational type-(0,0) special and nearby maps q_S and q_P to the constant primitive ambient homology of X, prove q_S=q_P composed with the special-to-nearby map after both B022 quotients, and verify q_P(t_psi)=c.
falsifier: inability to realize t_psi in the coefficient object, failure of either B022 kernel to descend, noncommutativity of the square, or q_P(t_psi) different from c
---

# G061 — Build the quotient-compatible ambient morphism

**Status:** EXPLORATORY

For the actual collision, construct maps on rational type-$(0,0)$ stalks

\[
 \begin{array}{ccc}
 S & \xrightarrow{u} & P\\
 \downarrow q_S && \downarrow q_P\\
 PH_{2n}(X,\mathbf Q(n)) & = & PH_{2n}(X,\mathbf Q(n))
 \end{array}
\]

such that:

1. the B057 nearby class $t_\psi$ is in the domain of $q_P$;
2. the equator-extension image maps to zero at the first B022 quotient;
3. the base-locus kernel maps to zero at the second B022 quotient;
4. the square commutes as a morphism of rational Hodge structures; and
5. $q_P(t_\psi)=c$, B058's selected tube class.

B098 closes steps 2, 3, and 5 on the nearby side once step 1 is realized.
The residual G062 comparison identifies that fixed nearby map with B010's
special Saito map. B097 then gives $F\circ d=0$ and
$\lambda(t_\psi)=\langle\zeta,c\rangle\ne0$, closing G060. The construction
must be made on the actual topology-changing coefficient object; a raw
proper-pushforward slogan is NG073, and automatic special extension is NG074.
