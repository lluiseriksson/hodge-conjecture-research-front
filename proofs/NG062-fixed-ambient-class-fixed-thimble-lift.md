---
brick_id: NG062
status: NO-GO
base_field: C in the geometric application; Q in the obstruction model
variety: a B058 detector transported around a punctured collision parameter
smoothness: generic fibers smooth; endpoint may be singular
projectivity: ambient and hyperplane families projective
dimension: ambient 2n and hyperplane fibers 2n-1
codimension: middle codimension n
coefficient_field: Q
cohomology_theory: thimble quotient homology, primitive ambient homology, local-system monodromy, and B022 kernels
hodge_type: the ambient class is type (0,0) after Q(n); its lift need not be fixed or Hodge
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B055, B085, G049
claim: Because the B058 ambient primitive class is constant around the collision parameter, every thimble or nearby lift representing it is fixed by collision monodromy.
falsifier: a nontrivial kernel shear that fixes the quotient class while moving its lift
---

# NG062 — A fixed ambient class need not have a fixed thimble lift

**Status:** NO-GO

Naturality gives a monodromy-equivariant quotient from thimble data to the
constant primitive ambient group. Hence the monodromy defect of a lift maps
to zero. It may nevertheless be a nonzero element of the equator-extension
or base-locus kernel.

Abstractly, take $A=\mathbf Q^2$, $J=\mathbf Q(0,1)$,
$V=\mathbf Q$, and $q(x,y)=x$. The shear

\[
 M(x,y)=(x,x+y)
\]

acts trivially on $V$, but moves every vector $(1,y)$ above $1$. The ambient
class is fixed while no lift is fixed; B085's cokernel obstruction is
nonzero.

The re-entry condition is G050: compute the actual kernel-valued defect and
show its class in $\operatorname{coker}(M_J-I)$ vanishes.
