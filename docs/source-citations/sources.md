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
- B127/NG102 audit: Theorem 1.3 quantifies only non-torsion/nonzero
  singularity; it contains no clean-nodal incidence condition. Thus it
  confirms G008 as the terminal-equivalent support gate but supplies neither
  G008 unconditionally nor the additional cleanup G085.
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
- B147 reuses only this audited local mechanism: in coordinates adapted to
  the carrier, it computes the nodal Hessian and proves that the carrier
  conormal is maximal isotropic for the inverse-Hessian form. The universal
  construction in Theorem 4.2 still assumes the algebraic carrier and is not
  imported as progress toward HC.
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

- Rechecked Section 4.1.1, pp. 4-5 for G025/NG036: quasi-local normal
  crossings means a union of smooth divisors such that, on a transverse
  slice to their common intersection, every subset of at most the
  intersection codimension of the local equations is part of a coordinate
  system; the local monodromies must commute and be unipotent. It does not
  assert simultaneous analytic equivalence to the tangent hyperplanes.
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
- Rechecked the same Section 4.3.2 for B135/NG108. A local multivalued lift
  changes by \(f+\lambda\); the flat term \(\lambda\) changes the residue
  vector by \(((T_i-I)\lambda)_i\), explicitly a Koszul coboundary. Replacing
  \(T_i-I\) by the commuting rational nilpotent \(N_i\) preserves the
  rational cohomology. For a nodal rank-one image this gives
  \([a]\in\operatorname{coker}\Delta^\ast\), not intrinsic individual
  coefficients. The source identifies the quotient but does not force it to
  be nonzero for an arbitrary prescribed Hodge class.
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
- B045 applies the residue sequence on the blow-up of \(\mathbf P^2\) at two
  points. The three divisor-class components and simultaneous partial-sum
  equations are derived in B045, not imported from S021.
- B046 applies the same rational SNC residue mechanism to
  \(\operatorname{Bl}_{\widetilde\ell}\operatorname{Bl}_p\mathbf P^3\).
  Its three divisor-class components and nested partial-sum equations are
  derived in B046, not imported from S021. No general building-set residue
  theorem is attributed to this source.
- B052 uses Section 4.3.2's logarithmic residue morphism only to identify the
  universal Postnikov transgression with the divisor-class connecting map.
  Connectedness, spectral-sequence vanishing, the divisor basis, coefficient
  sheaves, and the triangular kernel are proved in B049-B052.
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
- NG036 applies the checked definition to five smooth plane branches with
  pairwise independent differentials. Its quadratic-jet computation shows
  that the definition permits analytic moduli, so G025 cannot upgrade the
  source hypothesis to simultaneous analytic linearization.
- B053 uses the same checked definition positively: the coordinate-subset
  condition makes the normal covectors uniform, so the common-stratum
  blow-up has the projectivized tangent arrangement as an SNC exceptional
  divisor. The source is not cited for the blow-up, residue, support, or
  Hodge calculations, which are proved in B053 from B043 and B050-B052.
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
- Rechecked equation (0.3), Theorem 1(i), and the proof in Section 2.4 for
  B134/NG107: the **cohomological** intermediate-extension stalk is
  \(E(Y_0)\), while the homological relation space is canonically
  \(E(Y_0)^\vee\). Thus a local incidence class is intrinsically a functional
  on relations. Proposition 1.7 identifies the two normal-crossing maps as
  adjoints under polarization and proves the dimension comparison; it does
  not turn the specified cohomology class into a canonically selected
  relation vector.
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
- Rechecked Section 2.5, printed pp. 8-9, for B099: Saito chooses
  $\gamma'\in H_{2n}(Y_c,Z_c)$ with boundary $\beta$, transports it by a good
  retraction to $H_{2n}(Y_0)$, pushes it to $H_{2n}(X)$, and takes the
  primitive part. Thus equality with B057's ambient class follows if the
  collision comparison identifies $\gamma'$ with the same relative chain;
  the source does not prove that identification for an arbitrary B057 word.
- Rechecked Section 2.4, printed p. 8, together with §2.5 for B100: the image
  of nearby/limit middle homology in $H_{2n}(X)$ is nonprimitive. Hence two
  relative lifts of the same boundary relation have identical primitive
  ambient images. Literal equality of the relative representatives is not
  required; identifying B057's local boundary remains the open comparison.
- Rechecked §2.5 for B103: the good retraction $\rho:Y_c\to Y_0$ is global
  and induces an isomorphism over $Y_0\setminus\operatorname{Sing}Y_0$.
  With $Z_c$ defined as the union of inverse images of the singular points,
  the paper identifies $H^j(Y_0,Z_0)$ with $H^j(Y_c,Z_c)$ and then uses the
  dual relative cycle. Hence separate local/exterior collapse gluing is not
  the remaining comparison; realization of B057's distributed chain in the
  single nearby pair is.
- Rechecked Proposition 1 and Theorem 1 for B105/NG081: the terminal
  condition for a fixed primitive class is nonvanishing of the scalar
  pairing with $\gamma_\beta$. The paper does not require equality with a
  separately chosen tube class, equality of relative representatives, or
  vanishing of a relative-bordism obstruction. Those are sufficient
  comparison mechanisms only.
- Rechecked the same statements against B106/NG082: $\gamma_\beta$ is
  constructed from the local relation $\beta$ and the terminal formula only
  pairs $\gamma_\beta$ with the prescribed primitive class. No auxiliary
  global tube detector appears in Saito's criterion, confirming that the
  $c$ in B105 cancels rather than encoding provenance.
- Rechecked Proposition 2 and its proof in §2.2, printed pp. 2 and 7, for
  B118/NG094: an isolated hyperplane singularity is an isolated complete
  intersection singularity, and its reduced local vanishing cohomology is
  zero outside degree $2n-1$. Together with the special/nearby/vanishing
  triangle in §2.1, specialization is therefore an isomorphism in degree
  $2n+2$. This is used only after relative hard Lefschetz moves the proposed
  point support into that high direct-image degree.
- Rechecked Theorem 3 and the ordinary-double-point specialization in §1.4
  for B119/NG095: every local vanishing group is $\mathbf Q(-n)$, so the
  rational relation kernel becomes a sum of $\mathbf Q(0)$ after
  $\mathbf Q(n)$. This statement applies to the relation-grade quotient; it
  does not require an arbitrary total special-stalk lift to be type $(0,0)$.
- Rechecked Proposition 2 and the special/nearby exact sequence for B122 and
  NG098. Since isolated hypersurface vanishing cohomology is concentrated in
  raw degree $d$, the arrow
  $H^{d+1}(Y_p,\mathbf Q)\to H^{d+1}(Y_t,\mathbf Q)$ is surjective. This
  proves ordinary target liftability only; it does not place a lift in a
  perverse-filtration step.
- Rechecked Proposition 1, Theorem 1, and the displayed exact sequence for
  B123/NG099. Saito defines
  $E(Y_p)=\ker(H^{d+1}(Y_p)\to H^{d+1}(Y_t))$ and identifies its Hodge-cycle
  dual with the local vanishing-cycle relation space. Thus the relation/extra
  channel is killed by specialization; the source does not obtain it by
  lifting a nonzero nearby cohomology class. Section 2.5 instead constructs
  the ambient class from the boundary of a relative class, matching
  G064-G065's direction.
- Rechecked §2.5 against §2.4 for B124/NG100. After choosing any
  $\gamma'\in H_{2n}(Y_c,Z_c)$ with boundary $\beta$, Saito defines
  $\gamma_\beta$ by good retraction, inclusion in $X$, and primitive
  projection. The absolute nearby-fiber ambiguity maps into the
  nonprimitive part, so every lift of the fixed $\beta$ has the same
  primitive value. The source supplies no freedom to tune this value to a
  preselected global tube class.
- Rechecked Theorem 1(ii) and Theorem 3 for B125. At a nodal member, every
  rational relation has the required Tate-normalized type, and nonzero
  restriction of the specified primitive Hodge class is equivalent to
  nonzero pairing with one canonical relation class. Combined with S024's
  local-restriction criterion, this removes relation choice from G084 and
  leaves only the clean-support incidence.
- For B101/NG077, compared §2.5's target pair $(Y_c,Z_c)$ with S029's marked
  thimble pair. Naturality proves the boundary square only after a map of
  pairs is supplied. S022 does not construct such a map from an arbitrary
  distributed B057 word or identify the individual marked boundary spheres.
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
- B050 uses the full formula (1.4.1), not only its Hodge-number consequence:
  the intermediate-extension stalk is the cohomology of the subcomplex with
  degree-one term \(\bigoplus\operatorname{Im}N_i\) and higher terms the
  images of residue products. Its own Picard-Lefschetz argument proves that
  all products vanish and that the origin residue canonically splits the
  degree-one quotient at every wonderful stratum.
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
- Rechecked pp. 1 and 6-7 for B056-B057: a monodromy-fixed class traces a
  cycle along its loop, well defined modulo reference-fiber homology.
  Schnell's Lemma 3 proves that nonzero vanishing homology makes the dual
  variety an irreducible hypersurface. On pp. 12-13 he chooses a general
  projective plane through the base point and explicitly invokes the
  Lefschetz-Zariski isomorphism
  \(\pi_1(\mathbf P^2\setminus C)\simeq\pi_1(P^{\rm sm})\).
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
- Rechecked Theorem 1 and the scope guard for B106/NG082: surjectivity gives
  the global class $c$ but no topology-changing map to a chosen Saito
  relation. Any use of $c$ in a local scalar formula must therefore be
  justified by additional collision data, not by the tube theorem itself.
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
- Rechecked p. 2, equations (2.1)-(2.2), pp. 3-5, formulas (2.7)-(2.13), and
  Definition 3.3 for B128: the IC has ordinary cohomology only in degrees
  \([-d,-1]\), \(IH^1=\mathbb H^{1-d}\), and restriction of the canonical
  global perverse component gives the local component. These inputs yield
  the two-row edge sequence and identify its section stalks with
  \(s(\zeta)_p\).
- Rechecked Definition 3.3 and Proposition 3.8 against S022 equation (0.3)
  for B134: after the high-power support simplification,
  \(s(\zeta)_p=[\zeta|_{X_p}]_{00}\) is the same canonical restriction
  cocycle in the full-support cohomological IC stalk. Combined with S022 it
  is the functional
  \(\beta\mapsto\langle\zeta,\gamma_\beta\rangle\), not a relation vector.
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
- Rechecked pp. 5-7, equations (5), (7), and (10), for B057: extension along
  a composite path is the sum of the successively transported extensions;
  its boundary is monodromy minus the identity; and a Lefschetz-meridian
  extension is the corresponding intersection coefficient times its
  thimble. These formulas identify B013's telescoping vector with the actual
  tube extension chain.
- Rechecked pp. 15-16, equations (42)-(43), for NG038: the total-equator
  extension matrix is
  \(T_1+T_2M_1+\cdots+T_rM_{r-1}\cdots M_1\), exactly the B057 coefficient
  matrix. Equation (12) quotients its entire image from
  \(\ker\partial\), so a total-equator relation is zero in
  \(\mathcal T(Y)\).
- B091 uses only the audited path-composition identity: marked Hurwitz moves
  preserve the relative extension attached to the same composite path and
  input class. Nothing in this source identifies that extension with a
  topology-changing special-fiber relation. G055 records the missing map.
- Rechecked the pair boundary in §2.1.4 for B101/NG077: S029 computes the
  total boundary in the smooth reference fiber. This does not canonically
  determine the pre-gluing vector in S022's disjoint local group. A marked
  collision map remains necessary.
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
  polarized homological model is the full relation kernel or that the
  cohomological stalk is its dual. A
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
  the polarized homological model with the full relation kernel, the
  cohomological stalk with its dual, or remove point-supported summands after
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
- Rechecked the strictness clause of Theorem (0.3.1) for B132: the filtered
  \(D\)-module direct image under a projective morphism is strict. Applied to
  \(P\to\mathrm{pt}\), this identifies the associated graded of intersection
  cohomology with hypercohomology of the associated-graded de Rham complex.
- Checked Saito Theorem (0.6) and formula (0.7), pp. 128-129. For geometric
  local-system coefficients, proper direct images of intersection complexes
  decompose into shifted intersection complexes. The local variation in
  B039 is geometric because it comes from projective vanishing cohomology.
