---
brick_id: NG055
status: NO-GO
base_field: C
variety: the B071 semistable log-stack and its global proper pushdown for the root-covered plane-net hyperplane degeneration
smoothness: the semistable stack is regular and has local monomial charts; generic hyperplane fibers are smooth but non-toric in general
projectivity: the family, alterations, modifications, and pushdowns are projective
dimension: arbitrary ambient dimension 2n and odd hyperplane-fiber dimension 2n-1
codimension: arbitrary proper supports in the parameter base; terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, nearby cycles, strict support, and the toric decomposition theorem
hodge_type: the detector target is rational type (0,0) after Q(n); toric Hodge-Tate parity alone does not determine it
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B071-B078, G043, S048
claim: B078's toric support parity by itself forces the B058 nearby specialization to have zero projection to every proper-support summand of B077's global semistable pushdown.
falsifier: failure to identify the global pushdown with a proper toric map carrying the same constant/intersection-complex input and degree normalization
---

# NG055 — Local toric parity does not determine the global tube projection

**Status:** NO-GO

## Proposed shortcut

The B058 detector is tracked in an ordinary degree-one relation channel.
B078 says that proper-support summands for a smooth proper toric map occur
only in even ordinary generic degrees. One might therefore declare every
proper-support component zero and place the detector in full support.

## Failure

B071 makes the relevant morphism semistable/toroidal and locally monomial.
It does not make the projective hyperplane degeneration a single globally
proper toric map. Its global fibers contain the original non-toric
hyperplane geometry, and their cohomology supplies coefficient systems and
cohomological shifts not present in B078's constant toric model. Étale-local
toric charts describe the boundary normal directions; they do not by
themselves identify the global strict-support decomposition or the class

\[
 \operatorname{sp}(c)
 \in f_*\mathbf Q_{\mathcal Y}[\dim\mathcal Y].
\]

There is also no proved comparison placing the B057 extension chain in the
same ordinary-degree normalization used in B078 after nearby cycles,
finite descent, and proper pushdown. Thus the parity theorem cannot be
applied directly to the specified class.

## Re-entry condition

Prove G044: factor the exact B071 pushdown, retain the non-toric coefficient
Hodge modules, and establish a coefficient-sensitive toroidal parity or
amplitude bound in the precise perverse degree containing the B057-B058
specialization. Only then can parity remove exceptional supports in G043.
