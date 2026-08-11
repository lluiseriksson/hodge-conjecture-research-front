---
brick_id: B127
status: PROVED
base_field: C with rational coefficients
variety: arbitrary polarized smooth projective complex varieties, reduced to an arbitrary smooth projective complex 2n-fold X with a specified primitive rational Hodge class zeta
smoothness: X smooth; optional cleanup target Li-clean multipart nodal
projectivity: X and all universal hyperplane incidence families projective
dimension: arbitrary globally; dim_C X=2n in the middle-degree reduction
codimension: arbitrary globally; middle codimension n after reduction; local support codimension at least two
coefficient_field: Q
cohomology_theory: singular and intersection cohomology, admissible normal-function singularities, local restriction support, and Saito nodal relations
hodge_type: primitive rational type (0,0) after Q(n); cleanup relation type (0,0)
cycle_class_map: CH^p(Y)_Q -> H^(2p)(Y,Q(p)), reduced to CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B001, B007, B010, B012, B125, G008, G031, G084-G085, S009 Theorem 1.3 and Theorems 6.5-6.6
claim: Universal nonemptiness of the class-specific local restriction support is exactly terminal-equivalent to the standard rational Hodge Conjecture; G084 splits into this terminal gate G008 plus the independent conditional cleanup G085, so the clean-incidence requirement is sufficient but not a smaller terminal reduction.
falsifier: a mismatch between BFNP's universal rational singularity criterion and G008, or a G084 witness without nonempty support
---

# B127 — Clean incidence splits into terminal support and cleanup

**Status:** PROVED

For each primitive rational Hodge class \(0\ne\zeta\), G008 asks for some
high power with

\[
 \Sigma_{\zeta,m}\ne\varnothing.
\]

B007, importing BFNP Theorem 1.3 and Theorems 6.5–6.6 with the rational
coefficient audit, proves that the universal statement over all
\((X,\zeta)\) is equivalent to the standard rational Hodge Conjecture.
B012 identifies \(\Sigma_{\zeta,m}\) with the local restriction/singularity
support used in that theorem. Thus

\[
 \boxed{\mathrm{HC}_{\mathbf Q}\Longleftrightarrow G008.}
\]

G084 asks for the stronger incidence

\[
 \Sigma_{\zeta,m}\cap C_m^{\mathrm{clean}}\ne\varnothing.
\]

It therefore contains two logically separate obligations:

1. **terminal support:** \(\Sigma_{\zeta,m}\ne\varnothing\), namely G008;
2. **conditional cleanup:** once some support exists, make support meet a
   Li-clean multipart nodal locus, namely G085.

Hence

\[
 G008+G085\Longrightarrow G084\Longrightarrow G008
 \Longleftrightarrow\mathrm{HC}_{\mathbf Q}.
\]

B125 then propagates G084 to G031 by automatically supplying the detecting
nodal relation.

## Strictness guard

The implication from nonempty support to clean intersection is not formal.
A nonempty subset can be disjoint from a prescribed clean locus, and
B126/NG101 give the geometric local warning that an $A_2$ support germ has no
multipart nodal fiber in its versal slice. No audited theorem proves G085.

Therefore G084 remains a useful stronger sufficient target, but it cannot be
called the smallest active terminal gate. That gate is G008.

## Scope guard

B127 is a quantifier and dependency audit. It proves neither G008 nor G085,
constructs no support point or algebraic cycle, and contributes 0% genuine
general-case progress.