- Rechecked Theorem (0.3.2), pp. 127-128, and Theorem (3.1.2), p. 142, for
  B118: a relative Kähler class gives
  $\eta^j:{}^pH^{-j}f_*M\simeq{}^pH^jf_*M(j)$. Formula (0.1) makes strict
  support unique, so this isomorphism carries a point-supported summand in
  perverse degree $-1$ to a point-supported summand in degree $1$. The
  discussion on p. 147 explicitly says the Lefschetz maps preserve strict
  support.
- Checked de Cataldo-Migliorini Proposition 4.2.1, Example 4.2.5, and
  Theorem 4.2.7. They record the dimension criterion for semismallness, that
  a surjective map between surfaces is semismall, and the no-shift
  decomposition for a semismall map from a nonsingular source.
- Checked de Cataldo-Migliorini Remark 1.4.2 and Remark 1.6.2: the
  decomposition-theorem splitting into shifted perverse cohomology objects
  is not uniquely determined. The authors compare it to choosing a splitting
  of a filtered vector space.
- Checked Theorem 1.6.1 and Section 2.4: each perverse cohomology object has
  a canonical semisimple decomposition into intersection complexes, while
  perverse truncation induces a canonical perverse filtration on cohomology.
  B081 therefore moves the B058 class test to an associated-graded perverse
  piece before projecting by strict support.
- Rechecked de Cataldo-Migliorini Theorem 1.2.1 for B131: for a smooth
  projective family, the rational Leray spectral sequence degenerates at
  E2. This is the family form of Deligne's primary degeneration theorem
  audited separately as S054.
- Rechecked Remarks 1.4.2 and 1.6.2 together with Theorem 1.6.1 for
  B107/NG083: a filtered object maps canonically to an associated grade only
  from the corresponding filtration step. Neither degeneration nor the
  unique strict-support decomposition inside the grade supplies a projection
  from the entire stalk. Thus G070 must first prove liftability inside that
  filtration step before forming its dual detector certificate.
- Rechecked Theorem 1.7.1(2) and the filtration discussion for B108/NG084:
  local invariant cycles give surjectivity from the unfiltered special-fiber
  group to local monodromy invariants. The theorem does not state strictness
  for the perverse filtration or surjectivity from one chosen filtration
  step. Thus B084 cannot by itself kill
  $[t_\psi]\in\operatorname{im}u/u(S_0)$.
- Rechecked Theorem 1.6.1, Remark 1.6.2, and Theorem 1.7.1 for B109/NG085:
  degeneration supplies associated-graded information, while the derived
  splitting is noncanonical and local invariant cycles are stated on the
  total cohomology sheaf. No cited statement reconstructs the off-diagonal
  extension between perverse grades. G072 must retain that extension data.
- Checked Section 5.5, Remark 5.5.1, triangle (39), and Theorem 5.5.3: the
  natural arrow is $i^*K\to\Psi_fK$, followed by the canonical arrow to the
  shifted vanishing-cycle term. The stalk long exact sequence makes a nearby
  class liftable from the special stalk exactly when its canonical
  vanishing-cycle obstruction is zero. It supplies no unconditional or
  preferred reverse lift. B083/G048 use precisely this criterion.
- G055 uses the same triangle only as an obstruction test. It does not infer
  from it a chain-level morphism from the distributed thimble complex to the
  target local monodromy complex; constructing that comparison is the gate.
- B092/NG068 separately guard the theorem's output: surjectivity onto
  invariant nearby classes supplies a special lift, not a map from that lift
  to B009's local relation group and not nonvanishing of such a component.
- Visually rechecked Theorem 1.7.1(2), printed pp. 15-16: for a proper map
  $f:X\to Y$, an open $U$ where $R^if_*IC_X$ is locally constant, a boundary
  point $u\in\overline U$, and the punctured small ball $B_u$, the natural
  special-fiber restriction/retraction map onto
  $H^0(B_u,R^if_*IC_X)$ is surjective. B084 uses this local invariant-cycle
  theorem to kill B083's obstruction for collision-monodromy-invariant
  nearby classes. The audit does not extend the statement silently from
  varieties to stacks or identify detector-loop with collision monodromy.
- Rechecked the same theorem after proper base change to a marked algebraic
  curve for B120/NG096. On its punctured analytic disk the invariant target
  is the kernel of one cyclic monodromy operator. With
  $K_\Delta=a^*K_B[-1]$, its special group $H^0(i^*K_\Delta)$ is canonically
  $H^{-1}(i^*K_B)$; the source theorem does not require simultaneous
  invariance for approach directions omitted by this curve.
- Rechecked Theorem 1.6.1 and the stalk spectral sequence for B121/NG097.
  In total degree $-1$, ${}^pH^1$ contributes at
  $E_2^{-2,1}$ in addition to the already recorded $E_2^{-1,0}$ and
  $E_2^{0,-1}$ positions. Decomposition degenerates the sequence but does
  not erase this constant ambient grade or canonically project a total lift
  into the relation filtration step.
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
- B045 repeats this support audit for two disjoint strict transforms of
  dependent flats; it makes no claim about nested centers.
- B046 separately audits the codimension-two flat, codimension-three flat,
  and origin for one nested-center model. It does not infer a uniform
  strict-support theorem for arbitrary wonderful building sets from S037.
- B051 first derives the coefficient-sensitive normal-fiber amplitude from
  B050, then uses Saito's projective direct image, Verdier duality, and
  strict-support decomposition. It does not infer the amplitude from the
  constant-coefficient semismall theorem.
- Scope guard: the theorem separates the downstairs full-support IC summand
  from point-supported summands. It does not calculate the latter's Hodge
  structures and does not prove that the degree-one relation group has type
  \((0,0)\).
- Local retrieval SHA-256 for the de Cataldo-Migliorini survey PDF:
  `171415A41C8E6AAF90E227B4003DE9611C249A88B94A93550D7500EAD6996E5F`.

## S038 - Wonderful compactification and permissible blow-up orders

