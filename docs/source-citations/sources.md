# Source records

## S001 - Official statement

Pierre Deligne, *The Hodge Conjecture*, official Clay Mathematics Institute
problem description. [Official PDF](https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf)

- Checked: pp. 1-2 define rational Hodge classes and state the conjecture for
  projective nonsingular varieties over \(\mathbf C\).
- Checked: p. 3 warns that projectivity cannot be weakened to Kahler and that
  Hodge's stronger integral/generalized forms fail.
- Checked: p. 4 distinguishes Hodge correspondences and motives from known
  algebraic cycles.
- Does not prove: the conjecture.
- Local retrieval SHA-256:
  `E308D945EA3CF5DAD8B187A06509013712C467B589039EB41B365CC4C988F0C8`.

## S002 - Algebraicity of Hodge loci

Eduardo Cattani, Pierre Deligne, Aroldo Kaplan, “On the locus of Hodge
classes,” *J. Amer. Math. Soc.* 8 (1995), 483-506.
[IAS record/PDF](https://publications.ias.edu/book/export/html/416),
[arXiv](https://arxiv.org/abs/alg-geom/9402009).

- Checked claim: for a polarized variation, the locus where a fixed integral
  class remains of type \((p,p)\) is algebraic (with the paper's precise
  bounded/polarized formulation).
- Does not prove: that the class is algebraic, or that a relative cycle space
  dominates the Hodge locus.
- Local retrieval SHA-256:
  `B420E56D738F0C04870E71DF4E4C5834926835AC3DF3A114655ED7CE2B008217`.

## S003 - Lefschetz standard conjecture and correspondences

Steven L. Kleiman, “Algebraic cycles and the Weil conjectures,” in *Dix
exposes sur la cohomologie des schemas* (1968), 359-386.
[Scanned article](https://www.jmilne.org/math/Documents/KleimanAlgebraicCycles.pdf)

- Seeded claim: standard conjecture \(B(X)\) asks for the relevant Lefschetz
  inverse operator to be induced by an algebraic correspondence.
- Does not prove: \(B(X)\) for arbitrary smooth projective varieties.

## S004 - Integral counterexamples

Michael Atiyah and Friedrich Hirzebruch, “Analytic cycles on complex
manifolds,” *Topology* 1 (1962), 25-45.
[DOI](https://doi.org/10.1016/0040-9383(62)90094-0)

- Seeded claim: topological K-theory operations obstruct the integral Hodge
  conjecture.
- Does not disprove: the rational Hodge Conjecture.

## S005 - Abelian varieties and absolute Hodge classes

Pierre Deligne (notes by J. S. Milne), *Hodge cycles on abelian varieties*,
in *Hodge Cycles, Motives, and Shimura Varieties*, LNM 900 (1982).
[Author-hosted text](https://jmilne.org/math/Documents/Deligne82_2011.pdf)

- Checked distinction: Hodge classes on abelian varieties are absolute Hodge.
- Does not prove: all such classes are algebraic. Therefore it is not the
  rational Hodge Conjecture for arbitrary abelian varieties.

## S006 - Hypersurfaces, periods, and Abel-Jacobi invariants

Phillip A. Griffiths, “On the periods of certain rational integrals: I, II,”
*Annals of Mathematics* 90 (1969), 460-541.
[Part I DOI](https://doi.org/10.2307/1970746)

- Seeded use: residue/Jacobian-ring control of primitive cohomology and period
  variation for hypersurfaces.
- Does not prove: that a Hodge-locus tangent vector or period relation is
  represented by an algebraic cycle.

## Citation policy for mechanisms not yet audited

## S007 - Variation, monodromy, and degeneration

Wilfried Schmid, “Variation of Hodge Structure: The Singularities of the
Period Mapping,” *Inventiones Mathematicae* 22 (1973), 211-319.
[DOI](https://doi.org/10.1007/BF01389674)

- Seeded use: asymptotic period maps, monodromy, and limiting Hodge-theoretic
  control near a degeneration.
- Does not prove: lifting of a limiting/special-fiber algebraic cycle to the
  original smooth fiber.

## S008 - Semiregularity and deformation of cycles

Spencer Bloch, “Semi-regularity and de Rham cohomology,” *Inventiones
Mathematicae* 17 (1972), 51-66.
[DOI](https://doi.org/10.1007/BF01390023)

- Seeded use: semiregularity maps can annihilate certain obstruction classes
  for deforming subvarieties/cycles.
- Does not prove: that every anchor cycle deforms along its entire Hodge locus,
  or that arbitrary cycles satisfy the needed semiregularity hypotheses.
- Relevance: this is the first primary source to audit deeply for G002.

## S009 - Admissible normal functions

Patrick Brosnan, Hao Fang, Zhaohu Nie, Gregory Pearlstein, “Singularities of
admissible normal functions,” *Inventiones Mathematicae* 177 (2009), 599-629.
[arXiv](https://arxiv.org/abs/0711.0964)

- Checked p. 2, Conjecture 1.2 and Theorem 1.3: for every even-dimensional
  smooth projective \(X\), universal non-torsion singularity of the admissible
  normal functions attached to primitive middle Hodge classes is equivalent
  to HC for all smooth projective varieties.
- Checked pp. 13-15, Proposition 5.11 and the perverse weak-Lefschetz setup:
  sufficiently high powers have nontrivial vanishing cycles. This is ambient
  information only.
- Checked pp. 15-16, Corollary 5.15: when vanishing cycles are nontrivial, the
  local singularity is exactly the restriction
  \(\sigma_p(\nu)=\zeta|_{X_p}\) in rational cohomology.
- Checked pp. 16-18, Lemma 6.2 and Theorems 6.5-6.6: the proof treats rational
  coefficients, reduces arbitrary HC to middle-dimensional
  perpendicularity, and proves the converse by resolving a detecting
  singular hyperplane, using mixed-Hodge strictness, and inducting on
  dimension.
- Coefficient guard: the integral non-torsion formulation in the introduction
  and the rational formulation in Section 6 agree for the official target
  after clearing denominators; no integral HC is asserted.
- Does not provide: an unconditional class-specific nonzero restriction or
  singularity. The equivalence is a terminal reformulation, not a solution.
- Local retrieval SHA-256:
  `B71C1EFBBBCB46BF639749D5384E7768FE557FA0E622E9D0667FAB3B84352668`.

## S010 - Reduction modulo primes and Tate classes

John Tate, “Algebraic cycles and poles of zeta functions,” in *Arithmetical
Algebraic Geometry* (Purdue, 1963), Harper & Row, 1965, 93-110.
[Bibliographic record](https://cir.nii.ac.jp/crid/1574231875534172544)

- Seeded use: formulation of the Tate-cycle/Frobenius bridge over finitely
  generated fields.
- Does not prove: the general Tate conjecture, nor lifting of cycles from a
  finite-field fiber to characteristic zero.

## S011 - Motives and motivated cycles

Yves Andre, “Pour une theorie inconditionnelle des motifs,” *Publications
Mathematiques de l'IHES* 83 (1996), 5-49.
[NUMDAM full record](https://www.numdam.org/item/PMIHES_1996__83__5_0/)

- Checked distinction: motivated cycles yield an unconditional semisimple
  category with good realization properties.
- Does not prove: motivated cycles are algebraic cycles in general. Replacing
  “algebraic” by “motivated” is therefore not the official Hodge Conjecture.

## S012 - Hypersurface special case

Steven Zucker, “The Hodge conjecture for cubic fourfolds,” *Compositio
Mathematica* 34 (1977), 199-209.
[NUMDAM article](https://numdam.org/item/CM_1977__34_2_199_0/)

- Checked theorem: the rational Hodge Conjecture holds for cubic fourfolds.
- Scope guard: smooth cubic fourfolds are one special family in dimension four;
  no reduction of arbitrary fourfolds to cubic fourfolds is supplied.

## S013 - Abelian special case

Sergei G. Tankeev, “Cycles on simple Abelian varieties of prime dimension,”
*Mathematics of the USSR-Izvestiya* 20 (1983), 157-171.
[MathNet article](https://www.mathnet.ru/eng/im1611)

- Checked theorem: HC holds for simple complex abelian varieties of prime
  dimension.
- Scope guard: not all abelian varieties, not arbitrary varieties, and not a
  global reduction mechanism.

## S014 - Relative Hilbert schemes

Alexander Grothendieck, “Techniques de construction et theoremes d'existence
en geometrie algebrique IV: les schemas de Hilbert,” *Seminaire Bourbaki*,
Expose 221 (1961), 249-276.
[NUMDAM article](https://numdam.org/book-part/SB_1960-1961__6__249_0/)

- Seeded use: representability and projectivity/properness of the relative
  Hilbert scheme for a projective family and fixed Hilbert polynomial.
- Does not prove: smoothness of the Hilbert scheme at an arbitrary cycle, or
  dominance over a Hodge locus.

## S015 - Intersection-theoretic functoriality

William Fulton, *Intersection Theory*, 2nd ed., Springer, 1998.
[Publisher record](https://doi.org/10.1007/978-1-4612-1700-8)

- Seeded use: proper pushforward, refined Gysin maps for regular embeddings,
  rational equivalence, and compatibility used in B001/G002.
- Does not prove: surjectivity of a cycle-class map for an arbitrary variety.

## S016 - Semiregular varieties and the variational bridge

Ananyo Dan and Inder Kaur, “Semi-regular varieties and variational Hodge
conjecture,” arXiv:1612.00754 (version dated 2018).
[arXiv record](https://arxiv.org/abs/1612.00754)

- Checked pp. 1-2: for a semiregular lci subscheme, infinitesimal preservation
  of the cycle's Hodge class is equivalent to lifting the subscheme; the paper
  attributes the bridge to Bloch and Buchweitz-Flenner.
- Checked Theorem 1.1: any smooth projective \(n\)-fold \(Z\) can be embedded
  as a semiregular subvariety of a suitable sufficiently high-degree smooth
  hypersurface in \(\mathbf P^{2n+1}\).
- Checked Remark 3.5: this yields a very special variational-Hodge case for
  the constructed hypersurface family.
- Does not prove: every Hodge class has an anchor, every anchor has a
  semiregular representative, or arbitrary-variety HC.
- Local retrieval SHA-256:
  `26C14D8DB3710D8905172901648D7DE19034565DD2DBEF41A39A2A3A46E33AAC`.

## S017 - General semiregularity, VHC, and Hilbert smoothness

Ragnar-Olaf Buchweitz and Hubert Flenner, “A semiregularity map for modules
and applications to deformations,” *Compositio Mathematica* 137 (2003),
135-210; author-revised arXiv text.
[arXiv record](https://arxiv.org/abs/math/9912245)

- Checked p. 36, Theorems 5.1-5.2: a horizontal Hodge class whose anchor is a
  relevant Chern-character component of an injectively semiregular sheaf or
  subspace remains algebraic on nearby fibers.
- Checked pp. 50-51, Theorems 7.8-7.9 and Corollary 7.10: injectivity of the
  semiregularity map yields smoothness of the appropriate Douady/Hilbert germ;
  the lci obstruction group specializes to \(H^1(N_{Z/X})\).
- Scope guard: the paper assumes the semiregular sheaf/subspace exists. It
  does not give such a representative for every algebraic or Hodge class.
- Local retrieval SHA-256:
  `C753D3C553F591ACB81172096B5FC68CAC2D6CC0CF5916E970419965BE9A5C79`.

## S018 - All-order relative obstruction theorem

Ziv Ran, “Semiregularity, obstructions and deformations of Hodge classes,”
*Annali della Scuola Normale Superiore di Pisa* 28 (1999), 809-820.
[NUMDAM article](https://www.numdam.org/item/ASNSP_1999_4_28_4_809_0/)

- Checked Theorem 0, pp. 809-810: for a connected codimension-\(p\)
  submanifold of a compact complex manifold, embedded obstructions lie in the
  kernel of the semiregularity map; in the Kahler case this also holds for
  obstructions relative to deformations of the ambient manifold along which
  the fundamental class remains of Hodge level \(p\).
- Checked quantifier: the detailed statement covers arbitrary Artin-local
  small extensions, not only first order or curvilinear extensions.
- Scope guard: injectivity is an extra hypothesis if one wants obstruction
  vanishing, and the theorem starts with an existing submanifold/cycle.
- Local retrieval SHA-256:
  `25A9CD82E38F5E32DCDEEB62DCDB49E85444D6138659C83B36D213353C65EB81`.

## S019 - Nodal-hypersurface equivalence and deformation obstruction

R. P. Thomas, “Nodes and the Hodge conjecture,” *Journal of Algebraic
Geometry* 14 (2005), 177-185.
[arXiv](https://arxiv.org/abs/math/0212216)

- Checked p. 1, Theorem 1.1: standard rational HC is equivalent to the
  statement that for every even-dimensional smooth projective \(X^{2n}\) and
  rational middle Hodge class \(A\), some high-degree nodal hypersurface
  \(D\subset X\) carries a middle homology class pushing forward to the
  Poincare dual of \(A\).
- Checked pp. 2-5: arbitrary codimension reduces to the middle statement, and
  a detecting nodal divisor implies HC by resolution and induction.
- Checked p. 6, Theorem 4.2: the converse construction assumes an algebraic
  representative, smooths it, and embeds the resulting \(Z^n\) in a
  high-degree hypersurface having only ordinary double points on \(Z\).
  Therefore this construction cannot be reused to produce \(D\) before
  algebraicity is known.
- Checked pp. 6-8, Section 5: the attempted nodal deformation route has
  obstruction in \(H^1(I_{\{p_i\}}(NH))\), with
  \(H^1(N_{Z/X})\) injecting into it via the displayed Koszul resolution.
  Raising the degree does not automatically kill the original cycle
  obstruction.
- Does not provide: a construction of a detecting nodal divisor directly
  from an arbitrary Hodge class.
- Local retrieval SHA-256:
  `D10590F93E62D31DCF3FAE4571CB8C2E167666D7A141FC57FB8D3C57B1551D86`.

## S020 - Cohomological defect of desingularized nodal hypersurfaces

Chad Schoen, “Algebraic cycles on certain desingularized nodal
hypersurfaces,” *Mathematische Annalen* 270 (1985), 17-27.
[GDZ scan](https://gdz.sub.uni-goettingen.de/id/PPN235181684_0270?tify=%7B%22pages%22%3A%5B23%5D%2C%22view%22%3A%22info%22%7D)

- Checked pp. 17-20, Lemma 1.1, Corollary 1.2, and Proposition 1.3: for a
  nodal hypersurface in a smooth projective variety of even dimension and the
  indicated blowups, the new middle cohomology is isolated as an excess
  summand; under the displayed coherent-vanishing hypotheses that summand is
  computed by a node-defect group
  \(H^1(P,I_S\otimes\omega_P(mX))\).
- Scope guard: this is a theorem for the stated nodal hypersurface/blowup
  geometry. It neither constructs a defect for an arbitrary Hodge class nor
  reduces arbitrary smooth projective varieties to this special setting.
- Local retrieval SHA-256:
  `D792CF24C67E36E2907E18BFBBE9F0A1A91CF224EE76BB8F617DEA13F6EA74E5`.

## S021 - Vanishing-cycle relations and singularities of normal functions

Mark Green and Phillip Griffiths, “Algebraic cycles and singularities of
normal functions I,” in *Algebraic Cycles and Motives*, London Mathematical
Society Lecture Note Series 343 (2007), 206-263.
[IAS author PDF](https://publications.ias.edu/sites/default/files/acycles1%28609%29.pdf)

- Checked Section 4.2.3, pp. 14-15: under the local or quasi-local
  normal-crossing hypotheses, the monodromy complex \(B^\bullet\) computes the
  relevant local intersection cohomology, and the rational singularity group
  injects into \(H^1(B^\bullet)\).
- Checked Section 4.2.4, pp. 18-22: for a transverse nodal model whose nodes
  impose independent smoothing conditions, \(H^1(B^\bullet)\) is the rational
  relation space among the vanishing cycles. The stated partition variant
  permits \(I=J\sqcup K\) with each part independent.
- Scope guard: a nonzero relation space is only a possible singularity
  channel. It does not prove that a specified Hodge class maps nontrivially
  into it. The paper's constructions from a subvariety \(W\) already assume
  an algebraic cycle and cannot be used circularly for G006.
- Local retrieval SHA-256:
  `4D1DB080F19E77E4627462C7684F822CE1E18EFD783E0D00ABA65BEE7DDB61A0`.

## S022 - Exact local relation-pairing criterion

Morihiko Saito, “Generalized Thomas hyperplane sections and relations between
vanishing cycles,” arXiv:0806.1461v5 (2008).
[arXiv record](https://arxiv.org/abs/0806.1461)

- Checked pp. 2-3, Proposition 1 and Theorem 1: the degeneration exact
  sequence defines the extra cohomology \(E(Y_0)\) and the unipotent
  type-\((0,0)\) relation space \(R(Y_0)_1^{(0,0)}\); these are dual, and a
  relation \(\beta\) gives a primitive Hodge class \(\gamma_\beta\) such that
  \(Y_0\) detects \(\zeta\) exactly when
  \(\langle\zeta,\gamma_\beta\rangle\ne0\) for some \(\beta\).
- Checked pp. 3 and 8-9, Theorems 2-3 and Section 2.5: the result extends via
  vanishing-cycle mixed Hodge modules to non-isolated singularities; for
  ordinary double points the local vanishing group is \(\mathbf Q(-n)\) with
  unipotent monodromy; the relative-cycle/retraction construction of
  \(\gamma_\beta\) is explicit.
- Scope guard: the theorem characterizes a chosen singular member but does
  not produce one for an arbitrary Hodge class.
- Local retrieval SHA-256:
  DC4C2308EBA568BE14BF5027D8110ECC4FF428261E436499E4DD2AE016ACDA12.

## S023 - Global tube generation of primitive cohomology

Christian Schnell, “Primitive cohomology and the tube mapping,”
*Mathematische Zeitschrift* 268 (2011), 1069-1089.
[DOI and author PDF](https://www.math.stonybrook.edu/~cschnell/pdf/papers/tube.pdf)

- Checked pp. 1-3, Theorem 1: for a smooth projective embedded \(d\)-fold with
  nonzero rational vanishing homology in a smooth hyperplane section, the
  tube map from pairs \((g,\alpha)\), with \(g\) a monodromy loop and
  \(g\alpha=\alpha\), surjects onto \(H^d_{\mathrm{prim}}(X,\mathbf Q)\).
  Dually, the map to the product of coinvariant quotients
  \(V/(g-1)V\) is injective.
- Checked p. 20, Section 6: the dual formulation detects every primitive
  class by a cohomology class on the global étale space of vanishing cycles.
- Scope guard: tube classes are global topological cycles swept through
  smooth hyperplane sections. The theorem does not support them on a single
  singular hyperplane, make them algebraic, or identify
  \(\ker(g-1)\) with Saito's local relation kernel.
- Local retrieval SHA-256:
  38AF760A171C9373EFA0232768D8C24D5FB2F5409DFEE63646DD5CB3E55310EE.

## S024 - Global and local singularities of primitive classes

Mark Andrea de Cataldo and Luca Migliorini, “A remark on singularities of
primitive cohomology classes,” *Proceedings of the American Mathematical
Society* 137 (2009), 3593-3600.
[Author PDF](https://www.math.stonybrook.edu/~mde/MyPublishedPapers/SingularitiesOfPrimitiveClasses.pdf),
[DOI](https://doi.org/10.1090/S0002-9939-09-10014-X).

- Checked p. 5, Definition 3.3 and Remark 3.4: the global class
  \(s(\zeta)\) lies in
  \(IH^1(\mathbf P^d,IC(R^{2n-1}))\), the local class \(s(\zeta)_p\) lies in
  the corresponding perverse stalk, and its nonzero locus has codimension at
  least two.
- Checked pp. 5-6, Propositions 3.6 and 3.8: a primitive class is zero if and
  only if its global Green-Griffiths invariant is zero; after embedding by
  \(mL\), \(m\gg0\), the local invariant detects the canonical local
  restriction component.
- Checked pp. 6-7, Corollaries 3.10 and 3.12: for a primitive Hodge class the
  local invariant vanishes exactly when its restriction to the singular
  hyperplane vanishes in intersection cohomology; it can also be tested on
  the smooth part over a contractible punctured neighborhood.
- Scope guard: nonzero global invariant does not in the paper imply a
  nonzero local invariant. Nonemptiness of the local singularity locus for
  every primitive Hodge class is the Thomas/Hodge-conjecture condition.
- Local retrieval SHA-256:
  `A3801E1017A87B747DE2F7053D4EDCDB035B07F14382B48F5096B6C6950DA5DC`.

## Citation policy for incompletely audited mechanisms

Spreading out, products/fibrations, and cycle-class rigidity remain recorded
only at the mechanism/obstruction level. Before any dependent brick is
promoted, its exact primary theorem must receive a new `S...` record with
matching field, coefficients, cohomology, and scope. Seeded sources above must
likewise be upgraded to page/theorem-level checks before decisive use.
