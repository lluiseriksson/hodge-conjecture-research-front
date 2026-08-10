---
brick_id: B062
status: PROVED
base_field: C
variety: a smooth complex analytic manifold Y with a holomorphic map to a polydisk and its graph in the product
smoothness: Y and its graph are smooth; the original map may have critical points
projectivity: not required; a projective family may be analytified
dimension: arbitrary finite dimension
codimension: the graph has codimension equal to the dimension of the polydisk
coefficient_field: any constructible-sheaf coefficient field; the cotangent calculation is complex analytic
cohomology_theory: constructible sheaves and singular support
hodge_type: none asserted
cycle_class_map: none
cycle_equivalence: none
scope: relative
dependencies: Nadler Remark 4.1.3 in S041 and an elementary conormal calculation
claim: The graph conormal is non-characteristic for the ambient projection at a point if and only if the original family map is a submersion there.
falsifier: a critical point of the original map at which every nonzero base covector avoids the graph conormal
---

# B062 — The graph trick retains the characteristic obstruction

**Status:** PROVED  
**Gate:** G033  
**Primary source:** S041 (Nadler, Remark 4.1.3), plus the differential calculation below

## Mathematical type record

- **Base field:** \(\mathbf C\).
- **Variety/class:** a smooth complex analytic manifold \(Y\) with a holomorphic map \(g:Y\to D^n\), and its graph \(\Gamma_g\subset Y\times D^n\).
- **Smoothness/projectivity:** \(Y\) is smooth; projectivity is not required. A projective family may be used after analytification.
- **Dimension:** arbitrary finite dimension.
- **Codimension:** \(\Gamma_g\) has codimension \(n\) in \(Y\times D^n\).
- **Coefficient field:** any field for which the constant constructible complex is defined; the microlocal calculation is over \(\mathbf C\).
- **Cohomology theory:** constructible sheaves and their singular support.
- **Hodge type:** none asserted.
- **Cycle class map:** none.
- **Equivalence relation on cycles:** none.
- **Scope:** relative, local near a point of the graph.

## Claim

Let \(\pi:Y\times D^n\to D^n\) be projection. Although \(\pi\) is a submersion, the conormal bundle \(T^*_{\Gamma_g}(Y\times D^n)\) is \(\pi\)-non-characteristic at \((y,g(y))\) if and only if \(dg_y:T_yY\to T_{g(y)}D^n\) is surjective. Consequently, graph embedding does not make Nadler's non-characteristic hypothesis automatic at a topology-changing critical collision.

## Proof

At \((y,g(y))\), the tangent space to the graph is
\[
T\Gamma_g=\{(v,dg_yv):v\in T_yY\}.
\]
A covector \((\xi,\eta)\in T_y^*Y\oplus T_{g(y)}^*D^n\) is conormal to the graph exactly when
\[
\xi(v)+\eta(dg_yv)=0\quad\text{for every }v,
\]
or \(\xi=-dg_y^*\eta\). Covectors pulled back from the base by \(\pi\) have the form \((0,\eta)\). Therefore a nonzero base covector lies in the graph conormal exactly when
\[
dg_y^*\eta=0
\]
for some \(\eta\ne0\), which is equivalent to failure of surjectivity of \(dg_y\). This is precisely the conormal special case of Nadler's non-characteristic criterion.

## Consequence

Replacing a singular map by a smooth ambient projection plus graph-supported coefficients changes the presentation, not the obstruction. At a critical collision one must use a more refined singular-support decomposition, a Thom-type argument, a without-slopes theorem, or another comparison mechanism; the ambient submersion alone is insufficient.

## Non-claims

- Singular support may contain more strata than the smooth graph conormal; this brick does not analyze them.
- Failure of this sufficient hypothesis does not prove that nearby cycles fail to commute in the particular family.
- No Hodge class or algebraic cycle is constructed.
