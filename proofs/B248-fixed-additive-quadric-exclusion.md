---
brick_id: B248
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with primitive ruling difference zeta=a-b, arbitrary very ample A=O_Q(k), H=A^2, and d chosen sufficiently large relative to a fixed excess j
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: complete quadric embeddings, restrictions to double and reduced points, linear spans, hyperplane-square separators, and their point ranks are projective
dimension: dim X=d=2n; write h_Z(1)=4d+4+j, N=8d+8+2j, and balanced slack s=6d+6+2j; for each fixed j choose even d with d>j+7 and 4d+4+j>binom(2j+10,j+3)
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the obstruction closes G171 and every degree-two branch with fixed additive excess above 6d
coefficient_field: Q for zeta and C for sections, tangent jets, spans, hyperplanes, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to finite unions of double and reduced points
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B231, B235, B244-B247, G171, S081
claim: For every fixed integer j>=0, no universal m=2 G144 construction can have h_Z(1)=4d+4+j, equivalently balanced slack s=6d+6+2j, in all even dimensions. More precisely, a standard quadric candidate requires j>=d-7. A nonstandard candidate with j<d-7 requires 2k<=j+7 and 4d+4+j<=binom(2j+10,j+3). Hence any surviving excess along the quadric family is unbounded in d; G171 is the case j=1 and is NO-GO.
falsifier: a fixed j candidate on an even quadric satisfying d>j+7 and 4d+4+j>binom(2j+10,j+3), failure of four-double independence, failure of B215 at degree 8+j, failure of the hyperplane-square separator, or a bounded-excess universal m=2 family
---

# B248 — Every fixed additive degree-two layer fails

Write the putative balanced point rank as

\[
 h=4d+4+j,\qquad
 N=2h=8d+8+2j,\qquad
 s=6d+6+2j, \tag{1}
\]

where \(j\ge0\) is fixed independently of \(d\). We test the valid
universal input \((Q^d,a-b)\).

## The standard polarization

B246 gives \(h\ge5d-3\) for \(A=O_Q(1)\). Thus a standard candidate
must satisfy

\[
 j\ge d-7. \tag{2}
\]

In particular, choosing \(d>j+7\) excludes the standard polarization.

## Four independent double neighborhoods

Now take \(A=O_Q(k)\), \(k\ge2\), so \(H=O_Q(2k)\). The construction
inside B247 supplies four marked points \(P=\{p_1,\ldots,p_4\}\), no
three collinear, whose double neighborhoods are independent.

For completeness, only \(k=2,3\) need the pair-line construction:
the union of three pair lines has point rank at most \(15\) or \(21\),
so a fourth point lies off it, and B235 plus the unit-jet product gives
four independent doubles. For \(k\ge4\), B215 separates four doubles
in exponent seven. Hence their dual span always has dimension

\[
 4(d+1)=4d+4. \tag{3}
\]

## High powers are immediately too large

B215 separates four double neighborhoods and \(j+1\) reduced points
in exponent

\[
 2\cdot4+(j+1)-1=8+j. \tag{4}
\]

Therefore

\[
 2k\ge8+j
 \quad\Longrightarrow\quad
 \dim S\ge4(d+1)+(j+1)=h+1, \tag{5}
\]

which is impossible. Every surviving nonstandard candidate must obey

\[
 2k\le j+7. \tag{6}
\]

Only finitely many powers remain when \(j\) is fixed.

## Bounded powers are trapped in a bounded span

Assume (6). Starting with \(L_0=\langle P\rangle\), inductively choose
marked points \(u_1,\ldots,u_{j+1}\). Before choosing \(u_{\ell+1}\),
put

\[
 L_\ell=\langle P,u_1,\ldots,u_\ell\rangle,
 \qquad \dim L_\ell\le3+\ell
 \quad(0\le\ell\le j). \tag{7}
\]

If every marked point lay in \(L_\ell\), restriction of ambient
degree-\(2k\) forms would give

\[
 h_Z(1)
 \le h^0(\mathbf P^{3+\ell},O(2k))
 =\binom{3+\ell+2k}{3+\ell}
 \le\binom{2j+10}{j+3}. \tag{8}
\]

Choose an even \(d\) such that

\[
 d>j+7,\qquad
 4d+4+j>\binom{2j+10}{j+3}. \tag{9}
\]

The right side depends only on the fixed \(j\), so such even dimensions
exist. Equations (8)-(9) force a marked
\(u_{\ell+1}\notin L_\ell\).

Choose a hyperplane \(E_\ell\) containing \(L_\ell\) and avoiding
\(u_{\ell+1}\). The section

\[
 E_\ell^2 U_\ell\in H^0(Q,O_Q(2k)), \tag{10}
\]

where \(U_\ell\) is a product of \(2k-2\) hyperplanes avoiding
\(u_{\ell+1}\), vanishes on \(2P\) and on all previous \(u_i\), but is
nonzero at \(u_{\ell+1}\). Its restriction to the irreducible quadric
is nonzero. Thus each new reduced point contributes one independent
condition.

After \(j+1\) steps, the dual span has dimension

\[
 4(d+1)+(j+1)=h+1, \tag{11}
\]

again a contradiction.

## Quantitative consequence

Every quadric candidate therefore satisfies the dichotomy

\[
 j\ge d-7
 \quad\text{or}\quad
 4d+4+j\le\binom{2j+10}{j+3}. \tag{12}
\]

Both alternatives force \(j\to\infty\) along any sequence of even
dimensions \(d\to\infty\). Consequently no fixed additive continuation
\(s=6d+C\) survives the universal quadric test. The odd slack layer has
the same integral rank budget and is excluded as well.

For G171, \(j=1\); for example \(d=124\) satisfies (9), since
\(4d+5=501>\binom{12}{4}=495\). Thus G171 is NO-GO.

B248 is a necessary special-input obstruction. It constructs no
configuration, ODP package, rational detector, specified pairing,
algebraic cycle, proof, or disproof of HC.
