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
- Checked p. 22 visually: the partition statement follows the universal
  local-deformation discussion in which nodes are independently smoothed and
  the parameter slice meets the partial-node strata. Thus “independent” here
  is a condition on accessible node-smoothing directions, not merely linear
  independence of the resulting vanishing cycles.
- Checked pp. 18-19, the six-invariant theorem: for \(L\gg0\), the dimensions
  of the vanishing-cycle relation space, the primitive ambient image, the
  failure of the nodes to impose independent conditions on
  \(H^0(K_X\otimes L^n)\), two desingularization defects, and
  \(H^1(B^\bullet)\) are equal. The coherent defect is displayed as
  \(h^1(I_\Delta\otimes K_X\otimes L^n)\).
- Checked p. 19: the construction of a one-dimensional generating relation
  from hypersurfaces containing a smooth codimension-\(n\) subvariety starts
  with that already-algebraic subvariety. It cannot be used to select the
  relation for an arbitrary Hodge class without circularity.
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
- Checked author-PDF pp. 12-13, Section 3.4 and Lemma 6: when
  \(d=\dim X\) is even, Schnell constructs vanishing cycles
  \(\delta_1,\delta_2\) with intersection number one. In a general plane
  section of the dual variety, a node corresponds to a hyperplane with two
  ordinary double points, while a cusp corresponds to one singularity of
  Milnor number two; the cusp supplies the intersection-one pair. This pair
  is linearly independent, not a local relation.
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

## S025 - Intersection cohomology on independent-node Severi strata

