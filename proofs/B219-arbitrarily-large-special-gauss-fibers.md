---
brick_id: B219
status: PROVED
base_field: C
variety: for every d>=2 and N>=1, a constructed smooth degree-e hypersurface X^d in P^(d+1) with H=O_X(1), together with a hyperplane Lambda and N marked points Z
smoothness: X is smooth; its hyperplane section Y=X intersect Lambda has ordinary double points at every point of Z and is smooth away from Z
projectivity: projective spaces, the prescribed-jet linear system on Lambda, the extension family f+x_0G, X, Y, and the H-Gauss map are projective
dimension: dim X=d, dim Lambda=d, dim Y=d-1, and e=3N is an explicit sufficient degree
codimension: the special ordinary-Gauss fiber over Lambda contains at least N distinct points, with no bound on N as the constructed hypersurface degree varies
coefficient_field: C for sections, jets, Bertini, tangent hyperplanes, and Gauss fibers
cohomology_theory: coherent restriction to triple points and principal parts through order two; no Hodge cohomology enters
hodge_type: none asserted; no rational detector or specified Hodge pairing is constructed
cycle_class_map: CH^p(X)_Q -> H^(2p)(X,Q(p)) is not used
cycle_equivalence: rational equivalence remains the terminal relation and is unused
scope: absolute
dependencies: B214-B215, S065, S079
claim: For every d>=2 and N>=1 there is a smooth nondegenerate complex hypersurface X^d in P^(d+1) whose ordinary Gauss map has a fiber containing N distinct points. One may take degree e=3N: prescribe an ODP hyperplane section at N points using simultaneous two-jet interpolation, then choose a general extension F=f+x_0G with G nonzero at the nodes.
falsifier: failure of degree-3N simultaneous two-jet interpolation, a forced singularity of every extension X, or a marked point whose tangent hyperplane is not Lambda
---

# B219 — Special Gauss fibers can be arbitrarily large

Fix \(d\ge2\), \(N\ge1\), a hyperplane

\[
 \Lambda=\{x_0=0\}\simeq\mathbf P^d\subset\mathbf P^{d+1},
\]

and distinct points \(Z=\{p_1,\ldots,p_N\}\subset\Lambda\). Put
\(e=3N\).

## A nodal hypersurface inside the tangent hyperplane

B215 applied to \((\mathbf P^d,\mathcal O(1))\) gives

\[
 H^0(\Lambda,\mathcal O_\Lambda(e))
 \twoheadrightarrow
 \bigoplus_{i=1}^N
 \mathcal O_{\Lambda,p_i}/\mathfrak m_{p_i}^3. \tag{1}
\]

Choose at every \(p_i\) a jet with zero constant and linear terms and a
nondegenerate quadratic term. Let \(f_0\) realize these jets. The affine
space

\[
 f_0+H^0(\Lambda,I_{3Z}(e)) \tag{2}
\]

has the prescribed ODP jets.

It is basepoint-free on \(\Lambda\setminus Z\): for
\(q\notin Z\), choose a linear form \(\ell_i\) vanishing at \(p_i\)
and nonzero at \(q\); then \(\prod_i\ell_i^3\) has degree \(3N=e\),
lies in \(I_{3Z}(e)\), and is nonzero at \(q\). By S079 Bertini, a
general \(f\) in (2) defines

\[
 Y=(f=0)\subset\Lambda \tag{3}
\]

with ODPs exactly at the marked points and smooth away from them.

## Smooth the ambient hypersurface only in the normal direction

Consider degree-\(e\) hypersurfaces of \(\mathbf P^{d+1}\) of the form

\[
 F=f+x_0G,qquad G\in
 H^0(\mathbf P^{d+1},\mathcal O(e-1)). \tag{4}
\]

This linear family has base locus \(Y\). At a smooth point of \(Y\),
the tangential differential \(df\) is nonzero, so every member is smooth
there. At a marked node \(p_i\), choose \(G(p_i)\ne0\); then

\[
 dF_{p_i}=G(p_i)\,dx_0, \tag{5}
\]

so \(X=(F=0)\) is smooth at \(p_i\) and

\[
 T_{p_i}X=\Lambda. \tag{6}

\]

Outside the base locus, S079 Bertini makes a general member of (4)
smooth. The conditions \(G(p_i)\ne0\) are simultaneous nonempty open
conditions, so a smooth such \(X\) exists. Equations (5)-(6) give

\[
 Z\subset\gamma_H^{-1}(\Lambda),\qquad |Z|=N. \tag{7}
\]

The construction changes \(X\) with \(N\). It does not construct the
required fiber on an arbitrary input variety, and it supplies none of
G146's central profile, relation, rational detector, specified pairing,
or later rungs.
