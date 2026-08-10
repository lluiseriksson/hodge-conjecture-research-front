# Formalization boundary

Status: **EXPLORATORY**.

The first realistic formal target is B001's projective-space degree bookkeeping
and the compatibility equations for pullback/pushforward of cycle classes.
Formalizing the full conjecture would require substantial algebraic-geometry
and Hodge-theory infrastructure not presently claimed here.

B007 adds a second stable boundary. Its denominator-clearing lemma and the
logical composition

\[
\text{universal local nonvanishing}\Longrightarrow
\text{middle perpendicularity}\Longrightarrow\text{HC}
\]

are realistic abstract interfaces. The decisive inputs - mixed Hodge modules,
local intersection cohomology, resolution with top-weight strictness, and the
BFNP singularity calculation - are not present in the current formal
toolchain. They must be imported only as explicitly named external theorems,
never replaced by a project-local axiom that silently asserts G005.

B008-B009 add a finite-dimensional formal boundary: one can model the
vanishing-cycle map \(\mathbf Q^r\to V\), its kernel, and the class-specific
linear functional on that kernel. Formalizing this linear algebra would check
the implication “nonzero pairing implies nonzero local class” and the NG-009
warning that a nonzero domain alone proves nothing about a fixed functional.
It would not formalize the imported geometric identification of local
intersection cohomology with that kernel, nor prove the open nonvanishing in
G006.

B010 supplies a stable abstract interface

\[
 R(Y_0)_1^{(0,0)}\simeq E^\vee(Y_0)^{(0,0)},\qquad
 \zeta|_{Y_0}\ne0\Longleftrightarrow
 \exists\beta,\ \langle\zeta,\gamma_\beta\rangle\ne0.
\]

B011 adds the global tube-surjectivity interface. A useful formal diagnostic
would keep \(\ker(g-1)\) and the local relation kernel as distinct types, so
that the invalid coercion in NG-010 is impossible. The geometric
global-to-local concentration required by G007 must not be introduced as an
axiom under a generic “monodromy relation” name.

B012 adds a second type separation:

\[
 s(\zeta):IH^1(\mathbf P^d,IC(V))
 \qquad\text{versus}\qquad
 s(\zeta)_p:\mathcal H^{-d+1}(IC(V))_p.
\]

A formal interface must not coerce global hypercohomology nonvanishing into
local-stalk nonvanishing. B013's telescoping relation is realistic finite
linear algebra to formalize, but its output type must remain a distributed
relation indexed by distinct meridians, not Saito's one-fiber relation type.
The open G008 support realization must never enter as a generic sheaf lemma.

B014 makes this guard executable at the specification level: an elliptic
curve has nonzero \(IH^1\) for its constant intersection complex while the
degree-\((-\dim+1)\) ordinary cohomology sheaf vanishes everywhere. A typed
formalization can prove this countermodel using shifts and
\(H^1(E,\mathbf Q)\ne0\). B015 can be exposed only as a conditional geometric
interface whose input includes a chosen nodal hyperplane and the explicit
independence condition \(H^1(I_{\Delta,X}(1))=0\).

B016 is a realistic finite-dimensional formalization target. Given a perfect
pairing \(H\times H^\vee\to\mathbf Q\), a family of detector vectors spans
\(H^\vee\) if and only if every nonzero vector of \(H\) pairs nontrivially
with some detector. This lemma can be kernel-checked without importing open
geometry. G009 must remain an explicit hypothesis about the geometric
detector family; no formal span axiom may assert it.

B017 is the corresponding finite-dimensional ascending-chain lemma. A formal
version may prove stabilization and extraction of a finite basis from a full
union. It must expose the stabilization index as non-effective and must not
invent comparison maps between the geometric detector families at distinct
polarization powers.

B018 is another stable formal target: from
\(\ell\cup\zeta=0\), derive
\(\langle\zeta,c\ell^n\rangle=0\) by associativity of cup product. This may
be formalized independently of the open detector geometry and used as a type
guard preventing tautological complete intersections from inhabiting the
primitive detector interface.

B019 adds a type-level separation suitable for formal interfaces: a matching
path has two distinct critical endpoints and returns an ambient Lagrangian
sphere, whereas a Saito detector takes one singular fiber and a vector in its
vanishing-cycle relation kernel. No coercion between these types is valid
without an explicit algebraic collision morphism and Hodge-compatibility
proof.

B020 adds an elementary executable guard. In a skew pairing, vectors
\(\delta_1,\delta_2\) with \((\delta_1,\delta_2)=1\) are linearly
independent; hence they cannot inhabit a nonzero two-generator relation
kernel. Formalizing this fact would not construct relations at other
multi-node members.

B021 composes the B019 and B020 guards: an equal-up-to-sign pair has span of
rank at most one, so no linear class-preserving map can identify it with an
intersection-one pair of rank two. The theorem must remain scoped to the
audited projective-surface comparison; it is not a formal obstruction to
higher-dimensional collision mechanisms with additional cycles.

B022 supplies the correct typed pipeline for a thimble model:

\[
 \ker\partial\to
 \ker\partial/\operatorname{im}\tau_\infty\to
 H_n(X)/\iota_*H_n(X_b).
\]

A formal interface must not coerce a boundary-kernel element directly into
ambient homology. It must expose the equator quotient and the base-locus
kernel \(K\), and separately require nonvanishing in the final quotient.

B023 is finite algebra: an isomorphism of commutative boundary-map squares
induces an isomorphism of kernels. This can be kernel-checked, while Seidel's
geometric assertion that Hurwitz moves yield the required isomorphisms
remains an imported theorem. A topology-changing collision must have a
different, explicitly non-invertible interface.

B024 is another finite-dimensional consequence once the imported exact
sequence \(\mathcal T(Y)\twoheadrightarrow PH_n(X)\) is exposed: a nonzero
functional on primitive homology pulls back to a nonzero functional on the
thimble quotient. The formal conclusion type must remain “global topological
detector”; it cannot be coerced to an algebraic cycle or local Saito
detector.

Rules:

- no `sorry`, admitted theorem, or project-local axiom may carry open
  algebraicity content on a stable branch;
- conditional interfaces must expose every hypothesis in their type;
- a kernel-checked implication from an explicit hypothesis package is labeled
  `CONDITIONAL`, not `FORMALLY VERIFIED` as a solution of that hypothesis;
- toolchain version and theorem inventory must accompany any future code.
