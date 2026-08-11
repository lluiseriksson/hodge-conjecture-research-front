---
brick_id: NG150
status: NO-GO
base_field: C
variety: a two-parameter affine-linear family with two labelled one-dimensional ODP charts having equal quadratic but unequal cubic critical-value terms
smoothness: the parameter base is smooth and both central spatial Hessians equal one; both critical incidences are etale
projectivity: the model is an affine-linear local slice realizable by finite jet interpolation in a projective linear system; no global Hodge detector is asserted
dimension: two base parameters, two nodes, critical-value rank one, one-dimensional basis carrier, and a cubic escape generator
codimension: K_B is contained in m^3 but not m^4; the quadratic Kuranishi tensor vanishes while the cubic tensor is nonzero
coefficient_field: C; Q remains required only for downstream Hodge detectors
cohomology_theory: algebraic critical values, implicit critical-point series, Kuranishi tensors, and conormal modules
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B146, B154, B157, B186, G118-G119, NG125, S065
claim: Vanishing of the complete quadratic Kuranishi tensor for an affine-linear ODP family forces the cubic and all later finite conormal rungs to vanish.
falsifier: the two charts f_a=x+yw+w^2/2+a w^3 and f_b=x+yw+w^2/2+b w^3 with a not equal b have identical linear and quadratic critical-value terms but cubic difference (a-b)y^3 on the basis carrier
---

# NG150 — Quadratic vanishing does not promote to the cubic rung

Fix \(a\ne b\), and consider the two affine-linear parameter families

\[
 f_a(w;x,y)=x+yw+\frac12w^2+a w^3,
 \qquad
 f_b(w;x,y)=x+yw+\frac12w^2+b w^3. \tag{1}
\]

At \((x,y,w)=(0,0,0)\), both spatial Hessians equal one. Their critical
points solve

\[
 y+w+3a w^2=0,\qquad y+w+3b w^2=0,
\]

so the implicit expansions are

\[
 w_a(y)=-y-3a y^2+O(y^3),\qquad
 w_b(y)=-y-3b y^2+O(y^3). \tag{2}
\]

Let \(\tau_a,\tau_b\) be the critical values. The envelope identity
\(\partial_y\tau_a=w_a\) gives

\[
 \tau_a=x-\frac12y^2-a y^3+O(y^4),\qquad
 \tau_b=x-\frac12y^2-b y^3+O(y^4). \tag{3}
\]

Their differentials at the origin both equal \(dx\), so the value rank is
one. Choose \(\tau_a\) as the basis value. On its smooth zero germ,

\[
 x=\frac12y^2+a y^3+O(y^4),
\]

and the nonbasis escape is

\[
 \epsilon_b=(a-b)y^3+O(y^4). \tag{4}
\]

Therefore

\[
 K_B\subset\mathfrak m^3,\qquad
 K_B\not\subset\mathfrak m^4.
\]

The complete quadratic Kuranishi tensor vanishes, but the cubic tensor is
nonzero. By B186, \(j^1\beta_{K_B}=0\) while
\(j^2\beta_{K_B}\ne0\).

## Re-entry condition

After G119, the cubic tensor must be killed by a separate full-incidence
mechanism, followed by every higher rung through \(D_{\mathrm{car}}\).
Quadratic Hessian isotropy supplies no automatic recurrence.

NG125 already excludes promotion from an arbitrary fixed Kuranishi
truncation using nonlinear critical-value germs. NG150 strengthens the
first transition by realizing the quadratic/cubic separation inside an
affine-linear parameter family with nondegenerate ODP Hessians.
