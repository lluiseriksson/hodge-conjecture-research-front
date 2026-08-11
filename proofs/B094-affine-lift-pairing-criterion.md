---
brick_id: B094
status: PROVED
base_field: C with rational Hodge structures
variety: the special-stalk data of a projective one-parameter collision for an arbitrary polarized smooth projective complex 2n-fold
smoothness: generic hyperplane fiber smooth; special target clean nodal; the lemma itself is rational linear algebra on the resulting Hodge structures
projectivity: collision projective in the application
dimension: ambient 2n; hyperplane fibers 2n-1; collision base 1
codimension: middle codimension n; target nodal stratum of positive codimension
coefficient_field: Q
cohomology_theory: rational mixed Hodge structures, nearby/special exactness, perverse associated grade, strict support, B022 quotients, and the Saito pairing
hodge_type: all lift and ambiguity vectors are restricted to the rational type-(0,0) subspace after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is constructed
cycle_equivalence: rational equivalence in the terminal application
scope: relative and fiberwise
dependencies: B010, B022, B059, B083, B093, B134
claim: If the rational type-(0,0) lifts of a fixed nearby detector form the affine torsor beta_0+A and F is the scalar obtained by canonical relation-grade landing, both B022 quotients, and pairing with the prescribed Hodge class, then a detecting lift exists exactly when F(beta_0) is nonzero or F(A) is nonzero; ambiguity-independence is equivalent to the strictly stronger condition F(A)=0.
falsifier: an affine rational lift torsor and linear detector functional for which the stated disjunction does not characterize existence of a nonzero value
---

# B094 — Exact affine criterion for a detecting lift

**Status:** PROVED

Assume the type-$(0,0)$ lift set of the specified nearby detector is nonempty.
By B083 it is an affine rational space

\[
 \mathcal L=\beta_0+A,
\]

where $A$ is the type-$(0,0)$ part of the lift-ambiguity image. Once G057's
canonical associated-grade and full-support operations and the required
homological relation input are defined, B134 types the cohomological grade
as a dual relation space. Evaluation gives a rational linear functional

\[
 F:S^{(0,0)}\longrightarrow\mathbf Q.
\]

Its image on the lift torsor is

\[
 F(\mathcal L)=F(\beta_0)+F(A).
\]

Therefore every lift has zero detector pairing exactly when

\[
 F(\beta_0)=0
 \quad\text{and}\quad
 F(A)=0.
\]

Equivalently, at least one detecting lift exists exactly when

\[
 F(\beta_0)\ne0
 \quad\text{or}\quad
 F(A)\ne0.
\]

The value is independent of the chosen lift exactly when $F(A)=0$. Thus
annihilating all ambiguity is sufficient but not necessary: if $F(A)\ne0$,
the ambiguity itself supplies lifts with nonzero pairing.

## Boundary

B094 does not prove that a type-$(0,0)$ lift exists or calculate either term.
G058 is the geometric computation of this exact disjunction.
