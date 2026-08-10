---
brick_id: B037
status: PROVED
base_field: C
variety: the exceptional P^1 in the blow-up of the U_(2,5) local smoothing-parameter slice for a projective nodal hyperplane-section family
smoothness: the exceptional curve is smooth; its five marked boundary crossings are simple normal crossings; the central projective fiber has five ordinary double points and nearby fibers are smooth
projectivity: the exceptional curve and motivating hyperplane-section family are projective; the parameter calculation is local analytic
dimension: exceptional curve dimension 1, parameter surface dimension 2, ambient projective variety dimension 2n, and nearby fiber dimension 2n-1
codimension: marked crossings have codimension 1 on the exceptional curve and the unresolved original stratum has codimension 2 in the parameter surface; downstream cycles have middle codimension n
coefficient_field: Q
cohomology_theory: resolved Picard-Lefschetz monodromy complex, constructible-sheaf hypercohomology, and its local-to-global spectral sequence
hodge_type: the transgression is rational; no type-(0,0) mixed-Hodge comparison is asserted
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009, B035-B036, Green-Griffiths S021, and the hypercohomology spectral sequence
claim: In the nonzero five-cycle U_(2,5) model, the resolved exceptional complex has constant H^0 equal to K=ker N_E and H^1 equal to five one-dimensional skyscrapers; hence its degree-one hypercohomology is the kernel of the unique possible transgression d_2:Q^5 -> H^2(P^1,K)=K, and this resolved contribution equals the desired relation kernel exactly when d_2 factors as the vanishing-cycle map Q^5 -> W followed by an injection W -> K.
falsifier: a resolved U_(2,5) Picard-Lefschetz complex satisfying B035-B036 whose cohomology sheaves have another nonzero constituent, whose local-to-global spectral sequence has another differential affecting total degree one, or for which H^1 is not ker(d_2)
---

# B037 - Exceptional transgression gate

B036 determines how many global constraints are missing from the five
resolved crossing groups. B037 locates those constraints as one explicit
hypercohomology transgression.

## The exceptional constructible complex

Let \(E\simeq\mathbf P^1\) be the exceptional curve of B035, with marked
points \(p_i=E\cap\widetilde H_i\). Let \(\mathcal B_E^\bullet\) denote the
restriction to \(E\) of the resolved Green–Griffiths monodromy complex. Put

\[
 W=\operatorname{span}_{\mathbf Q}\{\delta_1,\ldots,\delta_5\},
 \qquad K=\ker N_E.
\]

At a generic point of \(E\), the complex is

\[
 V\xrightarrow{N_E}W.
\]

B036 proves that \(N_E\) is onto and
\(K=\bigcap_i\ker N_i\). Its generic cohomology is therefore \(K\) in
degree zero and zero in degree one.

At \(p_i\), the local complex is

\[
 V\xrightarrow{(N_E,N_i)}W\oplus\mathbf Q\delta_i.
\]

Its degree-zero kernel is still \(K\), and B036 proves that its degree-one
cokernel is one-dimensional. Since every \(T_i=1+N_i\) acts trivially on
\(K\), the degree-zero cohomology sheaf has no monodromy around the marked
points. Thus

\[
 \mathcal H^0(\mathcal B_E^\bullet)=K_E,
 \qquad
 \mathcal H^1(\mathcal B_E^\bullet)
   =\bigoplus_{i=1}^5\mathbf Q_{p_i},
\]

and all other cohomology sheaves vanish. Here \(K_E\) is the constant
rational sheaf with fiber \(K\).

## The only possible differential

The local-to-global hypercohomology spectral sequence is

\[
 E_2^{p,q}=H^p\!\left(E,
   \mathcal H^q(\mathcal B_E^\bullet)\right)
 \Longrightarrow
 \mathbb H^{p+q}(E,\mathcal B_E^\bullet).
\]

For \(E\simeq\mathbf P^1\),

\[
 H^1(E,K_E)=0,
 \qquad H^2(E,K_E)\simeq K,
\]

while a skyscraper sheaf has only degree-zero cohomology. Consequently the
only differential that can affect total degree one is

\[
 d_2:E_2^{0,1}=\mathbf Q^5
 \longrightarrow E_2^{2,0}=K.
\]

There is no possible incoming differential. Therefore

\[
 \mathbb H^1(E,\mathcal B_E^\bullet)=\ker d_2.
\]

The five crossing cokernels do not split globally unless \(d_2=0\); their
gluing is exactly the Postnikov extension class represented by this map.

## Exact form required in the resolved contribution

Because the vanishing cycles are mutually orthogonal, \(W\subseteq K\).
Let

\[
 \phi:\mathbf Q^5\to W,
 \qquad e_i\mapsto\delta_i.
\]

B036 gives \(R=\ker\phi\). Hence the resolved exceptional contribution is
the desired \(U_{2,5}\) relation space exactly when

\[
 \ker d_2=R.
\]

Equivalently, \(d_2\) must factor as

\[
 \mathbf Q^5\xrightarrow{\phi}W
 \xrightarrow{u}K
\]

for an injective \(u\). The geometric normalization sought is
\(u:W\hookrightarrow K\), so that

\[
 d_2(e_i)=\delta_i
\]

after the common orientation convention. Computing this Postnikov/residue
class—not its possible rank—is now the smallest open topological brick.

## Scope guard

B037 does not compute \(d_2\). In particular, it does not infer the map from
the desired answer, and it does not prove G015. Even the formula
\(d_2(e_i)=\delta_i\) would still require a rational type-\((0,0)\)
mixed-Hodge comparison, identification of the downstairs IC summand inside
the proper direct image, and extension from this first arrangement to
general multipart smoothing slices. No algebraic cycle or new general Hodge
class is constructed.
