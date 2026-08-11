---
brick_id: NG149
status: NO-GO
base_field: C
variety: a two-parameter affine-linear family with two disjoint one-dimensional ODP charts and a degree-one algebraic basis carrier
smoothness: the parameter base and carrier are smooth; both spatial Hessians equal two and both critical incidences are etale
projectivity: the example is a local affine-linear slice; finite jet interpolation can place the two charts in a projective linear system, but no global Hodge detector is asserted
dimension: two base parameters, two labelled critical points, critical-value rank one, one-dimensional carrier, and one escape numerator of degree two
codimension: the carrier has degree one while its conormal defect is nonzero and visible in order one
coefficient_field: C; Q remains required only for downstream Hodge detectors
cohomology_theory: algebraic ODP critical values, finite etale incidences, Kahler differentials, and conormal modules
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B157-B185, G117-G118, S065
claim: Existence of the canonical full-incidence etale carrier and an explicit finite degree/order bound forces the required conormal jets to vanish.
falsifier: f_1(z)=z^2+x and f_2(w)=w^2+yw+x have critical values x and x-y^2/4; on the degree-one carrier x=0 the escape ideal is (y^2) and its conormal defect is nonzero in order one
---

# NG149 — A finite certificate is not a vanishing theorem

Consider the affine-linear two-parameter ODP charts

\[
 f_1(z;x,y)=z^2+x,\qquad
 f_2(w;x,y)=w^2+yw+x. \tag{1}
\]

Their critical points and Hessians are

\[
 z_c=0,\quad w_c=-y/2,\qquad
 \partial_z^2f_1=\partial_w^2f_2=2. \tag{2}
\]

Thus both critical incidences are algebraic and étale over
\(\mathbf A^2_{x,y}\). Their labelled critical values are

\[
 \tau_1=x,\qquad
 \tau_2=x-\frac{y^2}{4}. \tag{3}
\]

At the origin, \(d\tau_1=d\tau_2=dx\), so \(R=1\). Choose
\(B=\{1\}\). B185's basis carrier is simply

\[
 F_B=\{x=0\}\simeq\mathbf A^1_y,
\]

of degree one. The extra escape function is

\[
 \epsilon_{B,2}=-\frac{y^2}{4},
\qquad K_B=(y^2). \tag{4}
\]

Its conormal row is

\[
 \beta_{K_B}([y^2])=2y\,dy\pmod{y^2}, \tag{5}
\]

which is nonzero and first visible in order one. The carrier and numerator
degrees correctly give a finite certificate, but they do not make the
certificate green.

## Re-entry condition

G118 must prove the actual finite conormal coefficients vanish using new
full-incidence geometry tied to the specified Hodge detector. Étaleness,
low degree, effective elimination, and finite checkability alone cannot do
so.
