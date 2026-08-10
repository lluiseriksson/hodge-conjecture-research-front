---
brick_id: G047
status: EXPLORATORY
base_field: C with the comparison class and all Hodge-module maps over Q
variety: an arbitrary polarized smooth projective complex 2n-fold, a B058 plane-net detector, and a topology-changing algebraic collision family ending at one singular hyperplane member
smoothness: X and generic detector fibers are smooth; the endpoint is singular; any semistable replacement is regular as a stack
projectivity: X, the hyperplane families, collision family, and semistable modifications are projective
dimension: ambient 2n, hyperplane fibers 2n-1, plane-net base 2, and collision parameter 1
codimension: middle codimension n; endpoint support has base codimension one or two
coefficient_field: Q
cohomology_theory: singular relative homology, Lefschetz thimbles, rational mixed Hodge modules, nearby cycles, perverse stalks, and the B022 quotient maps
hodge_type: the special boundary class must be rational type (0,0) after Q(n), or at minimum have an ambient image pairing nontrivially with the prescribed type-(0,0) class
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B057-B059, B063, B071-B082, G032, NG059
claim: For every nonzero primitive rational Hodge class and a B058 detector pair, there is an algebraic collision datum carrying the B057 extension chain to a rational special boundary class beta in H^(-1)(i_p^*K), compatibly with the two B022 quotients, whose ambient image remains nonorthogonal to the prescribed Hodge class.
falsifier: a detector for which every algebraic collision either has no relative-chain extension, produces zero boundary, lands in an equator or base-locus kernel, loses rational type, or becomes orthogonal to the prescribed class
---

# G047 — Chain-to-stalk collision lift

**Status:** EXPLORATORY  
**Parent gates:** G032 / G046

Fix the B058 detector pair $(g,\alpha)$ and let $t=\tau_g(\alpha)$ be its
B057 boundary-zero extension chain. Construct:

1. a pointed algebraic curve $(T,0)$ and a projective topology-changing
   family of plane-net data over $T$;
2. a relative rational thimble/nearby-cycle class $\widetilde t$ over
   $T\setminus\{0\}$ whose realization is $t$;
3. a semistable comparison for which the canonical boundary map gives

   \[
   \beta=\partial_0(\widetilde t)\in H^{-1}(i_p^*K);
   \]

4. compatibility of $\beta$ with the equator-extension and base-locus
   quotients in B022; and
5. nonzero prescribed pairing

   \[
   \langle\zeta,\Phi_p(\beta)\rangle\ne0.
   \]

Exact recovery $\Phi_p(\beta)=c$ is allowed but is not required, by B059.
The collision datum may depend on $(\zeta,g,\alpha)$; G047 does not claim a
canonical map from all ambient homology to all singular stalks.

## Why this precedes G046

Once $\beta$ has been constructed, B081 gives its canonical
$E_\infty^{-1,0}$ and $E_\infty^{0,-1}$ associated grades, and G046 asks
whether the full-support part retains the pairing. Without $\widetilde t$
and $\beta$, the symbol previously written as $\operatorname{sp}(c)$ has no
defined source map. NG059 records that failed shortcut.

## First attack

Start from the ordered chain formula in B057 and build the collision over a
curve in the configuration space of critical values. The comparison must be
performed before passing to homology, so that its boundary is visibly the
limiting vanishing-cycle relation. Any construction that records only the
ambient class $c$ has already forgotten the lift data needed here.
