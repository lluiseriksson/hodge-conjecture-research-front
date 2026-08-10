---
brick_id: B033
status: PROVED
base_field: C
variety: X = P^2 x P^2, W = diagonal P^2, A_m = O_X(m,m), and a general divisor Y in |I_W tensor A_m| for m >= 3
smoothness: X and W are smooth; Y is smooth away from W and has only ordinary double points on W
projectivity: X, W, and Y are projective
dimension: dim_C X = 4, dim_C Y = 3, and dim_C W = 2
codimension: Y has codimension 1 in X; W has middle codimension 2 in X
coefficient_field: C for interpolation, coherent cohomology, and monodromy; Q for homology and Hodge classes
cohomology_theory: coherent cohomology, Chern classes, singular homology and cohomology, vanishing cycles, Lefschetz decomposition, and limit mixed Hodge structures
hodge_type: the unique rational nodal relation has type (0,0) after Tate twist and its ambient image is the nonzero primitive projection of the diagonal class
cycle_class_map: CH^2(P^2 x P^2)_Q -> H^4(P^2 x P^2,Q(2))
cycle_equivalence: rational equivalence
scope: generic
dependencies: Thomas Theorem 4.2 (S019), Saito Proposition 1 and Theorem 1 (S022), Edmonds Theorem 1 (S031), B010, B026, B028, and B032; S034 is contextual only
claim: For every m >= 3, a general diagonal-containing (m,m) divisor has a node set that partitions into two O(m,m)-independent blocks, adjoint defect one, and rank-one extra-to-primitive map.
falsifier: failure of normal-jet surjectivity, non-full monodromy of the zeros of a general section of Omega^1_P2(2m), a subset violating the asserted uniform evaluation matroid, adjoint defect other than one, or zero primitive diagonal projection
---

# B033 - High-power diagonal two-matroid witness

Put

\[
 X=\mathbf P^2\times\mathbf P^2,\qquad
 W=\Delta_{\mathbf P^2},\qquad A_m=\mathcal O_X(m,m),
 \qquad k=2m\ge6.
\]

This extends B032 from one low-degree example to every high power in this
family. It still starts with the algebraic diagonal and therefore does not
select a detector for an arbitrary Hodge class.

## Normal derivatives and the node count

The first normal derivative lies in

\[
 H^0\bigl(W,N^*_{W/X}\otimes A_m|_W\bigr)
 =H^0\bigl(\mathbf P^2,\Omega^1_{\mathbf P^2}(k)\bigr).
\]

This normal-jet map is surjective. One way to see this is the Pieri
decomposition

\[
 \operatorname{Sym}^mV^*\otimes\operatorname{Sym}^mV^*
 =\bigoplus_{i=0}^m \mathbf S_{(2m-i,i)}V^*.
\]

Restriction to the diagonal is the \(i=0\) projection. The first conormal
quotient is the \(i=1\) summand, whose dimension is \(k^2-1\), equal to
\(h^0(\Omega^1(k))\); the induced equivariant map is nonzero and hence an
isomorphism.

The bundle \(E_k=\Omega^1_{\mathbf P^2}(k)\) is globally generated. A
general section has a reduced zero scheme \(Z_k\), and

\[
 N_k=\#Z_k=c_2(E_k)=k^2-3k+3.
\]

Bertini and the normal-derivative criterion give a divisor \(Y_m\) smooth
away from \(W\), with exactly these \(N_k\) ordinary double points on \(W\).

## Full symmetric monodromy

Let \(V_k=H^0(E_k)\), and let \(U_k\subset\mathbf P(V_k)\) be the open set
of sections with reduced zero scheme. The finite etale universal-zero cover
over \(U_k\) has monodromy \(S_{N_k}\).

First, the one-point incidence is an open subset of a projective bundle over
\(\mathbf P^2\), hence is irreducible. For distinct \(p,q\), the evaluation

\[
 V_k\longrightarrow (E_k)_p\oplus(E_k)_q
\]

is surjective. Explicitly, write a section as the cross product of
\((x,y,z)\) with three forms \(P,Q,R\) of degree \(k-2\). After moving
\(p,q\) to coordinate points, polynomial interpolation prescribes the two
fiber values independently. The ordered two-point incidence is therefore a
projective bundle over
\(\mathbf P^2\times\mathbf P^2\setminus\Delta\), and the monodromy is
2-transitive.

It also contains a transposition. On \(x=1\), with coordinates \(u=y/x\)
and \(v=z/x\), choose the two displayed local components of a one-parameter
section to be

\[
 (u^2-t,v).
\]