Vincenzo Di Gennaro and Davide Franco, “Intersection cohomology and Severi's
varieties,” arXiv:2011.14854 (2020); revised as “Intersection Cohomology and
Severi Varieties,” in *The Art of Doing Algebraic Geometry*, Trends in
Mathematics, Birkhäuser, 2023, 145-160.
[arXiv record](https://arxiv.org/abs/2011.14854),
[published chapter DOI](https://doi.org/10.1007/978-3-031-11938-5_6).

- Checked p. 5, Theorem 3.2: if the \(\delta\) nodes of a hyperplane section
  impose independent conditions, the local dual discriminant has
  normal-crossing branches and every \(r\)-node partial-smoothing stratum is
  nonempty, smooth, and of dimension \(N-r\).
- Checked pp. 7-8, Theorem 4.3: the local intersection complex is computed by
  the normal-crossing monodromy complex, is concentrated in degrees zero and
  one, and its degree-one term fits into the stated exact sequence with
  \(R^{2n}\pi_*\mathbf Q\).
- Checked p. 9, Corollary 4.5 and Remark 4.6: the degree-one term is the
  primitive local restriction channel; for projective-space ambient variety
  its dimension is the nodal defect.
- Scope guard: every result begins with a chosen nodal hyperplane whose nodes
  impose independent conditions. The paper does not construct a hyperplane
  detecting a specified primitive Hodge class and does not prove that a
  nonzero possible channel receives that class nontrivially.
- Local retrieval SHA-256:
  7F74A3068E8DFC9D8CF8C2261314EEE18433E3140B00BE4B842AC57CB4E32374.

## S026 - Boundary-class program for singular loci

Mark Green and Phillip Griffiths, “Algebraic cycles and singularities of
normal functions, II,” in *Inspired by S. S. Chern*, Nankai Tracts in
Mathematics 11 (2006), 179-268.
[IAS record and PDF](https://publications.ias.edu/node/272),
[publisher DOI](https://doi.org/10.1142/9789812772688_0009).

- Checked pp. 1 and 6-9: the proposed rational maps to partially compactified
  Hodge-theoretic classifying spaces pull selected boundary components back
  to singular loci locally. For a specified primitive Hodge class, the nodal
  model used in the construction is obtained after assuming HC and writing
  \(k_0\zeta=[W-H]\).
- Checked pp. 7-8: nonzero pullback of a boundary fundamental class is
  proposed as a topological route to nonempty inverse image. The
  class-dependent map is studied on the Noether-Lefschetz locus, and the
  discussion explicitly sets aside noncompactness issues and describes the
  results as preliminary.
- Checked p. 95, conclusions (5)-(8): the expected cycle-level formula
  contains an unspecified correction term, and defining the needed universal
  Jacobian compactification and boundary components is listed as a major
  remaining issue.
- Scope guard: this is a boundary-geometry research program, not an
  unconditional proof of singular-locus nonemptiness. Its class-directed
  nodal construction assumes an algebraic representative via HC.
- Local retrieval SHA-256:
  D75371126D39CB89EC6DC1AB533654D3F8FA96DA081BC9C8EF2BC5BE9A2FAF3A.

## S027 - Matching paths and Lagrangian spheres

Denis Auroux, “The canonical pencils on Horikawa surfaces,”
*Geometry & Topology* 10 (2006), 2173-2217.
[Journal PDF](https://msp.org/gt/2006/10-4/gt-v10-n4-p04-p.pdf),
[DOI](https://doi.org/10.2140/gt.2006.10.2173).

- Checked p. 2173: title, author, publication scope, and the fact that the
  paper studies the canonical Lefschetz pencils of two particular Horikawa
  surfaces.
- Checked pp. 2214-2215, Definition 8.1 and Question 8.2: in the
  four-dimensional setting, a matching path is an embedded arc with two
  critical endpoints whose two transported vanishing cycles are isotopic in
  the smooth midpoint fiber. Gluing the thimbles gives an embedded
  Lagrangian sphere. The construction is explicitly symplectic and is
  formulated across two critical values, not as simultaneous nodes of one
  singular fiber.
- Checked pp. 2214-2215: repeated Dehn twists yield basic matching paths,
  while the attempted “exotic” relations in the Horikawa examples can lead
  only to immersed paths/spheres. The paper itself asks how to algebraize the
  embedded-versus-immersed distinction.
- Scope guard: the result does not identify a matching sphere with a Saito
  relation class at one algebraic hyperplane, assert Hodge type, or construct
  an algebraic cycle on an arbitrary smooth projective variety. The audited
  theorem is four-dimensional and the examples are a special family.
- Local retrieval SHA-256:
  B2857F36D1059F55F160B6D6058EA7F4E7E10EECE2F885913F59432E8A55775E.

## S028 - Hurwitz equivalence of distinguished vanishing-cycle bases

Paul Seidel, “Vanishing cycles and mutation,” in *European Congress of
Mathematics, Vol. II (Barcelona, 2000)*, Progress in Mathematics 202,
Birkhäuser, 2001, 65-85.
[arXiv record and PDF](https://arxiv.org/abs/math/0007115).

- Checked p. 1: for an exact Morse fibration over a disk, vanishing paths
  determine a distinguished basis and any two such bases are connected by a
  sequence of Hurwitz moves.
- Checked pp. 4-5, Definition 2.1: changing paths acts through isotopies,
  symplectomorphisms, and Dehn twists; Hurwitz equivalence is generated by
  the displayed moves and their inverses. The equivalence class is an
  invariant of the fixed exact Morse fibration.
- Scope guard: the theorem concerns invertible changes of distinguished
  basis in a fixed symplectic fibration. It does not describe a
  topology-changing collision, preserve a Hodge filtration, or construct an
  algebraic cycle.
- Local retrieval SHA-256:
  4A99AC13F173D1FBD826F0F5FE7B78EF785C048C11EFF4A7BABCDD77CDFC6075.

## S029 - Relative thimbles and ambient homology quotient

Pierre Lairez, Eric Pichon-Pharabod, and Pierre Vanhove, “Effective homology
and periods of complex projective hypersurfaces,” *Mathematics of
Computation* 93 (2024), 2985-3025.
[arXiv record and PDF](https://arxiv.org/abs/2306.05263),
[published DOI](https://doi.org/10.1090/mcom/3947).

- Checked p. 1: the paper's scope is smooth complex projective hypersurfaces
  and Picard-Lefschetz reconstruction of their singular homology.
- Checked p. 7, Section 2.1.4 and Lemma 1: the Lefschetz thimbles
  \(\Delta_i\) freely generate \(H_n(Y_+,X_b)\), all other relative degrees
  vanish, and \(\partial\Delta_i=\delta_i\).
- Checked pp. 7-9, equation (12) and Theorem 2: zero-boundary thimble
  combinations must be quotiented by the equator-extension image to form
  \(\mathcal T(Y)\). The two exact sequences then identify a further kernel
  \(K=\ker(H_{n-2}(X')\to H_{n-2}(X_b))\) before projection to ambient
  middle homology modulo the reference-fiber image.
- Checked p. 10, equation (19) and Theorem 4: for a smooth projective
  complete intersection, the second exact sequence becomes
  \(0\to K\to\mathcal T(Y)\to PH_n(X)\to0\), and the middle homology of the
  blowup splits noncanonically into the thimble, reference-fiber, and
  lower-fiber summands.
- Scope guard: these are exact topological statements despite the paper's
  computational goal. Numerical period calculations are not used as
  evidence of algebraicity. The theorem is for generic pencils in the
  smooth hypersurface setting and supplies no Hodge-type or algebraic-cycle
  conclusion.
- Local retrieval SHA-256:
  A270214FEC7C34957C0F21EBD17481F05F8A903D97FA06DB29EE030A9553FA0F.

## S030 - Distinguished bases of isolated hypersurface singularities

Egbert Brieskorn, “Die Monodromie der isolierten Singularitäten von
Hyperflächen,” *Manuscripta Mathematica* 2 (1970), 103-161,
[DOI](https://doi.org/10.1007/BF01155695),
[archival record and PDF](https://www.mathnet.ru/eng/mat608).

Wolfgang Ebeling, “Distinguished bases and monodromy of complex
hypersurface singularities,” arXiv:1905.12435 (2019),
[arXiv record and PDF](https://arxiv.org/abs/1905.12435).

- Checked p. 1: the survey treats monodromy and distinguished bases for
  isolated complex hypersurface singularities and records the classical
  theorems with their original attributions.
- Checked pp. 3-4: the Milnor fiber has the homotopy type of a bouquet of
  \(\mu\) middle-dimensional spheres, so its Milnor lattice is free of rank
  \(\mu\); a morsification has \(\mu\) nondegenerate critical points with
  distinct critical values.
- Checked p. 9, Theorem 3 (attributed there to Brieskorn) and Corollary 4:
  the vanishing cycles associated to a distinguished, respectively weakly
  distinguished, system form a basis of the Milnor lattice.
- Checked Brieskorn's appendix in the accessible Russian translation,
  printed pp. 156-159: the morsification argument proves that the middle
  homology rank equals the number \(b=\mu\) of Morse points; the supplement
  on p. 159 states that the transported integral vanishing cycles
  \(e_1,\ldots,e_b\) generate \(H_n(F_0,\mathbf Z)\). Since the group is free
  of rank \(b\), these \(b\) generators form an integral basis.
- Scope guard: this is a local topological basis theorem, not a theorem that
  the local Milnor lattice injects into a projective nearby fiber. It gives
  no Hodge type and no algebraic cycle. Its role is to exclude an internal
  relation among a complete morsification basis; global relations may still
  occur through a noninjective local-to-global map.
- Original Brieskorn retrieval SHA-256:
  E1924926E45A01B37397D3499B1D6CB825D783B4323168842B878A10028D5B2D.
- Ebeling survey retrieval SHA-256:
  26897DDDAFE02DF6A9C4EDA949057802C7BFA1BDF4847B8BB81947CA15E03642.

## S031 - Minimum partition of a matroid

Jack Edmonds, “Minimum Partition of a Matroid Into Independent Subsets,”
*Journal of Research of the National Bureau of Standards B* 69B (1965),
67-72. [NIST archival PDF](https://nvlpubs.nist.gov/nistpubs/jres/69B/jresv69Bn1-2p67_A1b.pdf),
[DOI](https://doi.org/10.6028/jres.069B.004).

- Checked p. 67: the abstract defines matroid rank and states the partition
  criterion in full.
- Checked p. 69, Theorem 1: a matroid ground set can be partitioned into at
  most \(k\) independent sets if and only if no subset \(S\) satisfies
  \(|S|>k r(S)\).
- Checked pp. 70-71: the proof reduces to spans and circuits and constructs
  the partition by a finite exchange process; p. 72 records the graph
  corollary and references.
- Scope guard: this theorem resolves only the finite combinatorial partition
  question. It does not construct a node scheme, establish an adjoint defect,
  compare coherent and rational relation vectors, or prove a Hodge pairing.
- Local retrieval SHA-256:
  864357675B91B552E899A2CCEE434A4A28D04749B2FF629DC4BFD49D317A4440.

## S032 - Plane-containing nodal hypersurfaces with defect

Remke Kloosterman, “Maximal families of nodal varieties with defect,”
*Mathematische Zeitschrift* 300 (2022), 1141-1156.
[Open-access article](https://link.springer.com/article/10.1007/s00209-021-02814-7),
[arXiv manuscript](https://arxiv.org/abs/1310.0227),
[DOI](https://doi.org/10.1007/s00209-021-02814-7).

- Checked the abstract and Theorem 1.1: a degree-\(d\) nodal hypersurface in
  \(\mathbf P^4\) with positive defect has at least \((d-1)^2\) nodes, with
  equality forcing a contained plane.
- Checked manuscript p. 8 visually: hypersurfaces containing a fixed plane
  have the form \(\ell_1f_1+\ell_2f_2\), \(\deg f_i=d-1\), and a general
  member is nodal; this is the maximal-dimensional defect family in the
  stated setting.
- B030 specializes to \(d=5\) and supplies its own transverse Hessian and
  Koszul calculations. The source does not assert the two-part matroid
  partition or a class-specific Hodge pairing.
- Local retrieval SHA-256:
  1200097775A38569C4250703ED83F983FEA236D348A2C39EDA414E3D2A7B2FC4.

## Citation policy for incompletely audited mechanisms

Spreading out, products/fibrations, and cycle-class rigidity remain recorded
only at the mechanism/obstruction level. Before any dependent brick is
promoted, its exact primary theorem must receive a new `S...` record with
matching field, coefficients, cohomology, and scope. Seeded sources above must
likewise be upgraded to page/theorem-level checks before decisive use.
