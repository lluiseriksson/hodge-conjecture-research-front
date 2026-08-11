---
brick_id: B158
status: PROVED
base_field: C
variety: a smooth analytic parameter germ with N labeled ordinary-double-point discriminant branches and critical-value map tau of differential rank R<N
smoothness: the parameter germ and each labeled branch are smooth; a chosen R-branch basis intersection is smooth by differential independence
projectivity: no projectivity is used in the analytic equivalence; the intended application is the full projective complete-linear-system germ
dimension: parameter dimension d; N critical-value branches; a basis has R branches and its persistence germ has dimension d-R
codimension: the basis-node germ is smooth of codimension R; full smooth excess occurs exactly when every other branch contains it
coefficient_field: C
cohomology_theory: analytic ideals, implicit coordinates, Hadamard lemma, discriminant branches, and ordinary-double-point deformation theory
hodge_type: none asserted
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) only downstream; no algebraic cycle or specified detector is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B144-B156 and the analytic implicit-function and Hadamard lemmas
claim: Choose any R critical-value components with independent differentials. Their smooth common zero germ F_B is the basis-node persistence germ. The following are equivalent: every remaining node branch contains F_B; every remaining critical value vanishes identically on F_B; every critical value lies in the ideal of the basis components; tau has B155's rank-R factorization with the basis components as submersion; and the full simultaneous-node germ is reduced smooth of codimension R. The restricted extra critical values form the exact escape germ.
falsifier: a basis-node germ contained set-theoretically in every branch without ideal membership, a factorization not giving persistence, or a smooth reduced height-R full node germ whose extra critical values do not vanish on the basis germ
---

# B158 — All-order factorization is persistence of the extra nodes

Let

\[
 \tau=(\tau_1,\ldots,\tau_N):(W,0)\longrightarrow(\mathbf C^N,0),
 \qquad \operatorname{rank}d\tau_0=R<N.
\]

Choose a set \(B\subset\{1,\ldots,N\}\) of size \(R\) such that
\(\{d\tau_b(0):b\in B\}\) is independent, and put

\[
 f_B=(\tau_b)_{b\in B},\qquad
 F_B=f_B^{-1}(0).
\]

The implicit-function theorem makes \(F_B\) a smooth codimension-\(R\)
germ. It parametrizes deformations on which the \(R\) basis nodes persist.
For \(i\notin B\), define the escape component

\[
 \epsilon_{B,i}=\tau_i|_{F_B}.
\]

The vector \(\epsilon_B=(\epsilon_{B,i})_{i\notin B}\) is the exact
all-order escape germ of the remaining nodes after the basis nodes have
been retained.

## Persistence equivalence

The following are equivalent.

1. The full simultaneous-node germ is reduced and smooth of codimension
   \(R\).
2. \(F_B\subseteq D_i:=\{\tau_i=0\}\) as analytic set germs for every
   \(i\notin B\).
3. \(\epsilon_B\equiv0\).
4. Every \(\tau_i\) belongs to the radical smooth ideal
   \(J_B=(\tau_b:b\in B)\).
5. There is an analytic matrix \(A_B\), whose \(B\)-rows form the identity,
   such that

   \[
   \tau=A_B f_B.
   \]

6. \(H_\tau=0\), equivalently B155's rank-\(R\) factorization holds.

Conditions 2 and 3 are the same statement. Choose analytic coordinates
\((f_B,u)\) on \(W\). If \(\tau_i(0,u)=0\), the Hadamard formula gives

\[
 \tau_i(f_B,u)=
 \sum_{b\in B} f_b
 \int_0^1
 \frac{\partial\tau_i}{\partial f_b}(t f_B,u)\,dt. \tag{1}
\]

Thus 3 implies 4 and supplies the nonbasis rows of \(A_B\); the basis rows
are the identity. Hence 3 implies 5. Conditions 4 and 5 immediately imply
3. B155-B156 identify 5 and 6 with condition 1.

In particular, a set-theoretic persistence theorem is already
scheme-theoretically strong enough here: the basis ideal is smooth and
radical, and formula (1) gives the required analytic ideal membership
without a multiplicity assumption.

## Geometric form of the remaining gate

If the conormal matroid is uniform \(U_{R,N}\), every \(R\)-subset is a
basis and defines such a smooth \(F_B\). G100 is therefore equivalent to
constructing one basis for which the other \(N-R\) nodes persist everywhere
on \(F_B\). Once that containment is known, B144 gives the saturated clean
arrangement and B156 gives all analytic syzygies.
