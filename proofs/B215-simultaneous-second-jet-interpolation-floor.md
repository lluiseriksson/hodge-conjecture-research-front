---
brick_id: B215
status: PROVED
base_field: C
variety: a smooth projective complex d-fold with very ample H, a finite reduced point scheme Z, and G143's lower two-layer extinction and full-support degree-m relation
smoothness: X and Z are smooth; the local triple neighborhoods have length c_d=binom(d+2,2), while no divisor or incidence smoothness is inferred
projectivity: X, powers of H, mixed unions of triple, double, and reduced marked points, their restriction maps, and value-relation multiplication are projective
dimension: dim X=d; q triple points, u double points, and t simple points are interpolated in degree 3q+2u+t-1; the Hodge case has d=2n
codimension: simultaneous mixed-jet interpolation raises each lower value rank to L_d(k), and B213 yields the optimized node floor D_d(m)
coefficient_field: C for separating sections, local jets, restriction ranks, and relations; Q remains required separately for the Hodge detector
cohomology_theory: coherent restriction to finite schemes, principal parts through order two, graded section multiplication, and finite-dimensional duality
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B187, B209-B214, G143
claim: H^(3q+2u+t-1) restricts surjectively to the disjoint union of q prescribed triple neighborhoods, u double neighborhoods, and t reduced points. Under G143 lower extinction, h_Z(k)>=L_d(k)=c_d floor((k+1)/3)+phi_d((k+1) mod 3), where phi_d(0)=0, phi_d(1)=1, and phi_d(2)=d+1. Consequently N>=D_d(2)=2(d+1); for m>=3, N>=D_d(m)=c_d floor((m+2)/3)+phi_d((m+2) mod 3).
falsifier: a mixed jet datum not interpolated in degree 3q+2u+t-1, a lower point span smaller than L_d(k) under extinction, or G143 data below the displayed D_d(m) floor
---

# B215 — Simultaneous second-jet interpolation raises the floor

Set

\[
 c_d=\binom{d+2}{2},\qquad
 \phi_d(0)=0,\quad\phi_d(1)=1,\quad\phi_d(2)=d+1. \tag{1}
\]

## A mixed finite-scheme interpolation lemma

Choose distinct points \(p_1,\ldots,p_s\), assign jet orders
\(r_i\in\{0,1,2\}\), and put

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
\(p_j\), \(j\ne i\). Very ampleness gives the full order-one jet for
\(r_i=1\), while B214 gives the full order-two jet for \(r_i=2\);
for \(r_i=0\) use constants. Multiplication by the unit \(P_i\) is an
automorphism of the local truncated algebra. Thus degree

\[
 \sum_{j\ne i}(r_j+1)+r_i=K \tag{5}
\]

sections realize an arbitrary prescribed jet at \(p_i\) and zero jets at
all other supports. Summing over \(i\) proves surjectivity onto the whole
mixed finite scheme.

For \(q\) triple neighborhoods, \(u\) double neighborhoods, and \(t\)
reduced points, this says

\[
 K=3q+2u+t-1, \tag{6}
\]

and the target dimension is

\[
 qc_d+u(d+1)+t. \tag{7}
\]

The same conclusion holds in every degree \(k\ge K\), after multiplying
by a section of \(H^{k-K}\) nonzero at all selected supports.

## Lower ranks under second-osculating absorption

For \(k\ge1\), write

\[
 k+1=3q_k+\rho_k,\qquad \rho_k\in\{0,1,2\}. \tag{8}
\]

Inspection of B214's three cases gives \(N\ge C_d(m)\ge m\). Hence there
are enough marked points to take \(q_k\) triples and, when
\(\rho_k=1\), one simple point, or when \(\rho_k=2\), one double point.
G143's lower extinction places all their dual jet spaces inside the
degree-\(k\) point span. Therefore

\[
 h_Z(k)\ge
 L_d(k):=
 c_d\left\lfloor\frac{k+1}{3}\right\rfloor
 +\phi_d((k+1)\bmod3)
 \quad(1\le k<m). \tag{9}
\]

## Optimize complementary relation transport

B213 gives \(h_Z(a)+h_Z(m-a)\le N\). For \(m=2\), equation (9) yields

\[
 N\ge2(d+1). \tag{10}
\]

Assume \(m\ge3\). Put \(x=a+1\), \(y=m-a+1\), so \(x+y=m+2\).
A direct check of the residue pairs modulo three, using
\(c_d\ge d+2\), shows the maximum uses residues \((0,0)\) when
\(m+2\equiv0\), \((0,1)\) when \(m+2\equiv1\), and \((0,2)\) when
\(m+2\equiv2\). The competing losses are respectively
\(c_d-d-2\), \(c_d-2d-1=d(d-1)/2\), and \(d-1\), all nonnegative.
Therefore

\[
 \max_{1\le a<m}
 \bigl(L_d(a)+L_d(m-a)\bigr)
 =
 c_d\left\lfloor\frac{m+2}{3}\right\rfloor
 +\phi_d((m+2)\bmod3). \tag{11}
\]

For \(m\ge4\), the pair \(a=2,m-2\) attains the maximum; for \(m=3\),
use \(a=1,m-1\). Define

\[
 D_d(2)=2(d+1), \tag{12}
\]

and, for \(m\ge3\),

\[
 D_d(m)=
 c_d\left\lfloor\frac{m+2}{3}\right\rfloor
 +\phi_d((m+2)\bmod3). \tag{13}
\]

Every G143 configuration has \(N\ge D_d(m)\). B215 constructs no such
configuration, central profile, holonomy, detector, or algebraic cycle.
