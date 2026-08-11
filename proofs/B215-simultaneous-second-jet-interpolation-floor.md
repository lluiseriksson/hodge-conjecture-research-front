---
brick_id: B215
status: PROVED
base_field: C
variety: a smooth projective complex d-fold with very ample H, a finite reduced point scheme Z, and G143's lower two-layer extinction and full-support degree-m relation
smoothness: X and Z are smooth; the local triple neighborhoods have length c_d=binom(d+2,2), while no divisor or incidence smoothness is inferred
projectivity: X, powers of H, mixed unions of triple and reduced marked points, their restriction maps, and value-relation multiplication are projective
dimension: dim X=d; q triple points and t simple points are interpolated in degree 3q+t-1; the Hodge case has d=2n
codimension: simultaneous mixed-jet interpolation raises each lower value rank to L_d(k), and B213 yields the optimized node floor D_d(m)
coefficient_field: C for separating sections, local jets, restriction ranks, and relations; Q remains required separately for the Hodge detector
cohomology_theory: coherent restriction to finite schemes, principal parts through order two, graded section multiplication, and finite-dimensional duality
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B187, B209-B214, G143
claim: H^(3q+t-1) restricts surjectively to the disjoint union of q prescribed triple neighborhoods and t prescribed reduced points. Under G143 lower extinction, h_Z(1)>=d+1 and h_Z(k)>=L_d(k)=c_d floor((k+1)/3)+((k+1) mod 3) for k>=2. Consequently N>=D_d(2)=2(d+1); for m>=3, N>=D_d(m), where D_d(m)=c_d m/3+d+1 if 3 divides m, and D_d(m)=c_d floor((m+2)/3)+((m+2) mod 3) otherwise.
falsifier: a mixed jet datum not interpolated in degree 3q+t-1, a lower point span smaller than L_d(k) under extinction, or G143 data below the displayed D_d(m) floor
---

# B215 — Simultaneous second-jet interpolation raises the floor

Set

\[
 c_d=\binom{d+2}{2}. \tag{1}
\]

## A mixed finite-scheme interpolation lemma

Choose distinct points \(p_1,\ldots,p_s\), and assign jet orders
\(r_i\in\{0,2\}\). Put

\[
 K=\sum_{i=1}^s(r_i+1)-1. \tag{2}
\]

For every ordered pair \(i\ne j\), very ampleness supplies a section

\[
 \ell_{ij}\in H^0(X,H),\qquad
 \ell_{ij}(p_j)=0,\quad \ell_{ij}(p_i)\ne0. \tag{3}
\]

Define

\[
 P_i=\prod_{j\ne i}\ell_{ij}^{\,r_j+1}
 \in H^0\!\left(X,H^{\sum_{j\ne i}(r_j+1)}\right). \tag{4}
\]

It is a unit at \(p_i\) and vanishes to order at least \(r_j+1\) at every
\(p_j\), \(j\ne i\). B214 gives surjectivity onto the order-\(r_i\) jet
at \(p_i\): for \(r_i=0\) use constants, and for \(r_i=2\) use sections
of \(H^2\). Multiplication by the unit \(P_i\) is an automorphism of the
local truncated algebra. Thus degree

\[
 \sum_{j\ne i}(r_j+1)+r_i=K \tag{5}
\]

sections realize an arbitrary prescribed jet at \(p_i\) and zero jets at
all other supports. Summing over \(i\) proves surjectivity onto the whole
mixed finite scheme.

For \(q\) triple neighborhoods and \(t\) reduced points, (2) is

\[
 K=3q+t-1, \tag{6}
\]

and the target dimension is

\[
 qc_d+t. \tag{7}
\]

The same conclusion holds in every degree \(k\ge K\), after multiplying
by a section of \(H^{k-K}\) nonzero at all selected supports.

## Lower ranks under second-osculating absorption

For \(k\ge2\), write

\[
 k+1=3q_k+t_k,\qquad
 q_k=\left\lfloor\frac{k+1}{3}\right\rfloor,\quad
 t_k\in\{0,1,2\}. \tag{8}
\]

Inspection of B214's three cases gives \(N\ge C_d(m)\ge m\), so for every
\(k<m\) there are at least \(q_k+t_k\) marked points. Apply (6)--(7) to
\(q_k\) triple points and \(t_k\) other reduced points. G143's lower
extinction places all their dual jet spaces inside the degree-\(k\) point
span. Therefore

\[
 h_Z(1)\ge d+1,\qquad
 h_Z(k)\ge
 L_d(k):=
 c_d\left\lfloor\frac{k+1}{3}\right\rfloor
 +((k+1)\bmod3)
 \quad(2\le k<m). \tag{9}
\]

## Optimize complementary relation transport

B213 gives \(h_Z(a)+h_Z(m-a)\le N\). For \(m=2\), this remains

\[
 N\ge2(d+1). \tag{10}
\]

Assume \(m\ge3\). The endpoint pair \(1,m-1\) gives

\[
 N\ge d+1+
 c_d\left\lfloor\frac m3\right\rfloor+(m\bmod3). \tag{11}
\]

If \(m\ge4\), for an interior pair set \(x=a+1\),
\(y=m-a+1\), so \(x+y=m+2\).
The sum in (9) is maximized when the sum of the two remainders modulo
three is minimal. The pair \(a=2,m-2\) attains this maximum:

\[
 N\ge
 c_d\left\lfloor\frac{m+2}{3}\right\rfloor
 +((m+2)\bmod3). \tag{12}
\]

For \(m\ge4\), if \(3\mid m\), (11) exceeds (12) by \(d-1\);
otherwise (12) is at least (11), since \(c_d\ge d+2\). When \(m=3\),
(11) is the only type of pair and already has the divisible-case value.
Hence define

\[
 D_d(2)=2(d+1), \tag{13}
\]

and, for \(m\ge3\),

\[
 D_d(m)=
 \begin{cases}
 c_d\,m/3+d+1,&3\mid m,\\
 c_d\left\lfloor\dfrac{m+2}{3}\right\rfloor
 +((m+2)\bmod3),&3\nmid m.
 \end{cases} \tag{14}
\]

Every G143 configuration has \(N\ge D_d(m)\). B215 constructs no such
configuration, central profile, holonomy, detector, or algebraic cycle.
