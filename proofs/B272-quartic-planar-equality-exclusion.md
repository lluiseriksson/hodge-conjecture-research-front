---
brick_id: B272
status: PROVED
base_field: C
variety: the smooth split even-dimensional quadric X=Q^d with d=2n>=22, primitive ruling difference zeta=a-b, quartic A=O_Q(4), H=O_Q(8), and a hypothetical G190 marked scheme
smoothness: Q^d and the reduced marked scheme are smooth; all auxiliary supports and plane lines are reduced; no central ODP package is constructed
projectivity: the complete octic embedding, plane restrictions, pair-line products, first jets, and marked point spans are projective
dimension: dim X=d=2n>=22; six independent doubles have rank 6d+6 and every seventh residual octic image has rank at least d, so h_Z(1)>=7d+6
codimension: the primitive codimension-n ruling difference supplies a universal test input; the theorem excludes quartic equality h_Z(1)=7d+5 but leaves the next rank 7d+6 and every detector clause open
coefficient_field: Q for zeta and C for sections, planar coordinates, and first jets
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B196, B260-B271, G190-G192, S081
claim: On every split even Q^d with d>=22, the quartic polarization A=O_Q(4) satisfies h_Z(1)>=7d+6 under the G190 lower-extinction hypotheses. Hence quartic equality 7d+5 is impossible. Together with B271 and B266, this closes G190 and G191 as NO-GO and activates G192 at the next piecewise floor.
falsifier: a quartic G190 candidate of rank 7d+5, failure of the perfect-matching full-jet construction when every line-through-u class has size at most three, failure of the explicit transverse octic when one class has size four, residual rank below d, or a different next piecewise boundary
---

# B272 — Quartic planar equality also fails

Let \(P_6\) be the six independent double supports and \(u\) the
seventh marked point. Partition \(P_6\) by the lines through \(u\).
B260 chooses the first four supports with no three collinear, so every
class has size at most four. The following two cases are exhaustive.

## No four-point class

If every class has size at most three, the complete multipartite good
graph has a perfect matching. The product \(C\) of its three pair lines
is a cubic vanishing on \(P_6\) and nonzero at \(u\). Therefore

\[
 C^2H^0(Q,O_Q(2))\subset H^0(Q,I_{2P_6}(8)). \tag{1}
\]

The square \(C^2\) is a unit on \(2u\), and the complete quadratic
system supplies all \(d+1\) first-jet coordinates. Thus the residual
rank is \(d+1\), already giving total rank \(7d+7\).

## The four-point class

Suppose four supports \(r_1,\ldots,r_4\) lie on a line
\(L\) through \(u\); write \(a,b\) for the other two. B264 puts the
equality configuration in the plane spanned by these data. We construct
an octic \(F\) that vanishes doubly at \(P_6\), has value zero at \(u\),
and has nonzero derivative there transverse to \(L\).

If the line \(\overline{ab}\) avoids \(u\), choose one further line
through each of \(a,b\) avoiding \(u\), and one line through each
\(r_i\) avoiding \(u\). Their product with \(\overline{ab}\) is a
degree-seven polynomial \(G\), double at \(a,b\), simple at each
\(r_i\), and nonzero at \(u\). If \(\ell=0\) is the equation of \(L\),
then

\[
 F=\ell G \tag{2}
\]

is the required octic.

It remains to handle \(a,b,u\) collinear. Choose affine coordinates

\[
 L=(y=0),\quad \overline{ab}=(x=0),\quad
 u=(0,0),\quad r_i=(\alpha_i,0),\quad
 a=(0,\beta_1),\quad b=(0,\beta_2), \tag{3}
\]

with all displayed nonzero parameters distinct where required. Put

\[
 R(x)=\prod_{i=1}^4(x-\alpha_i),\qquad
 S(y)=(y-\beta_1)^2(y-\beta_2)^2,\qquad
 c=\frac{R(0)}{S(0)}. \tag{4}
\]

Choose the affine linear polynomial \(V(y)\) satisfying

\[
 \beta_jV(\beta_j)=-R'(0),\qquad j=1,2, \tag{5}
\]

and define

\[
 G(x,y)=R(x)-R(0)+cS(y)+xyV(y). \tag{6}
\]

Then \(G(r_i)=0\), \(G\) vanishes doubly at \(a,b\), and

\[
 G(u)=R(0)\ne0. \tag{7}
\]

Thus \(yG\) has the required double zeros and a nonzero transverse
derivative at \(u\). Its degree is five; multiply it by the cube of a
general line avoiding all seven supports to obtain the required octic.

## Rank consequence

B260's eight-edge product supplies a residual octic that is a unit at
\(u\). Equation (2), or the octic obtained by homogenizing \(yG\) and
multiplying by the unit-line cube, supplies an independent zero-value
plane derivative. Choose ambient linear lifts of the plane coordinates
whose differentials at \(u\) annihilate a complement of \(T_u\Pi\);
the lifted polynomial preserves the plane derivative and has zero normal
first derivatives there. Hence the residual plane-jet image has rank at
least two.

Degree-seven plane values on \(P_6\cup\{u\}\) are independent: to
isolate one of seven distinct points, multiply six lines through the
other points and avoiding the target, then multiply by a unit line.
The conormal quotient therefore supplies all \(d-2\) normal directions
at \(u\). The full residual rank is at least

\[
 2+(d-2)=d. \tag{8}
\]

Adding the six independent double blocks gives

\[
 h_Z(1)\ge6d+6+d=7d+6. \tag{9}
\]

Therefore quartic equality \(7d+5\) is impossible for every even
\(d\ge22\). B272 constructs no ODP package, Kuranishi vanishing,
rational detector, specified pairing, algebraic cycle, proof, or
disproof of HC.
