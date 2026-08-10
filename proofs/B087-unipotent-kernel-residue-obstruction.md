---
brick_id: B087
status: PROVED
base_field: C in the semistable application; Q for the nilpotent linear algebra
variety: the punctured-curve restriction of a semistable proper collision model after finite base change
smoothness: generic fibers smooth and semistable source regular; special fiber may be SNC
projectivity: proper/projective collision model
dimension: arbitrary; ambient dimension 2n and hyperplane-fiber dimension 2n-1 in the Hodge application
codimension: middle codimension n; special fiber has parameter codimension one
coefficient_field: Q
cohomology_theory: unipotent nearby cycles, monodromy logarithm, rational local systems, cyclic-group cohomology, and B022 quotient homology
hodge_type: monodromy logarithm is a morphism of the relevant limit Hodge structures up to the standard Tate twist; no type-compatible lift is asserted
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence in the downstream application
scope: relative and fiberwise
dependencies: B063, B071-B072, B076, B085-B086
claim: For unipotent collision monodromy M=exp(N) in B085's exact sequence, an invariant adjusted lift of a constant quotient class exists exactly when the residue class [N t] vanishes in coker(N_J); equivalently coker(M_J-I) and coker(N_J) encode the same obstruction.
falsifier: a nilpotent N for which exp(N)-I and N have different images, or vanishing of [Nt] without any N-invariant adjusted lift
---

# B087 — The residual obstruction is the nilpotent residue class

**Status:** PROVED

In B085's exact sequence, suppose collision monodromy is unipotent:

\[
 M=\exp N,
\]

with $N$ nilpotent and preserving $J$. Since

\[
 \exp N-I=N\,u(N),
 \qquad
 u(z)=\frac{e^z-1}{z}=1+\frac z{2!}+\cdots,
\]

and $u(N)$ is invertible, one has

\[
 \operatorname{im}(M_J-I)=\operatorname{im}N_J.
\]

Also $Mv=v$ is equivalent to $Nv=0$. For a lift $t$ of a constant quotient
class, equivariance gives $Nt\in J$. Replacing $t$ by $t+k$, $k\in J$,
makes it invariant exactly when

\[
 N(t+k)=Nt+N_Jk=0.
\]

Hence the exact obstruction is

\[
 [Nt]\in\operatorname{coker}(N_J:J\to J).
\]

This is the logarithmic form of B085's cyclic monodromy cocycle. It is
strictly narrower than computing the full braid matrix.

## Boundary

B087 does not compute $N$, $J$, or the specified B057 vector. G051 must do
so for the semistable collision model and exhibit $k$ with
$Nt+N_Jk=0$. Only then does B084 give the special-fiber lift.
