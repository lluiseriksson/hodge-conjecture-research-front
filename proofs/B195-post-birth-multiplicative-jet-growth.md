---
brick_id: B195
status: PROVED
base_field: C
variety: a smooth projective complex variety with very ample H, a fixed set Z of at least two distinct points, and the full graded systems H^m and H^(m+a)
smoothness: the variety and point supports are smooth; in the intended application the degree-m central singularities are ODPs, but the growth theorem concerns coherent first jets
projectivity: the variety, all powers of H, reduced point scheme, doubled point scheme, and complete linear systems are projective
dimension: degree-m conditional-gradient quotient dimension q_m; degree-a value-evaluation rank r_a; target quotient dimension at least r_a q_m
codimension: multiplication embeds the tensor product of degree-a value data with the one-node-determined degree-m jet quotient into the higher-degree jet quotient
coefficient_field: C for graded sections, values, gradients, and tensor products; Q remains required separately for Hodge detectors
cohomology_theory: coherent first-jet evaluation, graded multiplication, zero-dimensional Serre vanishing, and finite-dimensional tensor algebra
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream; no algebraic cycle or detector is constructed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B191-B194, G123-G125, and Serre vanishing for a fixed finite point scheme
claim: If V_m is determined by every one node, multiplication induces an injection E_a tensor V_m into V_(m+a), where E_a is the degree-a value image on Z. Hence q_(m+a)>=r_a q_m. For N>1, r_a>=2. In the maximal branch q_m=2n, every higher q is at least 4n and cannot be one-node determined; for a sufficiently large, r_a=N and V_(m+a) is the full 2nN-dimensional gradient target.
falsifier: a nonzero tensor of value data and degree-m conditional jets whose products vanish to first order at every node, a higher quotient smaller than r_a q_m, one-node determination at a higher degree in the maximal branch, or failure of eventual full gradient saturation for fixed Z
---

# B195 — Primitive birth forces multiplicative jet growth afterward

Let

\[
 V_m=H^0(I_ZH^m)/H^0(I_{2Z}H^m)
\]

and assume every node derivative

\[
 d_i:V_m\longrightarrow T_{p_i}^*X\otimes H^m|_{p_i} \tag{1}
\]

is injective. For \(a\ge1\), let

\[
 E_a=\operatorname{im}\left(
 H^0(X,H^a)\longrightarrow\bigoplus_iH^a|_{p_i}
 \right),\qquad r_a=\dim E_a. \tag{2}
\]

## The multiplication injection

Multiplication of sections defines

\[
 \mu_a:E_a\otimes V_m\longrightarrow V_{m+a}. \tag{3}
\]

It is well-defined. If a representative of a class in \(E_a\) changes by
a section vanishing on \(Z\), its product with a section already vanishing
on \(Z\) has zero value and zero derivative on \(Z\). Changing a
representative in \(V_m\) by a section of \(I_{2Z}H^m\) has the same
effect.

Choose local frames only for the injectivity calculation. For
\(\xi=\sum_\ell e_\ell\otimes v_\ell\), the derivative of \(\mu_a(\xi)\)
at node \(i\) is

\[
 d_i\left(\sum_\ell e_\ell(i)v_\ell\right). \tag{4}
\]

If \(\mu_a(\xi)=0\) in \(V_{m+a}\), every expression (4) is zero. By
injectivity of \(d_i\),

\[
 \sum_\ell e_\ell(i)v_\ell=0\quad\text{for every }i. \tag{5}
\]

But (5) says that \(\xi\) maps to zero under the tensor of the inclusion
\(E_a\hookrightarrow\bigoplus_iH^a|_{p_i}\) with \(V_m\). Tensoring an
injection of vector spaces over \(\mathbf C\) remains injective. Hence
\(\xi=0\), proving

\[
 E_a\otimes V_m\hookrightarrow V_{m+a}. \tag{6}
\]

Therefore

\[
 q_{m+a}:=\dim V_{m+a}\ge r_aq_m. \tag{7}
\]

## Immediate and asymptotic consequences

Since \(H^a\) is very ample and \(N>1\), evaluation on any two nodes has
rank two. Thus

\[
 r_a\ge2. \tag{8}
\]

In G125's maximal branch \(q_m=2n\), equations (7), (8) give

\[
 q_{m+a}\ge4n>2n. \tag{9}
\]

No map from \(V_{m+a}\) to one \(2n\)-dimensional node gradient block can
be injective, so one-node determination fails at every higher degree.

For the fixed finite scheme \(Z\), Serre vanishing makes the value
evaluation of \(H^a\) surjective for \(a\gg0\), so \(r_a=N\). Then (7)
and the ambient upper bound \(q_{m+a}\le2nN\) yield

\[
 q_{m+a}=2nN. \tag{10}
\]

Thus the higher-degree conditional gradients eventually fill the entire
nodewise gradient target. The primitive holonomy degree is isolated: it
cannot be stabilized by increasing the polarization while holding \(Z\)
fixed.

B195 makes no statement about a newly chosen node scheme at a higher
degree and constructs no detector, Kuranishi vanishing, or cycle.
