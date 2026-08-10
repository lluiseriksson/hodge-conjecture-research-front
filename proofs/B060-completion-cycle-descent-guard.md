---
brick_id: B060
status: PROVED
base_field: a finitely generated field k of characteristic zero, an algebraic closure kbar, and a p-adic completion K containing k
variety: an arbitrary smooth projective k-variety, with P1_k as the explicit type-checking example
smoothness: X is smooth; P1_k is smooth
projectivity: X and P1_k are projective
dimension: arbitrary; the explicit example has dimension 1
codimension: arbitrary; the explicit example uses codimension 1 closed points
coefficient_field: Qp for cohomology and cycles; field-of-definition statements are algebraic
cohomology_theory: p-adic etale cohomology and its cycle class map
hodge_type: not used; the example's point class is the Tate class in H^2(P1,Qp(1))
cycle_class_map: Z^d(X_K)_Qp -> H^(2d)_et(X_Kbar,Qp(d)); comparison with cycles over kbar requires an actual field-of-definition descent
cycle_equivalence: rational equivalence is not needed for the field-of-definition obstruction
scope: absolute
dependencies: elementary field theory, Galois descent, and S040
claim: A cycle constructed only over a p-adic completion K cannot be averaged under Gal(kbar/k) unless it is first shown to descend to a finite algebraic extension of k; invariance of its cohomology class does not supply that descent.
falsifier: a canonical finite Gal(kbar/k)-orbit for every cycle over K derived solely from invariance of its etale cohomology class
---

# B060 - Completion-valued cycles do not descend by class invariance

Let \(k\) be a finitely generated characteristic-zero field, let
\(\bar k\) be an algebraic closure, and let \(K\) be a completion of an
embedding \(k\hookrightarrow\mathbf C_p\). A cycle

\[
 Z\in Z^d(X_K)_{\mathbf Q_p}
\]

is defined by equations with coefficients in \(K\). The group
\(G_k=\operatorname{Gal}(\bar k/k)\) acts on \(X_{\bar k}\) and on cycles
defined over \(\bar k\). It does not canonically act on a cycle whose field
of definition is only \(K\). To form a finite average

\[
 \frac{1}{[k':k]}\sum_{g\in\operatorname{Gal}(k'/k)}gZ,
\]

one must first prove that \(Z\) is defined over a finite extension
\(k'/k\). Invariance of \([Z]\) in cohomology does not prove this statement
about the equations defining \(Z\).

## Exact type-checking example

Take \(k=\mathbf Q\), \(K=\mathbf Q_p\), and choose
\(a\in\mathbf Q_p\) transcendental over \(\mathbf Q\). Such an \(a\) exists
because \(\mathbf Q_p\) is uncountable and \(\bar{\mathbf Q}\) is countable.
The point

\[
 Z_a=[a:1]\subset\mathbf P^1_K
\]

is a codimension-one cycle over \(K\), but it is not a cycle over
\(\bar{\mathbf Q}\). Its geometric cycle class is nevertheless the standard
generator

\[
 [Z_a]=1\in H^2_{\mathrm{et}}
 (\mathbf P^1_{\overline K},\mathbf Q_p(1)),
\]

the same invariant class as any rational point. Thus class invariance does
not make the expression \(gZ_a\), for
\(g\in G_{\mathbf Q}\), defined.

This example does not refute descent of a *cohomology class*: here the same
class has the rational representative \([0:1]\). It proves that a particular
completion-valued representative cannot be descended by the proposed
averaging operation without an additional finite-field-of-definition
theorem.

## Application boundary

S040's audited proof constructs a cycle over a completion
\(\widehat{k}_{\sigma_p}\) and immediately averages its alleged Galois
conjugates to obtain a cycle over \(k\). B060 shows that this transition is
ill-typed. Repairing it would require a new theorem producing a cycle over a
finite algebraic extension of \(k\), which is precisely arithmetic
algebraicity content rather than formal descent.
