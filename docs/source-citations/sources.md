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
- The proof of Theorem 4.2 identifies the singular points with the simple
  transverse zeros of the first normal derivative in
  \(N^*_{Z/X}\otimes\mathcal O_X(N)|_Z\), uses Bertini away from \(Z\), and
  invokes the local criterion that a simple zero of the differential gives
  an ordinary double point. B032 verifies this normal-jet mechanism directly
  for the diagonal in \(\mathbf P^2\times\mathbf P^2\).
- Rechecked the displayed Theorem 4.2 proof for B034: it states that the
  number of nodes of the generic fixed-carrier hypersurface is exactly
  \(c_n(N^*_{Z/X}(NH))\). B034 combines this primary statement with
  asymptotic Riemann-Roch to obtain the \(n!\) block-capacity obstruction.
  Thomas makes no claim that these nodes split into two independently
  smoothable blocks.
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
- Proposition 1.3 is a proved canonical isomorphism from that coherent group
  to the desingularized excess space. It does not identify this space with
  the image in primitive homology of the original smooth ambient variety.
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
- Rechecked pp. 20-22 for G015. The displayed local complex includes
  degree-two pairwise terms
  \(\bigoplus_{i<j}N_iN_jV\), while the final “general result” is stated only
  for the bipartition \(I=J\sqcup K\). No multipart theorem or induction is
  stated. The preceding blow-up example changes the boundary monodromy
  operators, so a \(q\)-block extension must recompute the resolved local
  complex rather than count relations before resolution.
- Checked p. 22 visually: the partition statement follows the universal
  local-deformation discussion in which nodes are independently smoothed and
  the parameter slice meets the partial-node strata. Thus “independent” here
  is a condition on accessible node-smoothing directions, not merely linear
  independence of the resulting vanishing cycles.
- Rechecked Section 4.3.2, pp. 23-24 for B038. The paper writes the
  logarithmic subcomplex with differential
  \(\sum_i(df_i/f_i)N_i\), displays its residue map to the monodromy complex,
  and states that the infinitesimal invariant maps to the singularity class
  under this residue morphism. B038 combines this explicit primary formula
  with the standard logarithmic residue sequence on the exceptional
  \(\mathbf P^1\); it does not import a multipart theorem from the paper.
- For B042, the same normal-crossing logarithmic complex is applied after
  blowing up a uniform rank-three arrangement. The new global calculation
  uses the self-contained SNC residue sequence on \(\mathbf P^2\): the
  extension class of the \(i\)-th residue summand is
  \(c_1(\mathcal O(L_i))\), so constants map to
  \(\sum_i c_i[L_i]\). No higher-rank theorem is imported from S021.
- B043 observes that this residue calculation is dimension-independent for
  a simple uniform arrangement: after one blow-up the exceptional divisor is
  \(\mathbf P^{d-1}\), every branch residue has the same hyperplane class,
  and the degree-one connecting morphism is still the sum of residues. The
  uniform SNC and direct-image arguments are proved inside B043.
- B044 uses the same SNC residue morphism on
  \(\operatorname{Bl}_p\mathbf P^2\), but the two divisor-class components
  and the coefficient (W_F\) on the new exceptional curve are computed
  inside B044; they are not asserted by S021.
- Checked pp. 18-19 visually and against OCR: the paper explicitly defines
  \(\rho(ii)\) as the dimension of the image of
  \(H_{2n}(X_{s_0})\to H_{2n}(X)_{\mathrm{prim}}\), alongside relations,
  adjoint evaluation defect, two desingularization defects, and
  \(H^1(B^\bullet)\), and then prints equality of all six.
- Checked p. 2: the authors explicitly describe the document as an extended
  research announcement of work in progress and state that complete details
  of some results had not yet been written. The displayed six-invariant
  theorem is stated without a proof there, so it is not used as a sole source
  for any comparison that can be triangulated with Saito, Schoen, or
  Di Gennaro–Franco.
