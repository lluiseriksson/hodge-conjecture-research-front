---
brick_id: NG118
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex 2n-fold X, a primitive rational middle Hodge class zeta, and a proposed smooth algebraic middle-dimensional carrier W
smoothness: X is smooth; W may be replaced by a smooth algebraic representative only after algebraicity is known, which is the circular step under audit
projectivity: X and any proposed algebraic carrier W are projective
dimension: dim_C X=2n and dim_C W=n
codimension: W has middle codimension n; the target cycle class also has codimension n
coefficient_field: Q for zeta, cycle classes, and the Hodge pairing; C for the B147 local Hessian mechanism
cohomology_theory: rational Betti cohomology, Hodge-Riemann polarization, algebraic cycle classes, and local nodal deformation theory
hodge_type: zeta and the proposed carrier class have type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); assuming algebraic carrier classes detect every zeta already implies middle rational HC, while requiring smooth embedded carriers may be stronger
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B001, B016, B142-B147, S019, and G092-G093
claim: For every nonzero primitive rational Hodge class zeta, first choose an algebraic middle-dimensional W with nonzero Hodge pairing against zeta and then apply the B147 carrier-conormal mechanism to construct the class-directed smooth excess required by G092.
falsifier: the Hodge-Riemann nondegenerate pairing and B016 annihilator argument show that universal access to such algebraic detector classes already forces algebraic classes to span all rational Hodge classes
---

# NG118 — The carrier Lagrangian mechanism cannot be universalized circularly

- **Route:** for a given nonzero primitive rational Hodge class \(\zeta\),
  choose a smooth algebraic middle-dimensional carrier \(W\subset X\) with
  \(\langle\zeta,[W]_{\mathrm{prim}}\rangle\ne0\), put \(W\) inside a
  high-degree nodal hypersurface, and use B147's conormal Lagrangian core to
  obtain G092.
- **Valid input:** once such a \(W\) is supplied, S019 and B142-B147 give a
  genuine and often smooth rank-deficient nodal mechanism. Its detector
  pairing can be nonzero.
- **Invalid inference:** the carrier may be chosen for every \(\zeta\)
  before the rational Hodge Conjecture is known.
- **Precise obstruction:** on primitive rational middle Hodge classes, the
  Hodge-Riemann form is nondegenerate. If algebraic primitive classes detect
  every nonzero \(\zeta\), their span has zero Hodge-class annihilator and
  therefore equals the whole rational Hodge space. This is the same
  finite-dimensional annihilator mechanism as B016 and already implies the
  middle rational Hodge Conjecture. Requiring every detector to be a smooth
  embedded carrier may be strictly stronger. A formal, analytic, or
  transcendental \(W\) avoids the circular assumption but supplies neither
  an algebraic ideal \(I_W\) in the projective linear system nor an algebraic
  cycle class.
- **Re-entry condition:** construct G093's split Lagrangian jet constraints
  directly from \((X,\zeta)\), integrate them algebraically, and prove the
  specified Saito pairing without first selecting an algebraic carrier.