Li Li, “Wonderful compactification of an arrangement of subvarieties,”
*Michigan Mathematical Journal* 58 (2009), no. 2, 535-563,
[arXiv record and primary PDF](https://arxiv.org/abs/math/0611412),
[DOI](https://doi.org/10.1307/mmj/1250169076).

- Checked pp. 1-2, Theorem 1.2 in the primary PDF: for a building set in a
  nonsingular variety, the wonderful compactification is nonsingular; its
  boundary components are nonsingular divisors meeting transversally, and a
  collection has nonempty intersection exactly when it is a nest.
- Checked pp. 2-3, Theorem 1.3: if every initial segment of the chosen order
  is a building set, the wonderful compactification is the displayed
  sequence of blow-ups along nonsingular dominant transforms. Increasing
  dimension is listed as an admissible example.
- Checked Definition 2.7 and Proposition 2.8: a center contained in the
  blow-up center has dominant transform equal to its full inverse image, and
  blowing a minimal building element produces the stated induced
  arrangement and building set.
- Checked Lemma 2.9: the strict/dominant transforms retain the required clean
  intersections; incomparable transforms become disjoint when their
  intersection is the blown center. This supports the inclusion-order
  induction, not the false arbitrary-order avoidance claim in NG035.
- Rechecked the proof of Lemma 2.9(iii) for B054: inside the exceptional
  divisor, transformed intersections are explicitly
  \(\mathbf P(N_F A_1)\cap\mathbf P(N_F A_2)
  =\mathbf P(N_F(A_1\cap A_2))\); the clean tangent-space equality is the
  stated reason. Together with Proposition 2.8, this supplies the iterated
  tangent-normal-fiber induction for nonlinear clean arrangements.
- Checked Definition 2.12 and Proposition 2.13: the inclusion-compatible
  iterated blow-up construction yields the wonderful compactification.
- Checked pp. 4-7, Definitions 2.1-2.3: arrangements use clean
  scheme-theoretic intersections, building-set factors meet transversally,
  and nests are induced by flags. These hypotheses apply to B047's linear
  subspace arrangement over \(\mathbf C\).
- B047 imports only smoothness, the permissible inclusion-compatible order,
  SNC boundary, and nested-stratum incidence. Its exceptional fiber, divisor
  classes, residue equations, direct-image degree bounds, and Hodge type are
  derived inside B047; none is asserted by Li.
- B048 uses the same theorem for the fork's smooth/SNC resolution. The
  disjointness of the two child transforms, commutation of their blow-ups,
  divisor classes, and residue equations are proved inside B048.
- B049 uses these results to prove the Picard basis and multiplicity-one
  branch formula in inclusion order and then transport the intrinsic
  labelled divisors through Theorems 1.2-1.3. Li does not itself state the
  explicit formula. NG035 records why raw exceptional coordinates from a
  reverse nested order cannot replace this intrinsic comparison.
- B054 uses Proposition 2.8 and Lemma 2.9 to identify each restricted
  nonlinear blow-up with the corresponding blow-up of the projectivized
  tangent arrangement. Li supplies the clean/building-set geometry only;
  B049-B052 supply the residues, IC hypercohomology, support bounds, and
  rational Hodge type.
- Scope guard: wonderful compactification resolves the arrangement boundary.
  It does not identify a Picard-Lefschetz intermediate-extension stalk,
  supply a rational type-\((0,0)\) relation, or construct an algebraic cycle.
- Local retrieval SHA-256:
  EE9716E639B40AE0A59CC7073CDCC5C816106F412280E76F5206D4D67B7698B9.

## S039 - Zariski fundamental-group reduction to a plane

Shulim Kaliman, “Uniform Zariski's Theorem On Fundamental Groups,”
arXiv:alg-geom/9711033 (1997).
[arXiv record and PDF](https://arxiv.org/abs/alg-geom/9711033).

- Checked p. 1: Kaliman states the classical projective Zariski theorem in
  the exact form used here. For a hypersurface \(H\subset\mathbf P^N\),
  \(N\ge3\), and a generic projective plane \(A\), inclusion induces
  \[
  \pi_1(A\setminus H)\xrightarrow{\sim}
  \pi_1(\mathbf P^N\setminus H).
  \]
- Triangulated with Schnell S023, pp. 12-13: Schnell applies this theorem to
  a general plane through the reference hyperplane and the irreducible dual
  hypersurface \(X^\vee\), obtaining
  \(\pi_1(\mathbf P^2\setminus C)\simeq\pi_1(P^{\rm sm})\).
- B056 uses only this fixed-hypersurface projective theorem. It does not use
  Kaliman's stronger uniform affine-family result.
- Scope guard: the theorem moves a loop into a two-parameter net. It does
  not move it into a pencil, collide discriminant points, preserve a local
  Hodge type through specialization, or construct an algebraic cycle.
- Local retrieval SHA-256:
  A647D8043EF7548CFE77BD8D3523E01479619B20F380AFD1C5AE4D17076E909E.

## S040 - Claimed degeneration proof and its arithmetic dependencies

Johann Bouali, “Degeneration of families of projective hypersurfaces and
Hodge conjecture,” arXiv:2401.03465v13 (7 October 2024),
[arXiv record](https://arxiv.org/abs/2401.03465),
[versioned PDF](https://arxiv.org/pdf/2401.03465v13).

Dependency audit:

- Johann Bouali, “De Rham logarithmic classes and Tate conjecture,”
  arXiv:2303.09932v16 (24 September 2024),
  [versioned PDF](https://arxiv.org/pdf/2303.09932v16).
- Johann Bouali, “Hodge conjecture for projective hypersurface,”
  arXiv:2312.09268v1 (14 December 2023),
  [versioned PDF](https://arxiv.org/pdf/2312.09268v1).

Audit findings:

- Checked arXiv:2401.03465v13, pp. 14-15. The final algebraicity step invokes
  Theorem 4 of arXiv:2303.09932 after proving that certain Hodge-locus
  components and their conjugates are defined over
  \(\bar{\mathbf Q}\). This dependency is decisive for both summands of the
  arbitrary Hodge class.
- Checked arXiv:2303.09932v16, pp. 34-35, Theorem 3(i). Its proof constructs
  \(Z\in Z^d(X_{\widehat{k}_{\sigma_p}})\otimes\mathbf Q_p\), then writes an
  average of \(gZ\) over \(G_k/G_Z\) to produce a cycle over \(k\).
- No intervening argument proves that \(Z\) is defined over \(\bar k\) or a
  finite algebraic extension of \(k\). A cycle over the completion
  \(\widehat{k}_{\sigma_p}\) has no automatic \(G_k\)-orbit. B060 gives the
  explicit field-of-definition type check.
- Checked pp. 36-38 of the same version. Corollary 2(ii) derives algebraicity
  of absolute Hodge classes from Theorem 3, and Theorem 4 derives its
  Hodge-locus algebraicity criterion from Corollary 2(ii). The invalid
  descent therefore propagates directly to the theorem used on p. 14 of the
  degeneration paper.
- Checked arXiv:2312.09268v1, pp. 1-2 and 16, Theorem 1. Its hypersurface
  claim uses a separate logarithmic-de-Rham argument and the same earlier
  preprint, but even granting it does not repair the arithmetic descent gap
  in the general induction.
- Scope guard: NG041 identifies a gap in the written proof chain. It does
  not prove the claimed theorem statements false, and it is not evidence
  against the Hodge Conjecture.
- Local retrieval SHA-256 values:
  - arXiv:2401.03465v13:
    `33E0D01DC5B96B7A26A9C1B5150A7F0E918B71B58318BAFA644880B750CAD808`;
  - arXiv:2303.09932v16:
    `F3D565576D1C84C61B3C02CF6A2069A000135079B66A0BA498B3A6D9ACCB5E55`;
  - arXiv:2312.09268v1:
    `0BFF688E96BFA5DB860F818233C5F55F196D2D39A371FC0C83426B00B0E39E82`.

## S041 - Iterated nearby cycles: lax comparison and conditional commutation

Matthieu Kochersperger, “Comparison theorem for nearby cycles of a morphism
without slopes,” *Journal of Singularities* 16 (2017), 52-72;
[arXiv:1612.07473](https://arxiv.org/abs/1612.07473),
[versioned PDF](https://arxiv.org/pdf/1612.07473v2).

- Checked the introduction: nearby-cycle functors associated to several
  functions do not commute in general. The without-slopes condition is the
  additional hypothesis used to obtain order-independent iteration.
- Checked Theorem 3.6 and Corollary 3.7: for a regular holonomic
  \(\mathcal D\)-module whose graph pair is without slopes, algebraic and
  topological nearby cycles compare, iterated nearby cycles are independent
  of coordinate order, and the identifications respect monodromy.
- Local retrieval SHA-256:
  `1A9764FD467BD9BBE0D9DF010E74AF54247D17416E7D6D5FD8EE3291E50AC533`.

David Nadler, “A microlocal criterion for commuting nearby cycles,”
[arXiv:2003.11477](https://arxiv.org/abs/2003.11477),
[versioned PDF](https://arxiv.org/pdf/2003.11477v4).

- Checked Proposition 3.2.10 and the introduction: an arbitrary weakly
  constructible complex has a natural lax diagram from the multivariable
  nearby-cycle object to the different iterated orders; the arrows are not
  asserted to be equivalences without extra hypotheses.
- Checked Definitions 4.1.2 and 4.1.6 and Theorem 4.2.1: if the ambient map
  to a polydisk is a submersion and the singular-support Lagrangian is both
  non-characteristic and Thom at the origin, all flag-comparison maps are
  equivalences, compatibly with monodromy.
- Checked Remark 4.1.3: a conormal \(T_Z^*X\) is non-characteristic relative
  to \(f\) exactly when \(f|_Z\) is a submersion. B062 applies this to a
  graph and proves the elementary differential calculation explicitly.
- Local retrieval SHA-256:
  `AFD86207E77537D31A7E21E3F4AC77C3726F056C73E5059742952526F05372FD`.

Scope guard: these sources establish complex constructible-sheaf or regular
holonomic \(\mathcal D\)-module comparison under explicit hypotheses. They do
not verify those hypotheses for G032's collision family, give a rational
mixed-Hodge-module lift, preserve the B022 quotients or Saito pairing, or
construct an algebraic cycle.

## S042 - Mixed Hodge modules without slopes

Matthieu Kochersperger, “Mixed Hodge modules without slope,”
[arXiv:1808.10719](https://arxiv.org/abs/1808.10719),
[versioned PDF](https://arxiv.org/pdf/1808.10719v1) (2018).

- Checked pp. 2-4: the paper distinguishes the geometric without-slopes
  condition for a morphism from the corresponding condition for a
  \(\mathcal D\)-module or perverse-sheaf pair. For a geometric morphism the
  critical locus must lie over the union of the chosen coordinate
  hyperplanes. The introduction also records Lê's multi-parameter failure of
  Milnor fibration in general.
- Checked Theorem 6.1 and Corollary 6.2, p. 16: if
  \(\mathcal M\in MHM(X\times\Delta^p)\) and the underlying right
  \(\mathcal D\)-module pair is without slopes, every permutation of the
  iterated nearby-cycle functors is isomorphic in the category of mixed
  Hodge modules. Theorem A records the analogous nearby- and vanishing-cycle
  result.
- Checked Theorem B, pp. 3-4: under without slopes, strict
  \(R\)-multispecialisability is equivalent to compatibility of the Hodge
  filtration with the coordinate \(V\)-filtrations. It is an additional
  condition, not silently automatic in the audited statement.
- Checked Theorem 8.1, pp. 21-22: strict \(R\)-multispecialisability and the
  canonical \(V\)-multifiltration are preserved by proper direct image in the
  stated product situation. This theorem cannot be invoked from without
  slopes alone.
- Checked Proposition 10.2 and Corollary 10.3, pp. 27-28: for a
  \(p\)-dimensional quasi-ordinary hypersurface parametrized from
  \(\mathbf C^p\), the specified direct-image Hodge module is strictly
  multispecialisable along the first \(p\) ambient coordinate hyperplanes.
  For a plane cusp \(p=1\), so this does not furnish a simultaneous
  two-coordinate comparison for the ambient \((s,t)\)-plane; NG044 records
  the mismatch.
- Scope guard: the comparison preserves rational mixed-Hodge structure
  because it is internal to \(MHM\), but the paper does not discuss B022's
  quotient maps, the Saito ambient detector map, or its pairing with a fixed
  Hodge class.
- Local retrieval SHA-256:
  `622B4BF768D54B86102634C867D838EAF4C608EE24CD452C313703284DC48D81`.

## S043 - Weyl covers and simultaneous resolution of rational surface singularities

N. I. Shepherd-Barron, “Weyl group covers for Brieskorn's resolutions
in all characteristics and the integral cohomology of \(G/P\),”
[arXiv:1711.10439](https://arxiv.org/abs/1711.10439),
[versioned PDF](https://arxiv.org/pdf/1711.10439v5) (2019).

- Checked pp. 1-3: the paper concerns an affine **surface** with rational
  singularities and the Artin component of its deformation space. It recalls
  the Brieskorn characteristic-zero simultaneous-resolution result for
  rational double points and identifies the required finite covering through
  the associated Weyl group.
- Checked Theorem 1.1, p. 1, and Theorem 2.10(1), p. 9: the simultaneous-
  resolution cover is Galois with effective Weyl-group action and quotient
  the Artin component.
- Checked Theorem 2.10(2)-(3), p. 9: the cover is smooth and is the base of a
  versal deformation of the minimal resolution; reflection fixed divisors
  are the loci where the corresponding roots survive as effective curves.
- For type \(A_2\), the Weyl group is \(S_3\), agreeing with B067's explicit
  ordered-root cover.
- Scope guard: the theorem uses a minimal resolution of a surface and a root
  configuration of exceptional \((-2)\)-curves. It does not state a
  simultaneous-resolution or semistable-model theorem for arbitrary
  higher-dimensional quadratic suspensions, nor any rational mixed-Hodge or
  detector-pairing descent result. B068 and NG046 enforce this boundary.
- Local retrieval SHA-256:
  `5144A5F56FE7CE4BCE841D83B07B471147B88BCF8A254C7626CA346D1FA71DDD`.

## S044 - Weak semistable reduction in arbitrary dimension

Dan Abramovich and Kalle Karu, “Weak semistable reduction in
characteristic 0,” *Inventiones Mathematicae* 139 (2000), 241-273;
[arXiv:alg-geom/9707012](https://arxiv.org/abs/alg-geom/9707012),
[versioned PDF](https://arxiv.org/pdf/alg-geom/9707012v1).

- Checked Definition 0.1, p. 2: weak semistability means toroidal,
  equidimensional, with reduced fibers and nonsingular base. “Semistable”
  additionally requires the total space to be nonsingular.
- Checked Conjecture 0.2, p. 2: in the audited version, obtaining a
  nonsingular semistable total space by a base alteration and a modification
  is stated as the stronger goal, not as the main theorem.
- Checked Theorem 0.3, p. 2: for a surjective morphism of complex projective
  varieties with geometrically integral generic fiber, there is a projective
  alteration of the base and a projective modification of the pullback that
  is weakly semistable.
- Checked the immediately following scope statement: the theorem does not
  initially assert the total space smooth; the authors indicate quotient
  singularities after further work.
- The introduction's summary of de Jong allows alteration of the total space
  to obtain a nonsingular semistable model. That is generically finite, not
  the birational modification required to identify the original detector
  without a separate trace/descent argument.
- Scope guard: the theorem is dimension-uniform and projective, but does not
  specify the \(S_3\) root cover, equivariance, rational MHM strictness,
  direct-image supports, or preservation of the B022/Saito pairing. B069,
  NG047, and G038 record these boundaries.
- Local retrieval SHA-256:
  `D8EA2413D02D52091B06AAB4581F42628A3678F082C20784C204961FFBBED8D3`.

## S045 - Functorial absolute desingularization

Michael Temkin, “Functorial desingularization of quasi-excellent schemes in
characteristic zero: the non-embedded case,” *Duke Mathematical Journal* 161
(2012), 2207-2254; [arXiv:0904.1592](https://arxiv.org/abs/0904.1592),
[versioned PDF](https://arxiv.org/pdf/0904.1592v2).

- Checked Theorem 1.2.1, pp. 3-4: every noetherian quasi-excellent
  generically reduced scheme over \(\operatorname{Spec}\mathbf Q\) has a
  blowup sequence with regular centers, avoiding the original regular locus,
  with regular output, functorial for all regular morphisms.
- Checked the definition of functorial desingularization and Lemma 2.3.1,
  pp. 11-12: pullbacks of the functorial sequence agree for morphisms in the
  category, with empty blowups inserted compatibly.
- B070's equivariance is a formal consequence: every finite-group
  automorphism is an isomorphism, hence a regular morphism, so it preserves
  the canonical sequence and lifts to the output.
- Scope guard: this is an absolute desingularization theorem. It does not
  state that resolution of the source of a weakly semistable morphism
  preserves toroidality, equidimensionality, saturation/reduced fibers,
  nearby cycles, or detector trace. NG048 and G039 isolate the relative gap.
- Local retrieval SHA-256:
  `0C5E2F27FF35A48D605AB1573B9ACB027B4FD550574855417E643D24336B5CC3`.

## S046 - Functorial semistable reduction in characteristic zero

Karim Adiprasito, Gaku Liu, and Michael Temkin, “Semistable reduction in
characteristic 0,” [arXiv:1810.03131](https://arxiv.org/abs/1810.03131),
[versioned PDF](https://arxiv.org/pdf/1810.03131v2) (2019).

- Checked Definition 2.2 and Conjecture 2.4, pp. 3-4: weak semistability of a
  conical-complex map means cones map onto cones with surjective lattice
  maps and regular base; semistability additionally requires regular source.
  The conjecture is the projective alteration/subdivision theorem producing
  a semistable map.
- Checked Theorem 2.7, p. 4: the conjecture is proved by a quasi-local
  construction compatible with pairs of surjective local isomorphisms of
  source and base. This is stronger than bare existence.
- Checked the repair clause in Section 2.3.5, pp. 5-6: source subdivisions
  can destroy weak semistability, and the construction restores it after
  each such step by the minimal further base dilation/alteration. This
  directly repairs the obstruction isolated in NG048.
- Checked Theorem 3.3, p. 7: the polytopal construction is projective,
  quasi-local, and produces unimodular triangulations of source and base in
  arbitrary dimension.
- Checked Theorem 4.4, pp. 19-20: the construction lifts to a projective
  monoidal resolution of fine log schemes compatible with surjective strict
  morphisms. A finite group acting by strict automorphisms therefore lifts
  to the resolved log stacks; B071 records this formal consequence.
- Checked Theorem 4.5, pp. 20-21: a log-smooth morphism admits a monoidal
  alteration and source subdivision making it semistable.
- Checked Remark 4.6, p. 21: if the input consists of schemes, Kawamata's
  trick can produce schemes, but the usual base alteration is noncanonical.
  The remark does not assert compatibility with a preassigned finite-group
  action.
- Checked Theorem 4.7, p. 21: in characteristic zero the authors obtain a
  stack-theoretic base modification and projective source modification with
  regular source/base and SNC boundaries, preserving an already semistable
  open locus.
- Scope guard: the paper proves the arbitrary-dimensional relative
  semistable geometry, not rational mixed-Hodge-module descent, strict
  support, B022 quotient compatibility, or nonzero detector trace. NG049 and
  G040 retain those obligations.
- Local retrieval SHA-256:
  `09AC6958CC75D7FB2223A17B3109831DA2FF5C8CC8A4DF51E4FA577CEA578700`.

## S047 - Rational mixed Hodge modules on algebraic stacks

Swann Tubach, “Mixed Hodge modules on stacks,” *Forum of Mathematics,
Sigma* 13 (2025), e175;
[arXiv:2407.02256](https://arxiv.org/abs/2407.02256),
[versioned PDF](https://arxiv.org/pdf/2407.02256v3).

- Checked the introduction theorem, pp. 1-2: the rational derived category of
  mixed Hodge modules extends canonically to algebraic stacks with the six
  operations, weights, and nearby cycles.
- Checked Theorem 3.1, pp. 12-13: the stack extension has the adjunctions,
  base-change, projection, localization, purity, and duality structure needed
  for the six-operations formalism.
- Checked Proposition 3.15, pp. 16-17: for a proper morphism represented by
  Deligne-Mumford stacks, the canonical map (f_!\to f_*) is an isomorphism
  on the stated constructible bounded-below category.
- Checked Definition 3.27 and the discussion preceding Proposition 3.29,
  pp. 21-23: unipotent nearby cycles are defined on algebraic stacks and the
  coherent construction encodes compatibility with proper pushforward and
  smooth pullback.
- Checked Theorem 3.28 and its consequence on p. 22: unipotent nearby cycles
  form a natural transformation on the correspondence category with proper
  left legs and smooth right legs; the authors explicitly state that this
  expresses compatibility with proper pushforward and smooth pullback. B076
  applies this to the finite-cover unit/trace pair.
- Checked Proposition 3.29, p. 23: shifted unipotent nearby cycles preserve
  bounded constructible objects and are perverse exact; the rational
  realization is conservative and commutes with the construction.
- Checked Theorem 3.36, pp. 24-25: full nearby cycles on stacks preserve
  bounded constructible objects, are perverse exact and lax monoidal, commute
  with external products, and have the stated duality comparison. The proof
  is smooth-local and compares with Saito's functor on schemes.
- Checked Definition 3.37 and Proposition 3.38, p. 25: vanishing cycles are
  defined by the canonical cone and preserve bounded constructible objects
  with perverse exactness after shift.
- Checked Proposition 3.39, pp. 26-27: on a quotient stack ([X/G]), the
  homotopy category agrees with Achar's equivariant mixed-Hodge-module
  category; the six operations agree as well.
- Checked Proposition 3.22, Corollary 3.23, and Corollary 3.24, pp. 18-20:
  \(f_!\) preserves upper weight bounds, \(f_*\) preserves lower weight
  bounds, and on stacks with affine stabilizers every pure object splits into
  its perverse cohomology while pure perverse objects are semisimple. Together
  with proper \(f_!=f_*\), B077 obtains the strict-support decomposition of
  the semistable pushdown.
- Scope guard: the source constructs the stack/equivariant formalism. It does
  not compute the (S_3)-character of the A2 detector, identify the required
  invariant full-support summand, prove the B063 multi-(V)-filtration
  hypothesis for this object, compare B022's two quotients, or establish a
  nonzero detector pairing. B072, B073, NG050, and G041 separate these tasks.
- Local retrieval SHA-256:
  `CF8B315F723740C08EB43995DE0C5601866DF2310A4CA04C832616ABAAB33BA7`.

## S048 - The combinatorics and topology of proper toric maps

Mark Andrea A. de Cataldo, Luca Migliorini, and Mircea Mustaţă, “The
combinatorics and topology of proper toric maps,” *Journal für die reine und
angewandte Mathematik* 744 (2018), 133-163;
[arXiv:1407.3497](https://arxiv.org/abs/1407.3497),
[versioned PDF](https://arxiv.org/pdf/1407.3497v2).

- Checked Theorem 4.1, p. 17: for a proper toric map with simplicial source,
  every fiber has pure rational Hodge-Tate cohomology; in particular its odd
  cohomology vanishes.
- Checked Theorem 5.1, pp. 20-23: for a proper toric fibration,
  (Rf_*IC_X) decomposes into shifted intersection complexes of orbit
  closures with constant coefficients, and the multiplicity (s_{\tau,b})
  vanishes when (b+\dim X-\dim V(\tau)) is odd. Symmetry follows from
  Poincare duality, and the stated inequalities require projectivity and
  relative hard Lefschetz.
- Checked Remark 5.2, pp. 20-21: a general proper toric map factors through a
  toric fibration and a finite toric map. The same support multiplicities and
  shifts remain, while finite local systems may occur on the image orbits.
- Checked Proposition 5.4, pp. 21-22: fiber intersection cohomology vanishes
  when the degree plus (dim X) is odd; the proof resolves the toric source
  and invokes Theorem 4.1.
- Checked Lemma 5.6 and the proof of Theorem 5.1, pp. 22-23: for a toric
  fibration the direct image is constructible on torus orbits and the local
  systems are constant; the fiber parity gives the support-shift parity.
- Checked Theorem 6.1, pp. 23-24: when source and target are simplicial,
  (IC_X=\mathbf Q_X[\dim X]) and (IC_V=\mathbf Q_V[\dim V]), making the
  ordinary-degree normalization explicit. A term indexed by ((V,b)) starts
  generically in ordinary degree (dim X-dim V+b), hence in even degree.
- Scope guard: the paper treats globally toric maps. It does not state a
  coefficient-sensitive global decomposition theorem for arbitrary
  toroidal/semistable families, identify the B057-B058 specialization, or
  control the B022 quotients and prescribed pairing. B078 imports the exact
  positive theorem; NG055/G044 isolate the missing application.
- Local retrieval SHA-256:
  `E769D3C50F9499507F05A7E0E67441FD371BD874BB4AA9726923F5A5CC35FEF6`.

## S049 - Vanishing polyhedron and local collapsing map

Lê Dũng Tráng and Aurélio Menegon Neto, “Vanishing polyhedron and collapsing
map,” *Mathematische Zeitschrift* 286 (2017), 1003-1040;
[arXiv:1511.06812](https://arxiv.org/abs/1511.06812),
[DOI](https://doi.org/10.1007/s00209-016-1793-8).

- Checked Theorem 1: for a holomorphic function with an isolated singularity
  on a reduced equidimensional complex analytic germ, a sufficiently small
  Milnor fiber $X_t$ is a regular neighborhood of a real
  $(n-1)$-dimensional vanishing polyhedron $P_t$.
- Checked the conclusion of Theorem 1 and its proof: for a simple path from
  $t$ to $0$, a continuous map $\Psi_t:X_t\to X_0$ sends $P_t$ to the
  singular point and restricts to a homeomorphism
  $X_t\setminus P_t\to X_0\setminus\{0\}$.
- Checked Propositions 14-16 and the proof around the global vector field:
  the vanishing polyhedra and integrable stratified vector fields are
  constructed along a path, and Proposition 16 gives a collapsing cone over
  a closed semidisk.
- Scope guard: this is a local analytic theorem for one isolated
  singularity. It does not localize an arbitrary global B057 detector in the
  Milnor fiber, identify its marked local relation vector, glue several
  disjoint local collapses to the global exterior, descend through B022, or
  preserve a prescribed ambient Hodge class. B102 imports the theorem;
  NG078/G066 isolate the missing globalization.
- Retrieval audited through the versioned arXiv full text; no local copy is
  committed.

## S050 - Specialization of Milnor-fiber boundary homology

Marcelo Aguilar, Aurelio Menegon, and José Seade, “Vanishing and nearby
boundary cycles of complex non-isolated singularities,” *Boletín de la
Sociedad Matemática Mexicana* 31 (2025), article 81;
[open-access article](https://doi.org/10.1007/s40590-025-00761-5).

- Checked Proposition 1.1: outside a chosen vanishing zone, the boundary of
  a nearby Milnor fiber is homeomorphic to the complement of the analogous
  zone in the special link, under the stated Whitney/transversality setup.
- Checked Definitions 1.2-1.4: the specialization morphism on boundary
  homology is the composite of inclusion in an extended regular
  neighborhood and deformation retraction to the special link; its kernel
  defines vanishing boundary cycles.
- Checked Remark 1.5: the authors distinguish this boundary specialization
  from Siersma's variation maps on relative groups.
- Scope guard: the morphism concerns boundary homology of a local Milnor
  fiber. It is not a relative-thimble map from B057's distributed global
  complex, does not choose a marked relation coordinate, and has no B022 or
  primitive ambient-class compatibility theorem. NG078 records the blocked
  globalization.
- Open-access HTML and theorem statements audited; no local copy is
  committed.

## S051 - Ngô support theorem for delta-regular weak abelian fibrations

Bao Châu Ngô, “Le lemme fondamental pour les algèbres de Lie,”
*Publications Mathématiques de l'IHÉS* 111 (2010), 1-169;
[journal record and full text](https://www.numdam.org/item/PMIHES_2010__111__1_0/),
[arXiv:0801.0446](https://arxiv.org/abs/0801.0446),
[DOI](https://doi.org/10.1007/s10240-010-0026-7).

- Checked §7.1.1-§7.1.4: a weak abelian fibration consists of a proper map
  $f:M\to S$, a smooth commutative group scheme $g:P\to S$ of the same
  relative dimension, a fiberwise action with affine stabilizers, and a
  polarizable Tate module.
- Checked the delta-regular refinement in §7.1 and the support theorem and
  support inequality in Theorem 7.2.1 and Proposition 7.2.2: the support
  restriction uses the weak-abelian action and delta-regularity; it is not a
  theorem for arbitrary projective maps.
- Checked the stated full-support consequence: under the support theorem,
  irreducibility of the geometric fibers forces supports to be the whole
  base because the relevant top direct image has full support.
- Scope guard: the universal high-power hyperplane family in G076 is not
  supplied with a same-dimensional smooth commutative group scheme action,
  affine stabilizers, polarizable Tate module, or delta-regularity. B115
  proves more strongly that for high powers its generic fiber has ample
  canonical bundle, incompatible with the generically homogeneous abelian
  fibers forced by these hypotheses. Ngô's theorem therefore cannot close
  G076.
- Web and primary full-text retrieval audited on 2026-08-11; no local copy is
  committed.

## S052 - Lefschetz direct images across an ordinary quadratic fiber

Ania Otwinowska and Morihiko Saito, “Monodromy of a family of hypersurfaces
containing a given subvariety,” *Annales scientifiques de l'École Normale
Supérieure* 38 (2005), 365-386;
[primary full text](https://www.numdam.org/article/ASENS_2005_4_38_3_365_0.pdf),
[DOI](https://doi.org/10.1016/j.ansens.2005.03.003).

- Checked §2.1, equations (2.1.1)--(2.1.3), pp. 371-372: for a proper family
  of hypersurface sections, proper base change identifies the higher direct
  image stalks with fiber cohomology and fixes the degree convention used in
  B117.
- Checked §2.2, equations (2.2.1)--(2.2.2), p. 372: for a Lefschetz pencil
  with nonzero vanishing cohomology, restriction from middle cohomology to
  the rank-one Milnor-fiber group is surjective, and the vanishing-cycle long
  exact sequence makes cospecialization in the next degree an isomorphism.
- Checked equations (2.2.3)--(2.2.5), p. 372: every higher direct image away
  from the middle degree is constant across the critical values, while the
  middle direct image is the shifted intersection-complex extension from
  the smooth locus. The authors explicitly cite local invariant cycles or
  the decomposition theorem as an alternative proof of the latter fact.
- Degree guard: with ambient dimension $m=2n$ and hyperplane-fiber dimension
  $d=m-1$, a punctual summand of
  ${}^pH^0(Rg_*\mathbf Q[d+1])$ contributes to
  $R^{d+1}g_*\mathbf Q=R^m g_*\mathbf Q$, not to the middle sheaf
  $R^d g_*\mathbf Q$. NG093 records why equation (2.2.5) alone is
  insufficient; B117 also uses the constancy in equation (2.2.3).
- Scope guard: the checked statement is for a Lefschetz pencil with smooth
  total space and nonzero vanishing cohomology. B117 applies it only on a
  generic transverse disk to an ordinary-quadratic discriminant divisor of
  the original incidence family. It does not exclude exceptional supports
  created by a semistable alteration, construct a selected detector class,
  or prove any Hodge class algebraic.
- Primary full text audited on 2026-08-11; no local copy is committed.

## S053 - Nori connectivity from the filtered D-module viewpoint

Daniel Brogan, “Nori's connectivity theorem from the perspective of
\(D\)-modules,” arXiv:2209.13683 (2022).
[arXiv record](https://arxiv.org/abs/2209.13683),
[primary PDF](https://arxiv.org/pdf/2209.13683).

- Checked pp. 1-2, Theorem 1.1 and Proposition 1.3: for a smooth projective
  variety of dimension \(n+1\) and sufficiently high universal hyperplanes,
  restriction from \(P^{\rm sm}\times X\) to the smooth incidence family is
  an isomorphism below degree \(2n\) and injective in degree \(2n\); the
  filtered \(D\)-module statement computes graded de Rham cohomology sheaves
  of the vanishing-cohomology module.
- Checked pp. 11-13 and Corollary 4.1: the only nonconstant direct-image
  Hodge module is the minimal extension \(M\) of the vanishing-cohomology
  variation. Specializing \(k=n+1\), \(b=r\), and \(n=2r-1\) identifies
  \(H^{r,r}_{\rm prim}(X)\otimes\mathcal O_P\) with
  \(\mathcal H^{-d+1}\operatorname{gr}^{F}_{-r}\operatorname{DR}(M)\) for
  \(r\ge2\).
- Checked pp. 13-14, Corollary 5.2 and the subsequent Leray construction:
  the calculation continues over \(P^{\rm sm}\). The author constructs a
  map from primitive cohomology through the Leray filtration, but explicitly
  says it only seems likely to be the Corollary 4.1 map and that the
  coincidence was not checked.
- Rechecked the proof of Corollary 5.2 for B131-B132/NG105. The step from
  global sections of the primitive bundle on the smooth locus to the
  finite-dimensional primitive space is invalid in general: the complement
  of the discriminant hypersurface has nonconstant regular functions. The
  same passage uses associated-graded filtered hypercohomology on the
  nonproper smooth locus without the projective strictness available on the
  full parameter space. B131 proves rational first-Leray nonvanishing
  independently; B132 gives the valid filtered realization on full
  projective P.
- The displayed Corollary 5.2 conclusion uses primitive cohomology in degree
  n, while Corollary 4.1 at k=n+1, the proof's Hodge summands of total degree
  n+1, and the incidence total degree all require primitive cohomology in
  degree n+1. This is treated as an index typo, not as a theorem supplying
  G088.
- Scope guard: on \(P^{\rm sm}\), \(\operatorname{DR}(M)\) resolves the shifted
  vanishing local system and has no ordinary cohomology sheaf in degree
  \(-d+1\), even when the cohomology of its associated-graded Higgs complex
  in that degree is nonzero. The source does not prove a local Betti
  singularity at the discriminant and does not identify one with
  \(s_m(\zeta)\).
- Primary full text retrieved and audited on 2026-08-11; no local copy is
  committed.

## S054 - Lefschetz criterion and Leray degeneration

Pierre Deligne, “Théorème de Lefschetz et critères de dégénérescence de
suites spectrales,” *Publications Mathématiques de l'IHÉS* 35 (1969),
107-126. [DOI](https://doi.org/10.1007/BF02698925),
[official PDF](https://pmihes.centre-mersenne.org/item/10.1007/BF02698925.pdf).

- Checked Proposition 2.1, pp. 110-111: the relative Lefschetz condition
  splits the derived direct image into its cohomology sheaves and therefore
  degenerates the Leray spectral sequence.
- Checked cases 2.6.2-2.6.3, p. 112: a proper smooth Kähler family, and in
  particular a complex smooth projective family with a relatively ample line
  bundle, satisfies the relative Lefschetz condition for constant complex
  coefficients. Vanishing after tensoring with C implies degeneration for
  the rational spectral sequence used in B131.
- B131 applies this only over the smooth parameter locus, where both the
  product family and universal incidence are smooth and projective. It does
  not extend the ordinary local system across the discriminant or imply a
  nonzero boundary stalk.

## S055 - Hilbert schemes of points and uniform relative Serre vanishing

The Stacks Project, current cited tags:
[Hilbert scheme of points, Section 44.2](https://stacks.math.columbia.edu/tag/0B94),
[properness of the fixed-Hilbert-polynomial functor, Lemma 108.7.7](https://stacks.math.columbia.edu/tag/0DPH),
and
[relative Serre vanishing, Lemma 30.16.2](https://stacks.math.columbia.edu/tag/02O1).

- Checked Section 44.2: \(\operatorname{Hilb}^k(X)\) represents finite flat
  degree-\(k\) subschemes and carries the universal finite flat family.
- Checked Lemma 108.7.7: for projective \(X/\mathbf C\), the fixed Hilbert
  polynomial component used for length-\(k\) subschemes is proper.
- Checked Lemma 30.16.2: for a proper morphism over a Noetherian base, a
  coherent sheaf, and a relatively ample line bundle, all positive higher
  direct images vanish after a single sufficiently high twist, uniformly
  over the base.
- B136 applies this to the universal ideal on
  \(X\times\operatorname{Hilb}^k(X)\). Finite flat base change turns the
  resulting pushforward surjection into simultaneous separation of every
  length-\(k\) subscheme by \(L^m\). Only finitely many \(k\le N\) are used.
- Scope guard: the threshold depends on \(X,L,N\). The theorem proves
  bounded-node vanishing, not existence of any growing node configuration or
  nonzero class-specific residue.

## S056 - Small point sets failing degree-d postulation

David Eisenbud, Mark Green, and Joe Harris, “Cayley-Bacharach Theorems and
Conjectures,” *Bulletin of the American Mathematical Society* 33 (1996),
295-324. [Official article PDF](https://www.ams.org/bull/1996-33-03/S0273-0979-96-00666-0/S0273-0979-96-00666-0.pdf).

- Checked Proposition 1, pp. 301-303: for \(r\le2d+2\) distinct points of
  \(\mathbf P^2\), failure to impose independent conditions on degree-\(d\)
  curves occurs exactly when \(d+2\) points are collinear, or when
  \(r=2d+2\) and all points lie on a conic.
- B137 uses only the strict range \(r\le2d+1\), so the conic alternative is
  absent. A generic-projection argument, written out in B137, transfers the
  forced collinear subset from \(\mathbf P^2\) to the fixed very-ample
  embedding \(X\subset\mathbf P^N\).
- Scope guard: Proposition 1 is a postulation theorem for distinct points.
  It neither constructs nodes nor proves isolated first-jet conditions,
  nonzero vanishing-cycle relations, Hodge type, or class-specific pairing.

## S057 - Cayley-Bacharach sets on curves of degree two

Nicola Picoco, “Geometry of Points Satisfying Cayley-Bacharach Conditions
and Applications,” *Journal of Algebra* 631 (2023), 332-354.
[DOI](https://doi.org/10.1016/j.jalgebra.2023.03.042),
[arXiv](https://arxiv.org/abs/2201.01665).

- Checked Theorem A and its \(h=3\) case, Theorem 3.1: if a set
  \(\Gamma\subset\mathbf P^N\) of distinct points is
  \(\mathrm{CB}(k)\) and
  \(|\Gamma|\le3(k-3+3)-1=3k-1\), then \(\Gamma\) lies on a projective
  curve of degree two.
- B138 first extracts an inclusion-minimal dependent evaluation circuit, so
  every coefficient of its unique relation is nonzero and the circuit is
  intrinsically \(\mathrm{CB}(k)\). This verifies that S057 applies in the
  arbitrary ambient projective dimension used there.
- Scope guard: S057 produces only a low-degree carrier. B138 separately
  proves that, for high powers on a fixed smooth \(X\), enough singular
  points on every possible line/conic carrier force a positive-dimensional
  singular locus. Neither theorem constructs a detector or an algebraic
  cycle.

## S058 - Cayley-Bacharach sets on curves of degree three

Nicola Picoco, “Geometry of Points Satisfying Cayley-Bacharach Conditions
and Applications,” *Journal of Algebra* 631 (2023), 332-354.
[DOI](https://doi.org/10.1016/j.jalgebra.2023.03.042),
[arXiv](https://arxiv.org/abs/2201.01665).

- Checked Theorem A and its \(h=4\) case, Theorem 3.2: if a set
  \(\Gamma\subset\mathbf P^N\) of distinct points is
  \(\mathrm{CB}(k)\) and
  \(|\Gamma|\le4(k-4+3)-1=4k-5\), then \(\Gamma\) lies on a projective
  curve of degree three.
- B139 applies this only after B138's minimal-circuit argument has produced
  an intrinsic \(\mathrm{CB}(k)\) set. It separately classifies reduced
  degree-at-most-three carriers and proves a uniform normalization/conormal
  first-jet bound for their bounded Hilbert families.
- Scope guard: Theorem 3.2 supplies a carrier, not a nodal hypersurface,
  vanishing-cycle relation, class-specific residue, or algebraic cycle.
  B139 is only a necessary cardinality obstruction in a fixed high-power
  family.

## S059 - Cayley-Bacharach sets on curves of degree four

Nicola Picoco, “Geometry of Points Satisfying Cayley-Bacharach Conditions
and Applications,” *Journal of Algebra* 631 (2023), 332-354.
[DOI](https://doi.org/10.1016/j.jalgebra.2023.03.042),
[arXiv](https://arxiv.org/abs/2201.01665).

- Checked Theorem A at \(h=5\): for distinct
  \(\Gamma\subset\mathbf P^N\) satisfying \(\mathrm{CB}(k)\),

  \[
   |\Gamma|\le5(k-5+3)-1=5k-11
  \]

  implies that \(\Gamma\) lies on a projective curve of degree four.
- B140 uses the theorem only after extracting the intrinsic minimal
  evaluation circuit. Its separate bounded-component lemma uses S055-style
  Hilbert-family boundedness, uniform regularity, curve duality, and uniform
  conormal slopes to handle singular and reducible quartic carriers.
- Scope guard: S059 neither constructs nodes nor asserts that any carrier
  lies in \(X\). It supplies no vanishing-cycle relation, Hodge pairing, or
  algebraic cycle. Those implications are not attributed to the source.

## S060 - Arbitrary fixed-degree carriers for small CB sets

Ishan Banerjee, “Error terms for the motives of discriminant complements
and a Cayley-Bacharach theorem,” arXiv:2403.07272 (2024).
[arXiv](https://arxiv.org/abs/2403.07272),
[HTML](https://arxiv.org/html/2403.07272v1).

- Checked Theorem 1.13: for each fixed \(e\ge1\) and \(d\gg e\), a
  \(\mathrm{CB}(d)\) set \(Z\subset\mathbf P^N\) with

  \[
   |Z|<ed-f_N(e)
  \]

  lies on a curve of degree at most \(e\). The positive increasing function
  \(f_N\) depends on the ambient dimension but not on \(d\).
- Audited the proof in Section 2. It inducts on projective dimension using
  reduced generic projections (Proposition 2.2), intersects two cones
  (Proposition 2.3), removes the bounded residual set (Proposition 2.4), and
  applies the minimal-carrier lower bound (Proposition 2.5). The base case is
  the plane theorem, Proposition 2.1.
- B141 fixes \(e\) before sending \(d=t_m\) to infinity. B140's uniform
  component lemma then excludes the resulting carrier. Letting the fixed
  integer \(e\) be arbitrary proves a superlinear limit.
- Scope guard: the preprint gives no effective formula for \(f_N(e)\) or
  the threshold hidden in \(d\gg e\). It does not permit \(e=e(d)\), so B141
  claims only \(\omega(d)\), not a quadratic or other explicit floor. It
  constructs no nodes, vanishing-cycle relation, Hodge pairing, or cycle.
- NG156 uses this scope boundary explicitly: S056-S060 concern reduced
  point-value postulation for the adjoint degree. None treats the doubled
  node scheme, first derivatives of the hypersurface line bundle, one-node
  relation completion, or inverse-Hessian transition forms required by
  B191-B193/G124.

## S061 - Obstructed equianalytic hypersurface strata

Anna Gourevitch and Dmitry Gourevitch, “Geometry of obstructed
equisingular families of projective hypersurfaces,” *Journal of Pure and
Applied Algebra* 213 (2009), 1865-1889.
[DOI](https://doi.org/10.1016/j.jpaa.2009.02.012),
[arXiv](https://arxiv.org/abs/0803.2026),
[PDF](https://arxiv.org/pdf/0803.2026).

- Checked p. 13, Theorem 3.1: in the exceptional case \(n=4,d=3\), the
  equianalytic germ of the displayed Fermat-type isolated hypersurface
  singularity is smooth of codimension one less than expected. Remark 3.2
  identifies the generalized exceptional germ as a \(\mathrm{PGL}\)-orbit.
- Checked pp. 25-26, equation (5.2.16): after eliminating coordinate-change
  directions, the remaining obstruction equation has an explicit quadratic
  leading term. This supports treating tangent-rank data and reduced
  smoothness as separate questions.
- B146 does not import the paper's formulas. Its multi-node Hessian
  obstruction is derived directly from analytic critical-point elimination;
  S061 is an adversarial scope check showing that smooth non-expected
  equisingular strata can exist in special orbit-type geometry.
- Scope guard: S061 treats special equianalytic isolated-singularity
  families in projective space. It does not construct a carrier-free
  multinodal excess component on an arbitrary smooth projective variety,
  a rational vanishing-cycle relation, a specified Hodge pairing, or an
  algebraic cycle.

## S062 - Partial first-derivative interpolation

Maria Chiara Brambilla and Giorgio Ottaviani, “On partial polynomial
interpolation,” *Linear Algebra and its Applications* 435 (2011),
1415-1445. [DOI](https://doi.org/10.1016/j.laa.2011.03.024),
[arXiv](https://arxiv.org/abs/0705.4448).

- Checked arXiv v3, pp. 1-3, Theorems 1.1-1.2. In characteristic zero and
  degree \(d\ne2\), general points \(p_i\) with general derivative subspaces
  \(A_i\) impose the expected \(\sum_i(a_i+1)\) conditions, capped by the
  dimension of the polynomial space, except for the five explicitly listed
  cases. Degree two has the separate criterion of Theorem 1.2.
- Checked the local ideal immediately after Theorem 1.2:
  \(\mathfrak m_{p_i}^2\subset I_i\subset\mathfrak m_{p_i}\), and the
  corresponding scheme has length \(a_i+1\). Thus B149's oriented
  half-double scheme on \(\mathbf P^{2n}\) is the case \(a_i=n\).
- None of Theorem 1.1's exceptions matches ambient dimension \(2n\) with
  \(a_i=n\): the even-dimensional exceptions use full double points
  \(a_i=2n\), while the remaining exceptions have odd ambient dimension.
  B150 therefore obtains maximal rank for general oriented half-doubles in
  projective space when \(d\ne2\).
- Scope guard: the theorem concerns general points and general partial
  derivative subspaces on projective space. G094 requires a highly special
  configuration on an arbitrary \(X\), compatible with prescribed nodal
  Hessians, nonlinear smooth excess, vanishing cycles, and a specified
  Hodge pairing. Generic maximal rank proves no nonexistence for that special
  locus.

## S063 - Interpolation on curvilinear jets

J. Alexander and A. Hirschowitz, “Interpolation on Jets,” *Journal of
Algebra* 192 (1997), 412-417.
[arXiv](https://arxiv.org/abs/alg-geom/9703028).

- Checked pp. 1-3, Definition 1.1 and Theorem 1.2. For lines in general
  position and generic curvilinear jets of prescribed lengths on those
  lines, the degree-\(d\) evaluation map has maximal rank exactly under the
  stated numerical condition \(C(n,d)\).
- A B149 local half-double scheme is the union of \(n\) independent
  length-two curvilinear jets **with the same support**. S063's theorem uses
  a generic union of point-line pairs and does not cover this collision.
  Splitting the common support changes the nodal scheme and cannot be used
  as an equality or a detector-preserving deformation.
- Scope guard: S063 is useful as generic-independence evidence and as a
  degeneration input, not as a theorem about the special coalesced oriented
  schemes required by G094.

## S064 - Differential degeneration of zero-dimensional schemes

Laurent Evain, “Dimension of linear systems: a combinatorial and
differential approach,” arXiv:alg-geom/9709032 (1997).
[arXiv](https://arxiv.org/abs/alg-geom/9709032).

- Checked pp. 1 and 12, Theorems 13-14. Under the displayed residual-slice
  equalities, a monomial staircase scheme may be specialized toward a
  divisor, and the limiting linear system is contained in an explicitly
  described residual system. Semicontinuity then gives the asserted upper
  bound on the dimension through a general staircase scheme.
- This supplies a rigorous framework for testing collisions or
  specializations of B149's oriented schemes. The inequality direction does
  not construct a special superabundant scheme, prove that a proposed limit
  retains nodal Hessians, or transport a vanishing-cycle/Hodge pairing.
- Scope guard: no Evain degeneration is counted toward G094 until its trace,
  residual, flatness, Hessian, integration, and specified-pairing data are
  all verified for the actual family.

## S065 - Serre vanishing and global generation for coherent twists

Jean-Pierre Serre, “Faisceaux algébriques cohérents,” *Annals of
Mathematics* (2) **61** (1955), 197–278.
[Primary scan hosted by Collège de France](https://www.college-de-france.fr/media/jean-pierre-serre/UPL5435398796951750634_Serre_FAC.pdf).

- Checked no. 65, Proposition 7, and no. 66, Theorem 2, journal pp. 258–260.
  For a coherent algebraic sheaf on a projective variety, sufficiently high
  twists have vanishing higher cohomology and are generated by global
  sections.
- B157 applies the vanishing statement to the ideal sheaf of the fixed
  length-three infinitesimal neighborhoods of finitely many points. The
  resulting exact sequence makes the prescribed two-jet evaluation map
  surjective. Global generation of the same twisted ideal supplies the
  basepoint-free variation away from those points used by Bertini.
- NG134 uses the same fixed finite-jet surjectivity only to choose two
  global deformation sections with specified values and gradients at two
  ODPs. Their span is an affine-linear projective slice, and the nonzero
  quadratic critical-value term is fixed by those first jets. This does
  not assert rank deficiency for the full complete system.
- NG135 uses another pair of prescribed gradients, now forming a
  hyperbolic cross-term, to realize the mixed Hessian obstruction while
  the critical-value ideal itself is smooth. Again only the finite-jet
  obstruction, not full-system rank deficiency, is imported.
- NG153 applies the same theorem in the opposite direction. For a fixed
  finite point scheme and a sufficiently high twist, the exact sequence
  makes full first-jet evaluation surjective. Thus every value and every
  node-isolated gradient direction occurs in the complete linear system;
  a synchronized defect engineered inside a selected subfamily is not a
  defect of the full universal incidence.
- B198 applies global generation and higher-cohomology vanishing to the
  kernel of a finite presentation of \(I_ZH^r\). This proves finite
  generation of the section ideal and therefore a largest minimal-generator
  degree for fixed \(Z\).
- NG160 combines that generator ceiling with the already audited eventual
  first-jet surjectivity. The two asymptotic conclusions exclude, rather
  than construct, G128's adjacent primitive birth.
- NG164 applies the same FAC vanishing theorem to \(I_Z^3H^m\). Vanishing
  makes the complete two-jet evaluation surjective, so it is incompatible
  with G130's nontrivial value relation and one-node-dimensional
  conditional-gradient defect. G132 therefore needs selective kernel
  membership, not blanket Serre vanishing.
- Scope guard: the power depends on the fixed finite point scheme. This
  theorem gives jet interpolation; it neither makes the analytic base map
  linear nor supplies a vanishing-cycle relation, Hodge type, or specified
  pairing.

## S066 - Zero microsupport and local constancy

Masaki Kashiwara and Pierre Schapira, *Sheaves on Manifolds*, Grundlehren
der mathematischen Wissenschaften 292, Springer, 1990.
[Official book record](https://link.springer.com/book/10.1007/978-3-662-02661-8);
[official micro-support chapter, pp. 217–248](https://link.springer.com/chapter/10.1007/978-3-662-02661-8_7).

- Audited Proposition 5.4.5 for the exact criterion used in B163: a
  constructible derived sheaf has microsupport contained in the zero section
  if and only if its cohomology sheaves are locally constant. The official
  chapter summary describes microsupport as the failure-of-propagation
  codirections and records the functorial/non-characteristic framework.
- Cross-checked the proposition number and formulation against later
  microlocal-sheaf literature explicitly citing KS Proposition 5.4.5 for
  the same zero-section/local-system equivalence.
- B163 applies the theorem only to
  \(K_B=Rg_*\mathbf Q_{\mathcal Y_B}\) on the smooth analytic germ \(F_B\).
  Constructibility follows from the proper algebraic/analytic family.
- Scope guard: zero microsupport is required **after** base change to the
  proposed basis-node germ. The ambient direct image over the full linear
  system has discriminant microsupport. Proposition 5.4.5 supplies no
  class-specific Hodge type, Saito pairing, or algebraic cycle.

## S067 - Characteristic cycles, microlocal index, and positivity

Masaki Kashiwara, “Index theorem for constructible sheaves,”
*Astérisque* 130 (1985), 193–209.
[Primary full text at Numdam](https://www.numdam.org/item/AST_1985__130__193_0/).

Victor Ginsburg, “Characteristic varieties and vanishing cycles,”
*Inventiones Mathematicae* 84 (1986), 327–402.
[Official article record](https://link.springer.com/article/10.1007/BF01388811).

A. A. Beilinson, J. Bernstein, and P. Deligne, *Faisceaux pervers*,
*Astérisque* 100 (1982), 5–171.
[Primary full text at Numdam](https://archive.numdam.org/item/AST_1982__100__1_0.pdf).

- Audited Kashiwara Definition 3.4 and Theorem 4.1: generic microlocal
  Morse Euler multiplicities assemble into a Lagrangian characteristic
  cycle. Theorems 4.2–4.3 give the index/intersection formula, and
  Proposition 5.1 is the local transverse Morse calculation used in B165.
- Audited BBD Sections 2 and 4.4 for perverse truncation and the
  vanishing-cycle bounds. At a generic complex conormal, the normalized
  normal Morse group of a perverse sheaf is concentrated in degree zero;
  its characteristic-cycle coefficient is therefore a nonnegative
  dimension. This is the effectivity input in B165.
- Ginsburg is the primary regular-holonomic comparison around
  characteristic varieties and vanishing cycles. B165 uses it only as a
  Riemann–Hilbert cross-check; the proof is stated on the rational
  constructible-sheaf side.
- Shift guard: the characteristic cycle of a general derived complex is a
  Grothendieck-group invariant and changes sign under a shift. B165 instead
  defines the non-alternating sum over canonical perverse cohomology
  objects. NG131 shows why these must not be confused.
- Scope guard: none of these microlocal theorems constructs a
  class-directed nodal germ, proves a specified Hodge type or pairing, or
  supplies an algebraic cycle.

## S068 - Microlocal inverse image and higher discriminants

Masaki Kashiwara and Pierre Schapira, *Sheaves on Manifolds*, Grundlehren
der mathematischen Wissenschaften 292, Springer, 1990.
[Official book record](https://link.springer.com/book/10.1007/978-3-662-02661-8);
[open precursor, *Microlocal Study of Sheaves*, Astérisque 128](https://www.numdam.org/issues/AST_1985__128__1_0/).

Luca Migliorini and Vivek Shende, “Higher discriminants and the topology
of algebraic maps,” *Algebraic Geometry* 5 (2018), 114–130.
[Primary open-access article](https://content.algebraicgeometry.nl/2018-1/2018-1-004.pdf),
[arXiv:1307.4059](https://arxiv.org/abs/1307.4059).

- Audited Kashiwara--Schapira Corollary 6.4.4 and Remark 6.2.8(i) for
  B167: if \(i:M\hookrightarrow N\) is a closed embedding, then
  \(SS(i^{-1}K)\subseteq i^\#SS(K)\). The operation \(i^\#\) uses a normal
  cone and remains meaningful in the characteristic case; it is not the
  pointwise quotient of covector fibers.
- Audited Migliorini--Shende equation (2.2), Theorem 2.7, Lemma 2.12, and
  Theorems A--C. For a proper map of smooth characteristic-zero varieties,
  \(SS(Rf_*\mathbf Q)\subseteq f^\dagger(0)\), and the latter is the union
  of conormals to codimension-\(a\) components of the higher discriminants.
  Their Lemma 2.12 detects these loci by generic complete-intersection
  slices and vanishing cycles.
- Cancellation guard: Theorem A is stated for the characteristic cycle of
  the pushed-forward constructible function, while Theorem B concerns
  supports of decomposition summands. The article explicitly warns that
  constructible-function singular support can be strictly smaller than
  sheaf microsupport through cancellation. G106 therefore uses the full
  sheaf microsupport or the larger Theorem C envelope, never Theorem A as
  an equality for the sheaf.
- Application check: the base \(P=|L|\) and the universal hypersurface
  incidence \(\mathcal U\) are smooth for basepoint-free \(L\), and
  \(h:\mathcal U\to P\) is projective, so the smooth-source hypotheses used
  in B167 are satisfied.
- B169 audit: equation (2.2) identifies the envelope fiber with covectors
  annihilating one actual differential image; it does not take the linear
  span of annihilators coming from distinct critical points. In an
  exhaustive ODP neighborhood this gives exactly the zero section plus
  the individual nodal conormals. Equation (2.6) places the singular
  support of the pushed-forward Euler function inside the full sheaf
  microsupport; the nonzero generic one-ODP Euler jump therefore proves
  that every nodal conormal really occurs.
- Inverse-image audit for B169: the coordinate description in
  Kashiwara--Schapira Remark 6.2.8(i) gives zero \(i^\#\)-image when a
  smooth divisor contains the smooth pullback germ. For the converse,
  Corollary 6.4.4 applied to \(\mathbf Q_D\) detects the nonzero conormal of
  the reduced pullback divisor, including high-order contact \(y^m=0\).
- Scope guard: higher discriminants constrain ambient characteristic
  geometry. They do not prove microlocal absorption by a chosen
  class-directed germ, a nonzero Saito pairing, or algebraicity of a Hodge
  class.

## S069 - Jacobi global residues and the Cayley--Bacharach guard

Alekos Vidras and Alain Yger, “On some generalizations of Jacobi's residue
formula,” *Annales scientifiques de l'École Normale Supérieure* 34 (2001),
131--157. [Primary article and metadata](https://www.numdam.org/articles/10.1016/s0012-9593(00)01056-9/),
[primary PDF](https://www.numdam.org/article/ASENS_2001_4_34_1_131_0.pdf).

Eduardo Cattani, David Cox, and Alicia Dickenstein, “Residues in Toric
Varieties,” *Compositio Mathematica* 108 (1997), 35--76.
[arXiv:alg-geom/9506024](https://arxiv.org/abs/alg-geom/9506024).

- Audited Vidras--Yger equation (1.2) and Theorem 1.1: if a polynomial map
  \(P=(P_1,\ldots,P_d)\) has the stated Jacobi/properness condition, then the
  global residue of \(Q\) vanishes for
  \(\deg Q<\sum_j\delta_j-d\). Under the classical highest-homogeneous-part
  condition this is \(\deg Q\le\sum_j\deg P_j-d-1\).
- At a simple zero, the local residue is \(Q(p)/J_P(p)\). Applied to
  \(P=\nabla f_t\), this gives the inverse-Hessian weights used in B172.
- Audited Vidras--Yger Theorem 4.1: below the same critical degree, a
  hypersurface through all but one simple zero must contain the last. This
  Cayley--Bacharach consequence is a direct warning that low-degree
  selectors cannot be assumed freely.
- Cattani--Cox--Dickenstein is retained as primary toric context: on a
  simplicial complete toric variety, the toric residue is a sum of local
  residues. B172 does not import a toric selector or projective-boundary
  theorem from it.
- Scope guard: these residue theorems sum over complete critical schemes and
  impose degree/Newton-polytope and infinity hypotheses. They do not select
  the tracked nodes, produce Hodge type or rational structure, or prove a
  nonzero Saito pairing.

## S070 - Residual complete-intersection evaluation duality

Leah Gold, John Little, and Hal Schenck, “Cayley--Bacharach and
evaluation codes on complete intersections,” *Journal of Pure and Applied
Algebra* 196 (2005), 91--99.
[Primary arXiv manuscript](https://arxiv.org/abs/math/0311129),
[journal DOI](https://doi.org/10.1016/j.jpaa.2004.08.015).

E. Davis, A. V. Geramita, and F. Orecchia, “Gorenstein algebras and the
Cayley--Bacharach theorem,” *Proceedings of the American Mathematical
Society* 93 (1985), 593--597.
[DOI](https://doi.org/10.1090/S0002-9939-1985-0776185-6).

- Audited Gold--Little--Schenck Section 1.1 and the exact sequence on
  pp. 2--3: the cokernel of degree-\(a\) evaluation on a finite projective
  point set is \(H^1(I_\Gamma(a))\).
- Audited their Definition 1.1 and Theorem 1.2, which restate the
  Davis--Geramita--Orecchia theorem. For residual subschemes
  \(\Gamma',\Gamma''\) of a complete intersection of type
  \((d_1,\ldots,d_r)\), with
  \(s=\sum_i d_i-r-1\),
  \[
  h^0(I_{\Gamma'}(a))-h^0(I_\Gamma(a))
  =h^1(I_{\Gamma''}(s-a)).
  \]
- Audited Gold--Little--Schenck Lemma 3.4: the complete-intersection
  Artinian reduction has symmetric Hilbert function. This is the dimension
  guard behind the complementary evaluation spaces used in B173.
- B173 applies Theorem 1.2 with \(\Gamma'=A_t\),
  \(\Gamma''=T_t\), and \(a=e=s-m\). The residue weights and orthogonality
  come separately from S069; no coding-theory minimum-distance statement is
  used.
- NG161 uses only B199's elementary generator-kernel exact sequence. S070's
  residual complete-intersection duality can compute special Hilbert
  dimensions, but it does not create the extra double-generator line,
  prove ODP Hessians, or extend that package to an arbitrary polarized
  variety and specified Hodge class.
- Scope guard: the theorem computes residual evaluation dimensions for a
  projective complete intersection. It does not supply analytic constancy in
  a family, an arbitrary-variety residue theorem, Hodge type, or a detector
  pairing.

## S071 - Saito's criterion for free divisors

Kyoji Saito, “Theory of logarithmic differential forms and logarithmic
vector fields,” *Journal of the Faculty of Science, University of Tokyo,
Section IA, Mathematics* 27 (1980), no. 2, 265–291.
[Primary repository record and scan](https://repository.dl.itc.u-tokyo.ac.jp/records/39646).

Francisco J. Calderón-Moreno, “Logarithmic differential operators and
logarithmic de Rham complexes relative to a free divisor,” *Annales
scientifiques de l'École Normale Supérieure* 32 (1999), 701–714.
[Primary full text at Numdam](https://www.numdam.org/item/10.1016/S0012-9593(01)80004-5/).

Michele Torielli, “Deformations of free and linear free divisors,”
*Annales de l'Institut Fourier* 63 (2013), 2097–2136.
[Primary full text at Numdam](https://www.numdam.org/item/10.5802/aif.2824/).

- Audited Calderón-Moreno Section 1.1, pp. 702–703: for a reduced local
  equation \(f\), logarithmic derivations are those \(\delta\) satisfying
  \(\delta(f)\in(f)\). The displayed Saito criterion says that this module
  is free exactly when \(n\) logarithmic derivations have coefficient
  determinant equal to a unit times \(f\); those derivations then form a
  basis.
- Cross-checked the exact attribution against Torielli Proposition 2.8,
  which identifies it as Saito's Theorem 1.8 and states both the
  determinant criterion and the basis conclusion. Torielli Proposition
  2.11 gives the equivalent formal matrix form.
- Audited the dimension-two guard in Calderón-Moreno pp. 702 and 713 and
  Torielli p. 2100: logarithmic derivation modules of reduced plane-curve
  divisors are locally free. B175 does not rely on that blanket fact; it
  supplies its own two-column Saito matrix.
- B175 applies the criterion only after proving directly that
  \(F=x(x+y^2)\) is reduced, both displayed vector fields are logarithmic,
  and their determinant is \(-4F\).
- Scope guard: free-divisor theory controls the reduced principal ideal
  \((F)\) and tangent vector fields along \(V(F)\). It does not identify the
  labelled simultaneous ideal \((\tau_1,\ldots,\tau_N)\), its minimal
  generators, the hidden-generator space \(H_\tau\), a rational Hodge
  class, or a Saito detector pairing.

## S072 - Effective degree bounds for Groebner elimination

Thomas W. Dube, "The Structure of Polynomial Ideals and Groebner Bases,"
*SIAM Journal on Computing* 19 (1990), 750-773.
[Official journal record](https://epubs.siam.org/doi/10.1137/0219053).

- Audited the paper abstract and official bibliographic record. If an ideal
  in \(K[x_1,\ldots,x_m]\) is generated by polynomials of total degree at
  most \(d\), Dube gives, for every admissible monomial order, the bound
  \[
  2\left(d^2/2+d\right)^{2^{m-1}}
  \]
  for the total degrees occurring in a Groebner basis.
- A lexicographic order therefore supplies a finite, explicit, generally
  very large elimination bound once the complete polynomial presentation,
  localization variables, and ambient-variable count have been fixed.
- B184 does not need this bound for its local Bezout argument. G117 uses it
  only to justify that carrier and numerator degrees are in principle
  computable from a fully specified algebraic incidence.
- Scope guard: a Groebner degree bound does not choose the correct local
  component, prove that it is smooth or etale, make a collided value
  polynomial simple, prove conormal-jet vanishing, preserve the Hodge
  detector clauses, or prove the Hodge Conjecture.

## S073 - Terracini's lemma and tangential contact loci

Luca Chiantini and Ciro Ciliberto, “On the Dimension of Secant Varieties,” arXiv:0812.1904 (2008).
[arXiv](https://arxiv.org/abs/0812.1904).

- Audited Section 3, Theorem 3.1, preprint pp. 5–6: for general smooth points and a general point of their span, the tangent space to the join/secant is the span of the embedded tangent spaces.
- Audited Definition 3.4 and the surrounding discussion, preprint pp. 6–7: the tangential contact locus consists of points whose tangent spaces lie in this tangent-space span.
- NG159 scope: the theorem concerns general points in one embedding, and containment is in the span of tangent spaces. G127 instead requires one special marked set, fixed across all lower-power embeddings, with each tangent space inside the generally smaller span of the marked points.
- No ordinary-double-point, doubled-scheme, Hessian-holonomy, Hodge-type, or rational-detector conclusion is supplied.

## S074 - Gaussian maps from the diagonal and second-fundamental-form scope

Giuseppe Pareschi, “Gaussian Maps and Multiplication Maps on Certain
Projective Varieties,” *Compositio Mathematica* **98** (1995), 219–268.
[Numdam PDF](https://www.numdam.org/item/CM_1995__98_3_219_0.pdf).

Paola Frediani, “Second Fundamental Form and Higher Gaussian Maps,”
arXiv:2208.14794v2 (2023).
[arXiv](https://arxiv.org/abs/2208.14794).

- Audited Pareschi Section 1(A), journal pp. 223–224 (PDF pp. 5–6): the
  \(k\)-th Gaussian map is induced by successive powers of the ideal of the
  diagonal in \(X\times X\); its input is a space of global relations and
  its target is a global symmetric-cotangent section space.
- Audited Pareschi Theorem C and surrounding scope, journal pp. 220–222
  (PDF pp. 2–4): the displayed higher-dimensional surjectivity application
  concerns ample line bundles on abelian varieties with explicit power
  bounds. Section 3 then specializes to smooth projective curves.
- Audited Frediani Introduction, pp. 1–4, especially Theorems 1.1–1.3:
  the second-fundamental-form comparison is for the Torelli map of smooth
  canonical curves and is evaluated on Schiffer and higher Schiffer
  variations.
- Field audit: Pareschi works over an algebraically closed field, with the
  paper's curve applications in characteristic zero; Frediani works over
  the complex numbers. This is compatible with G137's base field but does
  not widen either theorem's geometric scope.
- G137 scope guard: neither source contains a finite marked scheme \(Z\),
  the relation weights \(S_m^\perp\), a central nodal inverse Hessian, or
  the dual connecting map associated with
  \(0\to I_Z^3H^k\to I_Z^2H^k\to(I_Z^2/I_Z^3)H^k\to0\).
- Consequently Gaussian-map surjectivity is not a proof of G137 without a
  new comparison morphism respecting all four structures. No arbitrary
  Hodge class, rational detector, algebraic cycle, or general Hodge
  Conjecture conclusion is supplied.

## S075 - Higher Terracini lemmas for osculating spaces

Edoardo Ballico and Claudio Fontanari, “A Terracini Lemma for Osculating
Spaces with Applications to Veronese Surfaces,” arXiv:math/0406321 (2004),
published in *Journal of Pure and Applied Algebra* **195** (2005), 1–6.
[arXiv PDF](https://arxiv.org/pdf/math/0406321).

Edoardo Ballico, Cristiano Bocci, Enrico Carlini, and Claudio Fontanari,
“Osculating Spaces to Secant Varieties,” arXiv:math/0406322 (2004).
[arXiv PDF](https://arxiv.org/pdf/math/0406322).

- Audited Ballico–Fontanari Lemma 2, preprint pp. 3–4: for general marked
  points, the tangent space to a join of prescribed osculating spaces is
  contained in the span of the next osculating spaces; equality requires
  additional dimension hypotheses. The applications concern Veronese
  surfaces and explicit secant-defect ranges.
- Audited Ballico–Bocci–Carlini–Fontanari Theorem 1, preprint pp. 1–2: for
  general points \(p_i\) and a general point of their secant span, the
  order-\(r\) osculating space of the secant variety is the span of the
  order-\(r\) osculating spaces of \(X\) at the \(p_i\).
- Field and scope audit: both papers work with complex integral
  nondegenerate projective varieties, but their decisive statements use
  general points and secant/osculating varieties. Their explicit
  interpolation applications are for Veronese surfaces or
  \(\mathbf P^3\).
- G139 scope guard: neither theorem says that the span of the point lines
  \(S_Z^{(0)}\) contains \(S_Z^{(2)}\), produces the adjacent power
  transition \(H^{m-1}\to H^m\), selects a one-dimensional nondegenerate
  profile, or retains an arbitrary Hodge-class detector.
- Thus higher Terracini theory is relevant language and a possible source
  of future comparison maps, but the cited theorems do not construct G139
  or prove the Hodge Conjecture.

## S076 - Gotzmann regularity and finite-scheme separation

Gerd Gotzmann, “Eine Bedingung für die Flachheit und das Hilbertpolynom
eines graduierten Ringes,” *Mathematische Zeitschrift* **158** (1978),
61–70, DOI 10.1007/BF01214566.
[EuDML record](https://eudml.org/doc/172619).

Jarosław Buczyński, Adam Ginensky, and J. M. Landsberg, “Determinantal
Equations for Secant Varieties and the Eisenbud–Koh–Stillman Conjecture,”
*Journal of the London Mathematical Society* **88** (2013), 1–24,
arXiv:1007.0192.
[arXiv](https://arxiv.org/abs/1007.0192).

- Audited Buczyński–Ginensky–Landsberg Proposition 2.1.2, preprint p. 6:
  Gotzmann regularity makes the ideal of every zero-dimensional
  projective scheme of degree \(\ell\) be \(\ell\)-regular.
- Audited their Lemma 2.1.3 on the same page: after a degree
  \(k\ge\ell-1\) Veronese re-embedding, such a scheme spans a projective
  \((\ell-1)\)-plane. Equivalently, degree-\(k\) polynomials restrict
  surjectively to it.
- Transfer audit for B212: if \(H\) embeds \(X\) into projective space,
  the restrictions to \(X\) of ambient degree-\(k\) polynomials are
  global sections of \(H^k\). Ambient separation therefore proves that
  \(H^k\) separates every subscheme of \(X\) of length at most \(k+1\);
  projective normality is not assumed.
- Scope guard: the cited regularity theorem controls finite-scheme Hilbert
  functions. It constructs no special fat-point dependence, Hodge
  detector, algebraic cycle, or general Hodge Conjecture conclusion.

## S077 - Togliatti systems, WLP, and osculating defect

Emilia Mezzetti, Rosa M. Miro-Roig, and Giorgio Ottaviani, “Laplace
Equations and the Weak Lefschetz Property,” *Canadian Journal of
Mathematics* **65** (2013), 634–654, arXiv:1110.5239.
[arXiv](https://arxiv.org/abs/1110.5239).

Mateusz Michalek and Rosa-Maria Miro-Roig, “Smooth Monomial Togliatti
Systems of Cubics,” *Journal of Combinatorial Theory, Series A* **143**
(2016), 66–87, arXiv:1310.2529.
[arXiv](https://arxiv.org/abs/1310.2529).

- Audited Mezzetti-Miro-Roig-Ottaviani Introduction and Theorem 3.2:
  under its generator bound and artinian hypotheses, failure of WLP in
  degree \(d-1\), dependence after restriction to a general hyperplane,
  and a Laplace equation of order \(d-1\) for the apolar projected
  Veronese variety are equivalent.
- Audited their Section 4 scope: explicit classifications concern monomial
  cubic linear systems in dimensions at most three, with additional
  special projected-Veronese examples. The osculating condition is a
  dimension defect at a general point.
- Audited Michalek-Miro-Roig Introduction and Theorem 3.4 scope: the paper
  classifies smooth minimal *monomial* Togliatti systems of cubics; the
  associated varieties are smooth toric projected Veronese varieties.
- Field audit: the decisive WLP discussion is over an algebraically closed
  field of characteristic zero. This covers complex examples but does not
  enlarge them to arbitrary smooth projective complex varieties.
- G145/NG178 scope guard: neither paper proves equality of the full affine
  second osculating spaces at all points of one prescribed marked scheme,
  nor constructs a central ODP profile, full-support nodal relation,
  holonomy/congruence package, rational type-\((0,0)\) detector, specified
  Hodge-class pairing, algebraic cycle, or the general Hodge Conjecture.

## S078 - Zak tangency and ordinary Gauss fibers

Luca Chiantini and Ciro Ciliberto, “On the Dimension of Secant
Varieties,” *Journal of the European Mathematical Society* **12** (2010),
1267–1291.
[EMS article](https://ems.press/journals/jems/articles/1932).

Katsuhisa Furukawa and Atsushi Ito, “On Separable Higher Gauss Maps,”
*Michigan Mathematical Journal* **68** (2019), 483–503,
arXiv:1702.06010.
[arXiv](https://arxiv.org/abs/1702.06010).

- Audited Chiantini-Ciliberto Section 4, especially Definition 4.1,
  Remark 4.2, and Theorem 4.4, journal pp. 1276–1277: if a linear space
  \(L\) is J-tangent to \(X\) along \(Y\), then
  \(\dim L\ge\dim X+\dim Y\); for \(X\) smooth along \(Y\), containment
  of the embedded tangent space at a general point is the relevant
  tangency condition.
- Audited Furukawa-Ito Introduction and Theorem 1.1: for a separable
  \(m\)-th Gauss map, the contact locus of a *general* tangent
  \(m\)-plane is a linear variety. Their discussion immediately after
  Theorem 1.1 records the ordinary \(m=n\) birational conclusion in the
  smooth characteristic-zero setting.
- B218 transfer: a positive-dimensional ordinary Gauss fiber would make
  its common \(d\)-plane tangent along a positive-dimensional subvariety,
  contradicting the Zak inequality. Projectivity then makes the map
  finite; general-contact linearity makes its general fiber one point.
- G146/NG179 scope guard: neither theorem bounds the cardinality or
  scheme length of a deliberately special zero-dimensional Gauss fiber.
  Neither supplies a marked nodal profile, relation, rational Hodge
  detector, specified pairing, algebraic cycle, or the Hodge Conjecture.

## S079 - Bertini away from the base locus

Phillip Griffiths and Joseph Harris, “Algebraic Geometry and Local
Differential Geometry,” *Annales scientifiques de l'École Normale
Supérieure* **12** (1979), 355–452.
[NUMDAM PDF](https://www.numdam.org/article/ASENS_1979_4_12_3_355_0.pdf).

- Audited Appendix (b), statement (A.6), journal p. 440: the generic
  member of a linear system of hypersurfaces in projective space is smooth
  outside the base locus. The following discussion derives the statement
  from the rational map defined by the system and Sard/Bertini.
- B219 first applies it to the projective linear system spanned by one
  section with prescribed ODP two-jets and the kernel
  \(H^0(I_{3Z}(e))\). The explicit cubed-separator product proves that
  its base locus is contained in \(Z\).
- B219 then applies it to the projective span of \(f\) and all
  \(x_0G\). Its base locus is the fixed hyperplane section \(Y\); the
  proof separately checks smoothness at smooth points and nodes of \(Y\),
  so Bertini is used only off that base.
- Scope guard: Bertini chooses smooth members in these special linear
  systems. It neither transfers the construction to an arbitrary fixed
  variety nor supplies a Hodge detector, specified pairing, algebraic
  cycle, or the Hodge Conjecture.

## S080 - Higher-order embeddings and tensor-product scope

Thomas Bauer and Tomasz Szemberg, “Higher Order Embeddings of Abelian
Varieties,” *Mathematische Zeitschrift* **224** (1997), 449–455.
[Author-hosted published text](https://www.mathematik.uni-marburg.de/~tbauer/1997-Higher-order-embeddings.pdf).

- Audited Introduction, p. 1: \(k\)-very ampleness is surjectivity onto
  every length-\(k+1\) finite subscheme, while \(k\)-jet ampleness is the
  displayed simultaneous fat-point restriction condition. The paper
  records the implications jet ample => very ample => spanned in the
  corresponding order.
- Audited Theorem 2.1 and Corollaries 2.2–2.3, pp. 3–5: the quantitative
  tensor-product jet-ampleness results are for line bundles on complex
  abelian varieties, using translations and ample divisors.
- B220 scope: its arbitrary-X Gauss injectivity does not import those
  abelian theorems. It directly multiplies one A-section and one B-section,
  each vanishing at \(p\) and nonzero at \(q\), to obtain an
  \(A\otimes B\)-section in \(\mathfrak m_p^2\) but nonzero at \(q\).
- Scope guard: neither higher-order embedding terminology nor the abelian
  jet theorem creates G147's exceptional common-tangent fiber, rational
  detector, specified Hodge pairing, algebraic cycle, or the Hodge
  Conjecture.

## Citation policy for incompletely audited mechanisms

Spreading out, products/fibrations, and cycle-class rigidity remain recorded
only at the mechanism/obstruction level. Before any dependent brick is
promoted, its exact primary theorem must receive a new `S...` record with
matching field, coefficients, cohomology, and scope. Seeded sources above must
likewise be upgraded to page/theorem-level checks before decisive use.