- Source-conflict guard: B031's general plane-containing nodal
  degree-\(d\) hypersurface in \(\mathbf P^4\) has one-dimensional relation
  and extra homology for arbitrarily large \(d\), while the displayed
  primitive ambient target is zero. The literal
  \(\rho(i)=\rho(ii)\) component is therefore quarantined as NG-028 pending
  a documented correction or different definition. B026 imports only the
  non-\(\rho(ii)\) defect comparisons.
- A targeted primary-literature search on 2026-08-10 located no erratum or
  later correction of \(\rho(ii)\). S033 revisits a related normal-function
  comparison but does not resolve this nodal numerical conflict.
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
- Checked displayed maps (0.4)-(0.5) and the proof in Section 2.4: the
  relation first determines an element of \(E^\vee(Y_0)\), followed by a
  canonical morphism
  \(E^\vee(Y_0)\to H_{2n}(X,\mathbf Q(n))_{\mathrm{prim}}\) obtained from the
  Lefschetz decomposition. No injectivity assertion is made for this second
  map; B031 gives an explicit zero-target instance.
- Checked pp. 3 and 8-9, Theorems 2-3 and Section 2.5: the result extends via
  vanishing-cycle mixed Hodge modules to non-isolated singularities; for
  ordinary double points the local vanishing group is \(\mathbf Q(-n)\) with
  unipotent monodromy; the relative-cycle/retraction construction of
  \(\gamma_\beta\) is explicit.
- Rechecked Section 1.4, especially formula (1.4.1) and Proposition 1.7, for
  B040. In a normal-crossing polydisk, the degree-one IC stalk is computed by
  Saito's image-of-monodromy subcomplex in mixed Hodge modules. If
  \(N_iN_j=0\) and every \(\operatorname{Im}N_i\subset H(-1)\) is a sum of
  one-dimensional mixed Hodge structures, Proposition 1.7 proves that the
  dimension of its \((0,0)\) Hodge classes equals the full degree-one
  dimension. B040 applies this only at the resolved two-branch crossings.
- B042 applies the same proposition at the two- and three-component strata
  of the resolved \(U_{3,r}\) divisor. The hypothesis \(N_iN_j=0\) is checked
  directly from the zero mutual intersections of distinct-node vanishing
  cycles; the source is not used for the global incidence or direct-image
  calculation.
- B043 applies Proposition 1.7 at arbitrary-depth SNC strata, but only after
  the uniform-matroid geometry proves that at most \(d\) total boundary
  components meet and all pairwise logarithm products vanish.
- Rechecked the proof of Theorem 3 in Section 2.7. The unipotent nodal
  vanishing cohomology is one-dimensional and pure of weight \(2n\), hence
  \(\mathbf Q(-n)\); after the \(\mathbf Q(n)\) normalization used in the
  relation complex, the generator is \(\mathbf Q(0)\).
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
- Checked manuscript p. 7 visually, Proposition 3.7: the defect of a nodal
  hypersurface is the failure of its nodes to impose independent conditions
  in the displayed adjoint degree; for a degree-\(d\) hypersurface in
  \(\mathbf P^4\), that degree is \(2d-5\).
- Checked pp. 7-8: a general degree-\(d\) hypersurface containing a fixed
  plane has equation \(\ell_1f_1+\ell_2f_2\) and is nodal. B031 combines
  this with the \((d-1,d-1)\) plane Koszul resolution and Proposition 3.7
  to obtain defect one in every degree \(d\ge3\).
- B030 specializes to \(d=5\) and supplies its own transverse Hessian and
  Koszul calculations. The source does not assert the two-part matroid
  partition or a class-specific Hodge pairing.
- Local retrieval SHA-256:
  1200097775A38569C4250703ED83F983FEA236D348A2C39EDA414E3D2A7B2FC4.

## S033 - Later Green-Griffiths singularity comparison

