---
brick_id: B001
status: PROVED
base_field: C
variety: arbitrary smooth projective algebraic variety X
smoothness: smooth
projectivity: projective
dimension: arbitrary n >= 0
codimension: arbitrary 0 <= p <= n
coefficient_field: Q
cohomology_theory: singular Betti cohomology with rational coefficients
hodge_type: (p,p), shifted to middle type (N/2,N/2)
cycle_class_map: CH^p(X)_Q -> H^{2p}(X^an,Q(p))
cycle_equivalence: rational equivalence
scope: absolute
dependencies: projective bundle Kunneth formula; functoriality of Chow pullback/pushforward and Betti cycle classes
claim: Universal rational HC is equivalent to universal middle-degree rational HC.
falsifier: a failure of either projective-space construction to return the original Betti class under the stated Chow operation
---

# B001 - Reduction to middle degree

## Statement

Let **MHC** say: for every smooth projective complex variety \(Y\) of even
dimension \(N=2m\), every rational middle Hodge class
\(\beta\in H^N(Y,\mathbf Q)\cap H^{m,m}(Y)\) is the class of an element of
\(CH^m(Y)_{\mathbf Q}\). Then MHC is equivalent to the standard rational Hodge
Conjecture HC.

## Proof

HC implies MHC by specialization of its universal quantifiers.

Assume MHC. Let \(X\) be smooth projective of dimension \(n\), and let
\(\alpha\in H^{2p}(X,\mathbf Q)\cap H^{p,p}(X)\).

### Case 1: \(2p\le n\)

Put \(r=n-2p\) and \(Y=X\times\mathbf P^r\). Then
\(\dim Y=n+r=2(n-p)\). If \(h\in H^2(\mathbf P^r,\mathbf Q)\) is the
hyperplane class, then

\[
 \beta=\operatorname{pr}_X^*\alpha\smile
       \operatorname{pr}_{\mathbf P}^*h^r
\]

has degree \(2p+2r=2(n-p)=\dim Y\) and Hodge type
\((n-p,n-p)\). MHC gives a middle-codimension rational cycle \(Z\) on \(Y\)
with class \(\beta\). Proper pushforward along
\(\operatorname{pr}_X:Y\to X\) gives a codimension-\(p\) rational cycle and

\[
 \operatorname{cl}(\operatorname{pr}_{X*}Z)
 =\operatorname{pr}_{X*}(\beta)=\alpha\int_{\mathbf P^r}h^r=\alpha.
\]

### Case 2: \(2p\ge n\)

Put \(r=2p-n\) and \(Y=X\times\mathbf P^r\), so \(\dim Y=2p\). The class
\(\beta=\operatorname{pr}_X^*\alpha\) is middle of type \((p,p)\). By MHC it
is the class of a codimension-\(p\) rational cycle \(Z\) on \(Y\). For the
regular embedding \(i:X=X\times\{t\}\hookrightarrow Y\) at any closed point
\(t\), the refined Gysin pullback is a codimension-\(p\) class
\(i^!Z\in CH^p(X)_{\mathbf Q}\), and compatibility of cycle classes gives

\[
 \operatorname{cl}(i^!Z)=i^*\beta=\alpha.
\]

At \(2p=n\), either construction has \(r=0\). Thus every rational Hodge class
on every \(X\) is algebraic. QED.

## Adversarial audit

- Both auxiliary varieties remain smooth and projective over \(\mathbf C\).
- The coefficients stay rational; no integral assertion is used.
- The first case uses normalized \(\int_{\mathbf P^r}h^r=1\).
- The second case uses a Chow/Gysin pullback along a regular embedding, not a
  set-theoretic intersection assumption.
- No inverse hard-Lefschetz correspondence and no Hodge Conjecture on \(X\) is
  smuggled into the proof.
- MHC remains universal over all even-dimensional smooth projective varieties,
  including the products constructed here; this is a reduction in degree, not
  a claim that a special-family case suffices.