They are realized by homogeneous \(P,Q,R\) of degree \(k-2\); for example
take \(P=0\), \(R=-(y^2x^{k-4}-t x^{k-2})\), and
\(Q=zx^{k-3}\), then vary the unused coefficients generally. At \(t=0\)
there is one length-two zero with local incidence \(u^2=t,\ v=0\), while
Bertini makes all other zeros simple. A loop around \(t=0\) exchanges only
the two colliding zeros. Thus the monodromy contains a simple transposition.
A 2-transitive subgroup containing one transposition contains every
transposition, so it is \(S_{N_k}\).

This last step is essential: double transitivity alone says nothing about
orbits of subsets of size at least three (NG-030).

## Uniform degree-\(k\) evaluation

The Koszul resolution of \(Z_k=Z(s)\), twisted by
\(\mathcal O_{\mathbf P^2}(k)\), is

\[
 0\longrightarrow\mathcal O(3-k)
 \longrightarrow T_{\mathbf P^2}
 \longrightarrow I_{Z_k}(k)\longrightarrow0.
\]

The Euler sequence gives \(H^1(T)=H^2(T)=0\). Hence

\[
 h^1(I_{Z_k}(k))=h^2(\mathcal O(3-k))
 =h^0(\mathcal O(k-6))={k-4\choose2},
\]

and the full evaluation rank is

\[
 R_k=N_k-{k-4\choose2}=\frac{k^2+3k-14}{2}.
\]

We now use the full monodromy, not a dimension count. For each
\(1\le s\le R_k\), the finite etale cover of \(U_k\) labeling an unordered
\(s\)-subset of \(Z_k\) is irreducible because \(S_{N_k}\) is transitive on
such subsets. Rank failure for the labeled subset is closed. It is a proper
closed locus: rank \(R_k\) for the whole set supplies a basis, and every
smaller size occurs inside that basis. Because the labeling cover is finite,
the image of this bad locus in \(U_k\) is also proper closed. Removing these
finitely many images shows that for a general section every subset
\(S\subseteq Z_k\) has

\[
 r_k(S)=\min\{|S|,R_k\}.
\]

Thus the degree-\(k\) evaluation matroid is the uniform matroid
\(U_{R_k,N_k}\). Since

\[
 2R_k-N_k=6k-17>0,
\]

any division of \(Z_k\) into blocks of sizes
\(\lfloor N_k/2\rfloor\) and \(\lceil N_k/2\rceil\) makes both blocks
independent. Restriction
\(H^0(X,A_m)\to H^0(W,\mathcal O_W(k))\) is surjective, so the blocks are
independent for the defining system on \(X\). This proves the exact Edmonds
condition required by B028.

## Adjoint defect and ambient rank

The adjoint bundle is

\[
 F_m=K_X\otimes A_m^2=\mathcal O_X(k-3,k-3),
 \qquad F_m|_W=\mathcal O_W(2k-6).
\]

Twisting the same Koszul resolution by \(\mathcal O_W(2k-6)\) gives

\[
 0\longrightarrow\mathcal O_W(-3)
 \longrightarrow T_{\mathbf P^2}(k-6)
 \longrightarrow I_{Z_k/W}(2k-6)\longrightarrow0.
\]

Bott/Euler vanishing yields
\(h^1(I_{Z_k/W}(2k-6))=h^2(\mathcal O_W(-3))=1\).
The restriction sequence of the diagonal has no intervening higher
cohomology in these nonnegative bidegrees, so

\[
 h^1(X,I_{Z_k}\otimes F_m)=1.
\]

The coherent vanishings used in B026 hold by Bott and Kunneth. Therefore
the rational relation and extra-homology spaces are one-dimensional.

Finally, the ambient calculation is independent of \(m\). For

\[
 \gamma=h_1^2-h_1h_2+h_2^2,
\]

the diagonal satisfies

\[
 [W]=\frac23(h_1+h_2)^2+\frac13\gamma,
 \qquad \int_X\gamma^2=3.
\]

The smooth-divisor Gysin image is
\((h_1+h_2)H^2(X,\mathbf Q)\), so the diagonal generates the
one-dimensional extra quotient and maps to
\(\frac13\gamma\ne0\). Consequently \(\operatorname{rank}\Phi_{Y_m}=1\),
and its image pairs nontrivially with \(\gamma\).

## Scope guard and next gate

This proves that isolated nodality, a two-part smoothing partition,
positive adjoint defect, positive ambient rank, and a nonzero primitive
pairing coexist at every power \(m\ge3\) in this family. It removes the
low-degree caveat from B032.

It does not remove the algebraic anchor. The primitive direction is known
in advance because the divisor is forced to contain \(W\). No step associates
an unanchored nodal incidence to an arbitrary rational Hodge class. The next
gate is G014: prove that the canonical images of unanchored two-part nodal
relations span primitive rational Hodge homology. B033 contributes zero
progress toward the general Hodge Conjecture.