Mark Green and Phillip Griffiths, “Singularities of the infinitesimal
invariant of normal functions,” *Rendiconti Lincei. Matematica e
Applicazioni* 36 (2025), 513-529; published online 14 February 2026.
[Official open-access PDF](https://content.ems.press/assets/public/full-texts/serials/rlm/36/3/14299507/online/10.4171-rlm-1080.pdf),
[DOI](https://doi.org/10.4171/RLM/1080).

- Checked the abstract and Introduction against the official PDF: the paper
  revisits the identification between singularities of a normal function and
  its infinitesimal invariant, presents a sketch, and says the formal proof
  in a more general setting will appear separately.
- Full-text searches found no occurrence of “nodal,” “defect,” or
  \(\rho(ii)\). This later paper therefore supplies no correction or
  reinterpretation of the Section 4.2.4 six-invariant statement in S021.
- Scope guard: this absence check supports only NG-028's source audit; it is
  not mathematical evidence that no correction exists elsewhere.

## S034 - Monodromy framework for enumerative problems

Joe Harris, “Galois groups of enumerative problems,” *Duke Mathematical
Journal* 46 (1979), 685-724.
[DOI](https://doi.org/10.1215/S0012-7094-79-04635-0).

- The official bibliographic record was checked. Direct full-text retrieval
  returned a publisher interstitial rather than the article, so no
  page-specific theorem from this source is imported into B033.
- A modern exposition was used to locate the standard strategy—multiple
  transitivity from irreducible incidence spaces and a simple transposition
  from one ordinary double solution—but it is not counted as primary
  evidence.
- B033 does not import a family-specific result from Harris. It verifies the
  one- and two-point incidence spaces, constructs the local double zero
  \((u^2,v)\), and proves the group-theoretic conclusion in the diagonal
  family itself.
- Scope guard: full symmetric monodromy controls uniform postulation of a
  general point scheme. It supplies neither a Hodge type nor an algebraic
  cycle and cannot select a direction paired with an arbitrary Hodge class.

## S035 - Hyperplane-arrangement perverse-sheaf frameworks

Mikhail Kapranov and Vadim Schechtman, “Perverse sheaves over real
hyperplane arrangements,” [arXiv:1403.5800](https://arxiv.org/abs/1403.5800);
Asilata Bapat, “Recollement for perverse sheaves on real hyperplane
arrangements,” [arXiv:1810.13126](https://arxiv.org/abs/1810.13126).

- Checked the primary abstracts and stated scopes. Kapranov–Schechtman give
  an explicit quiver-with-relations description indexed by faces of a real
  arrangement; Bapat identifies modules for intermediate extensions of
  local systems and gives recollement in that framework.
- Rechecked Bapat's Definition 4.3 and Corollary 5.8 in the primary TeX.
  Algebraically, the intermediate extension is the image of the natural map
  from induction \(Re\otimes_{eRe}M\) to coinduction
  \(\operatorname{Hom}_{eRe}(eR,M)\); Corollary 5.8 identifies that module
  with the IC extension of the corresponding open-stratum local system.
- Rechecked Bapat Section 2.2: the algebra \(R_0\) is explicitly generated
  freely over \(\mathbf C\), and the subsequent equivalence is stated for
  complex perverse sheaves. No weight or Hodge filtration appears. NG-034
  therefore forbids using this source alone for G015's rational
  type-\((0,0)\) comparison.
- These are candidate tools for G015 because the node-smoothing parameters
  define a central hyperplane arrangement and the required object is an
  intermediate extension. B036 now fixes the target calculation for
  \(U_{2,5}\); B037-B040 compute the same object by the logarithmic-residue
  and mixed-Hodge-module route. No rational Hodge conclusion is imported
  from Bapat's complex face algebra.
- Scope guard: an arrangement-quiver model by itself does not imply that the
  degree-one stalk equals the full vanishing-cycle relation kernel. A
  dependent \(q\)-block example must be computed explicitly before any
  promotion.

## S036 - Abelian-monodromy limit Hodge structures

András Némethi and Joseph Steenbrink, “Extending Hodge bundles for abelian
variations,” *Annals of Mathematics* 143 (1996), 131-148.
[Official Annals record](https://annals.math.princeton.edu/articles/13216).

- Checked the official bibliographic record and abstract. The paper treats a
  local variation of Hodge structure with abelian monodromy and proves a
  canonical limit mixed Hodge structure and a nilpotent-orbit theorem in
  that setting.
- This supports the relevance of commuting monodromy to G015, but the
  official scope does not state the B035 calculation: it does not identify
  the downstairs intermediate-extension stalk with the full relation kernel
  for the \(U_{2,5}\) arrangement or remove point-supported summands after
  the blow-up.
- No theorem from S036 is used to promote the unresolved IC or type-\((0,0)\)
  comparison. B035's promoted content is the elementary arrangement,
  blow-up, and Picard-Lefschetz reduction only.

## S037 - Pure Hodge-module direct images and semismall support

Morihiko Saito, “Decomposition theorem for proper Kähler morphisms,”
*Tohoku Mathematical Journal* 42 (1990), 127-148.
[DOI](https://doi.org/10.2748/tmj/1178227650).

Mark Andrea A. de Cataldo and Luca Migliorini, “The Decomposition Theorem,
perverse sheaves and the topology of algebraic maps,” *Bulletin of the
American Mathematical Society* 46 (2009), 535-633,
[arXiv:0712.0349](https://arxiv.org/abs/0712.0349).

- Checked Saito's Introduction, pp. 127-129. Theorem (0.3.1) gives
  projective direct-image functors on polarizable Hodge modules compatible
  with perverse cohomology of the underlying perverse sheaves. Formula
  (0.1) gives the unique strict-support decomposition, whose summands are
  intersection complexes with local-system coefficients. Saito states the
  exposition with \(k=\mathbf R\) for simplicity after explicitly allowing
  a subfield \(k\subset\mathbf R\); B039 uses \(k=\mathbf Q\).
- Checked Saito Theorem (0.6) and formula (0.7), pp. 128-129. For geometric
  local-system coefficients, proper direct images of intersection complexes
  decompose into shifted intersection complexes. The local variation in
  B039 is geometric because it comes from projective vanishing cohomology.
- Checked de Cataldo-Migliorini Proposition 4.2.1, Example 4.2.5, and
  Theorem 4.2.7. They record the dimension criterion for semismallness, that
  a surjective map between surfaces is semismall, and the no-shift
  decomposition for a semismall map from a nonsingular source.
- Coefficient guard: the displayed de Cataldo-Migliorini theorem is stated
  for the constant source sheaf. B039 does not extrapolate it to arbitrary
  coefficients. Instead, it proves the necessary perverse stalk/costalk
  bounds directly from B037 and its Verdier dual, then applies Saito's
  coefficient-sensitive projective direct-image and strict-support theorem.
- B042 uses Saito's projective decomposition only after proving directly
  that the threefold blow-up direct image has perverse amplitude
  \([-1,1]\). It does not call the non-semismall blow-up semismall or infer
  \(t\)-exactness.
- B043 similarly proves the dimension-uniform perverse amplitude
  \([-(d-2),d-2]\) from the exceptional cohomological amplitude before
  invoking Saito decomposition. The source supplies decomposition and
  strict support, not the amplitude estimate.
- B044 uses Saito decomposition only after separately auditing the generic
  dependent-flat stratum and the origin. The possible strict support on the
  flat is retained and shifted explicitly; it is not discarded by a
  semismall shortcut.
- Scope guard: the theorem separates the downstairs full-support IC summand
  from point-supported summands. It does not calculate the latter's Hodge
  structures and does not prove that the degree-one relation group has type
  \((0,0)\).

## Citation policy for incompletely audited mechanisms

Spreading out, products/fibrations, and cycle-class rigidity remain recorded
only at the mechanism/obstruction level. Before any dependent brick is
promoted, its exact primary theorem must receive a new `S...` record with
matching field, coefficients, cohomology, and scope. Seeded sources above must
likewise be upgraded to page/theorem-level checks before decisive use.
