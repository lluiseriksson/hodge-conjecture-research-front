---
brick_id: B203
status: PROVED
base_field: C
variety: a smooth projective complex variety with very ample H, a nonempty reduced point scheme Z, and the degree-m homogeneous point ideal
smoothness: X and Z are smooth; no divisor or incidence smoothness is inferred by the generator filtration
projectivity: X, L=H^m, the ideal powers I_Z^2 and I_Z^3, and the homogeneous section ideal are projective coherent data
dimension: arbitrary dim X=d; the new double-generator space D_m=H0(I_Z^2 L)/P_m splits in dimension into a triple-hidden term and a quadratic-profile term
codimension: decomposable lower products must be quotiented both before and after taking the quadratic profile
coefficient_field: C for sections, ideal powers, profiles, and quotient spaces; Q remains required separately for the detector
cohomology_theory: coherent ideal-power sequences, graded section ideals, connecting homomorphisms, and finite-dimensional exact sequences
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B194-B202 and G125-G132
claim: Let K_m=H0(I_Z^2 L), T_m=H0(I_Z^3 L), P_m=(R_+J)_m, and rho:K_m->H0((I_Z^2/I_Z^3)L). Under lower extinction P_m is contained in K_m and im(rho)=ker(partial_Z). There is a canonical exact sequence 0 -> T_m/(T_m intersect P_m) -> K_m/P_m -> ker(partial_Z)/rho(P_m) -> 0. Hence new double generators are exactly the sum of triple-hidden generators and quadratic-profile classes not produced by lower products.
falsifier: failure of exactness, a new double-generator class represented by neither a triple-hidden section nor a new quadratic profile, or a quadratic profile in rho(P_m) yielding a new class when every triple section lies in P_m
---

# B203 — New double generators have quadratic and triple-hidden parts

Let \(L=H^m\), retain B198's decomposable subspace

\[
 P_m=(R_+J)_m\subset
 K_m:=H^0(X,I_Z^2L), \tag{1}
\]

and put

\[
 T_m=H^0(X,I_Z^3L),\qquad
 A_m=H^0(X,(I_Z^2/I_Z^3)L). \tag{2}
\]

Let

\[
 \rho:K_m\longrightarrow A_m \tag{3}
\]

be the quadratic-profile map. B202's ideal-power sequence gives

\[
 \ker\rho=T_m,\qquad
 \operatorname{im}\rho=\ker\partial_Z. \tag{4}
\]

Write \(\overline P_m=\rho(P_m)\subset\ker\partial_Z\).

## Exact generator filtration

The map (3) induces a surjection

\[
 K_m/P_m\longrightarrow
 \ker\partial_Z/\overline P_m. \tag{5}
\]

Its kernel consists of classes represented by \(k\in K_m\) for which
\(\rho(k)=\rho(p)\) for some \(p\in P_m\). Then \(k-p\in T_m\), so the
kernel is

\[
 (P_m+T_m)/P_m
 \simeq T_m/(T_m\cap P_m). \tag{6}
\]

Therefore

\[
 0\longrightarrow
 \frac{T_m}{T_m\cap P_m}
 \longrightarrow
 \frac{K_m}{P_m}
 \longrightarrow
 \frac{\ker\partial_Z}{\rho(P_m)}
 \longrightarrow0. \tag{7}
\]

In particular,

\[
 \dim D_m
 =
 \dim\frac{T_m}{T_m\cap P_m}
 +
 \dim\frac{\ker\partial_Z}{\rho(P_m)},
 \qquad D_m=K_m/P_m. \tag{8}
\]

The left term records new generators invisible through quadratic order;
the right term records liftable quadratic profiles not already supplied by
products of lower ideal sections.

## Consequences for one prescribed profile

Let \(q\in\ker\partial_Z\).

- If \(q\notin\rho(P_m)\), every lift of \(q\) lies outside \(P_m\), so it
  is a new degree-\(m\) double generator.
- If \(q\in\rho(P_m)\), choose \(p\in P_m\) with \(\rho(p)=q\). Every lift
  is \(p+g\) for \(g\in T_m\). It is new only if the class of \(g\) in
  \(T_m/(T_m\cap P_m)\) is nonzero.

Thus B202's vanishing connecting class proves existence but not
minimal-generator novelty. B203 constructs no selective profile, ODP
divisor, detector, higher Kuranishi vanishing, or cycle.
