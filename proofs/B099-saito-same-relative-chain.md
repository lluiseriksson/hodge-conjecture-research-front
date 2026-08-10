---
brick_id: B099
status: PROVED
base_field: C with rational homology and Hodge structures
variety: a one-parameter projective degeneration of hyperplane sections of a smooth projective complex 2n-fold, with isolated singular special fiber; the clean nodal case is included
smoothness: ambient X and nearby fiber Y_c smooth; special fiber Y_0 has isolated singularities and admits Saito's good retraction
projectivity: X and the degeneration projective
dimension: ambient 2n; hyperplane fibers 2n-1
codimension: middle codimension n; singular locus finite
coefficient_field: Q
cohomology_theory: relative singular homology, good retraction, vanishing-cycle relations, primitive Lefschetz decomposition, B022 quotients, and Saito ambient classes
hodge_type: relation and ambient class rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence in the terminal application
scope: relative and fiberwise
dependencies: B010, B022, B057-B058, B098, S022 Section 2.5
claim: In Saito's isolated-singularity good-retraction model, if the local relation beta is the boundary of the same nearby relative homology class represented by the B057 detector chain and the good-retraction homotopy is taken in the total family over X, then Saito's primitive ambient class gamma_beta equals that detector's B022 ambient image c.
falsifier: a good-retraction model in which the same relative class gives different primitive ambient images in Saito's construction and the B022/B057 tube construction
---

# B099 — The same relative chain gives the same ambient class

**Status:** PROVED

Use Saito's notation from S022 §2.5. A good retraction
$\rho:Y_c\to Y_0$ identifies the relevant relative groups, and a local
relation $\beta$ is represented by a relative cycle

\[
 \gamma'\in H_{2n}(Y_c,Z_c;\mathbf Q(n)),
 \qquad \partial\gamma'=\beta.
\]

Saito defines $\gamma_\beta$ as the primitive part of the image in
$H_{2n}(X,\mathbf Q(n))$ of the retracted relative class
$\rho_*\gamma'\in H_{2n}(Y_0,\mathbf Q(n))$.

Assume the actual collision comparison identifies $\gamma'$ with the same
relative homology class represented by B057's extension
$t=\tau_g(\alpha)$, compatibly with the B022 equator and base-locus
quotients. Choose the good-retraction homotopy in the total hyperplane family;
after projection to the fixed ambient $X$, the nearby inclusion and the
retracted special inclusion are homotopic on this relative class. Therefore

\[
 \gamma_\beta=q_P(t).
\]

B098 gives $q_P(t)=c$, so

\[
 \gamma_\beta=c,
 \qquad
 \langle\zeta,\gamma_\beta\rangle
 =\langle\zeta,c\rangle\ne0.
\]

## Boundary

The theorem is a same-chain compatibility statement. B083 liftability alone
does not identify its special relation coordinate with the boundary of this
particular relative cycle. NG075/G063 isolate that chain-level obligation.
