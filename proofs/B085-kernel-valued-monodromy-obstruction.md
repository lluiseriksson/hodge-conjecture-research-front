---
brick_id: B085
status: PROVED
base_field: C in the geometric application; the obstruction calculation is over Q
variety: a punctured one-parameter collision family whose thimble quotient and primitive ambient homology form local systems
smoothness: generic collision fibers smooth; no assertion on the special fiber
projectivity: the ambient variety and hyperplane family are projective; the linear obstruction uses only the induced local systems
dimension: arbitrary for the local-system lemma; ambient dimension 2n in the Hodge application
codimension: middle codimension n; no new support codimension is asserted
coefficient_field: Q
cohomology_theory: rational local systems, Lefschetz-thimble quotient homology, monodromy, and first cyclic-group cohomology
hodge_type: no Hodge type is inferred; the obstruction occurs before choosing a special Hodge-compatible lift
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence in the downstream Hodge application
scope: relative and fiberwise
dependencies: B022, B055, B084, G049
claim: In a monodromy-equivariant exact sequence 0 -> J -> A -> V -> 0 with V constant, the monodromy defect of any lift of c in V lies in J and defines a lift-independent class in coker(M_J-I); an invariant lift of c exists exactly when this class vanishes.
falsifier: two lifts of the same constant ambient class whose defects give different cokernel classes, or a zero cokernel class with no invariant adjusted lift
---

# B085 — The collision defect is a kernel-valued cohomology class

**Status:** PROVED

Let

\[
 0\longrightarrow J\longrightarrow A
 \xrightarrow{q}V\longrightarrow0
\]

be an exact sequence of rational local systems on a punctured disk, with
$V$ constant. In the B022 application, $A$ can be the raw boundary-zero
thimble group and $J$ the combined preimage of the equator-extension and
base-locus kernels. Equivalently, after the equator quotient one may take
$A=\mathcal T(Y)$ and $J=K$.

Let $M$ be local monodromy and choose $t\in A$ with $q(t)=c\in V$. Since
$V$ is constant and $q$ is monodromy equivariant,

\[
 q(Mt-t)=0.
\]

Thus

\[
 d(t):=Mt-t\in J.
\]

If $t$ is replaced by another lift $t+k$, $k\in J$, then

\[
 d(t+k)=d(t)+(M_J-I)k.
\]

Consequently

\[
 [d(c)]\in\operatorname{coker}(M_J-I:J\to J)
\]

depends only on $c$ and the extension, not on the chosen lift. Moreover,
there is an invariant lift $t+k$ exactly when

\[
 d(t)+(M_J-I)k=0,
\]

equivalently exactly when $[d(c)]=0$. This cokernel is the usual
$H^1(\mathbf Z,J)$ obstruction for the cyclic local monodromy.

## Consequence for G049

Constancy of the B058 ambient class proves only that the defect lies in the
B022 kernel. It does not prove the specified thimble lift is fixed. G050
must compute the kernel action and the class $[d(c)]$. Vanishing produces an
invariant adjusted lift to which B084 applies; nonvanishing is the precise
obstruction to this local-invariant-cycle route.

B086 subsequently kills the finite deck-group part over $\mathbf Q$;
B087/G051 isolate the remaining unipotent residue class.
