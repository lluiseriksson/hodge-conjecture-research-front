---
brick_id: NG059
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex 2n-fold and a plane-net hyperplane degeneration
smoothness: X is smooth; the collision fiber may be singular
projectivity: X and the hyperplane family are projective
dimension: ambient 2n, fibers 2n-1, and base 2
codimension: middle codimension n; collision support has base codimension at least one
coefficient_field: Q
cohomology_theory: primitive singular homology, relative thimble homology, nearby cycles, and perverse stalk cohomology
hodge_type: ambient target type (0,0) after Q(n); no stalk type is inferred
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B057-B059, B081-B082
claim: The B058 ambient homology class c canonically specializes to a class sp(c) in the collision stalk H^(-1)(i_p^*K) without first choosing and proving compatibility of a collision family of thimble chains.
falsifier: the forward-only B022 quotient sequence, nonunique lifts through its kernels, and absence of any constructed collision comparison from the B057 chain
---

# NG059 — An ambient class does not automatically specialize to a stalk

**Status:** NO-GO

The B058 class $c$ lies in primitive ambient homology. The group
$H^{-1}(i_p^*K)$ is a stalk group for a particular singular member of a
particular degeneration. B022 maps a local thimble relation toward ambient
homology through two quotients; it does not provide a reverse specialization
map from ambient homology.

Thus writing

\[
 \operatorname{sp}(c)\in H^{-1}(i_p^*K)
\]

before constructing collision data hides the main geometric obligation.
The ambiguity is not repaired by the decomposition theorem or by B081's
canonical perverse filtration: a filtration can analyze a class only after
the class exists in its filtered group.

The valid replacement is G047. Choose an algebraic collision family and
construct a relative extension-chain class; then apply the nearby/boundary
map belonging to that chosen family and test the resulting class in G046.
