# Verification ledger

| ID | Claim | Label | Evidence | Remaining risk |
|---|---|---|---|---|
| D001 | exact official rational statement is fixed | PROVED | Deligne/Clay pp. 1-2; `problem-statement.md` | none beyond convention checks |
| L001 | algebraic cycle classes are of Hodge type | PROVED | standard cycle-class theorem; Deligne p. 1 | formalization absent |
| K001 | \(p=1\), \(p=n-1\), and \(n\le3\) cases | PROVED | Lefschetz (1,1), hard Lefschetz | primary-source audit can be expanded |
| B001 | universal HC iff universal middle HC | PROVED | `proofs/B001-middle-degree-reduction.md` | proof-assistant formalization absent |
| RC0 | a dominating relative cycle with fixed class gives fiberwise algebraicity | PROVED | functoriality/proper base change; encoded in G002 attempt | family singularities/base change must stay explicit |
| B002 | smooth Hilbert point plus tangent surjectivity forces component dominance and fiberwise cycles | PROVED | `proofs/B002-hilbert-dominance-criterion.md` | exact formalization absent |
| B003 | semiregular lci cycles lift along first-order Hodge-preserving deformations | PROVED | Bloch theorem 7.1; `proofs/B003-semiregular-infinitesimal-bridge.md` | first-order only; exact original-page audit incomplete |
| B004 | injectively combined semiregular lci presentations propagate over an irreducible Hodge base | PROVED | Ran Theorem 0(ii), BF 5.2/7.8-7.10, B002; `proofs/B004-semiregular-presentation-propagation.md` | conventional proof only; tuple-linearity not formalized |
| B005 | direct-sum augmentation cannot repair a noninjective combined semiregularity map | PROVED | exact linear-algebra proof in `proofs/B005-no-augmentation-repair.md` | applies only to appending, not replacing a presentation |
| B006 | B001 point products acquire the extra obstruction space H^1(O_Z)^r | PROVED | product normal bundle and Kunneth calculation in `proofs/B006-projective-product-obstruction.md` | product semiregularity map on the new summand not computed |
| B007 | universal HC iff every nonzero primitive rational middle Hodge class has a nonzero singular-hyperplane restriction | PROVED | BFNP Theorem 1.3, Corollary 5.15, Lemma 6.2, Theorems 6.5-6.6; `proofs/B007-normal-function-equivalence.md` | imported conventional proof; mixed-Hodge-module machinery not formalized |
| B008 | a smooth discriminant point has zero rational local IH singularity channel | PROVED | BFNP Theorem 2.11, equation (5.13), Corollary 5.15; `proofs/B008-smooth-discriminant-exclusion.md` | imported conventional proof; local IH calculation not formalized |
| B009 | in the transverse nodal local model, the local IH/monodromy channel is the relation space of vanishing cycles | PROVED | Green-Griffiths Sections 4.2.3-4.2.4; `proofs/B009-nodal-relation-channel.md` | scope is restricted to the stated local/quasi-local normal-crossing hypotheses |
| B010 | Saito's type-(0,0) relation class pairs nontrivially with zeta iff the chosen singular hyperplane detects zeta | PROVED | Saito Theorems 1-3 and Proposition 1; proofs/B010-saito-local-pairing-criterion.md | imported mixed-Hodge proof; universal existence is not supplied |
| B011 | global monodromy tubes surject onto rational primitive middle cohomology when vanishing homology is nonzero | PROVED | Schnell Theorem 1; proofs/B011-global-tube-surjectivity.md | tubes are topological/global, not algebraic or local singularity classes |
| G001 | every middle class has an algebraic anchor in a connected Hodge locus | EXPLORATORY | no proof | may be as hard as HC |
| G002 | anchored Hodge locus is dominated by relative cycle space | CONDITIONAL | sufficient theorem formulated; proof only when dominance is assumed | dominance is the open content |
| G003 | every anchored class has a B002-good cycle representative | EXPLORATORY | no proof; semiregularity source seeded | likely fails without strong lci/obstruction hypotheses |
| G004 | every algebraic anchor has an injectively combined semiregular lci presentation | EXPLORATORY | no proof; precise falsifier recorded | moving and K-theory generation do not control injectivity |
| G005 | every primitive rational middle Hodge class is detected on a singular hyperplane section | EXPLORATORY | exact terminal-equivalent theorem formulated; BFNP computes singularity as restriction | class-specific nonvanishing is exactly the open content |
| G006 | every primitive rational middle Hodge class admits a nodal vanishing-cycle relation with nonzero class-specific pairing | EXPLORATORY | B009 makes the local target concrete; Thomas proves terminal equivalence after universal quantification | the pairing nonvanishing is exactly the open content |
| G007 | every global tube detector for a primitive Hodge class can be replaced by a type-(0,0) relation detector at one singular member | EXPLORATORY | B010 gives the local target and B011 gives the global detector | no theorem concentrates a global loop cancellation at one higher discriminant stratum |
| NG-001 | CDK algebraicity alone implies G002 | NO-GO | logical audit in `no-go-ledger.md` | none; route requires a new input |
| NG-004 | Bloch semiregularity is automatic for arbitrary anchor cycles | NO-GO | hypothesis audit in `no-go-ledger.md` | exact positive scope still needs deep source audit |
| NG-005 | moving/K-theory generation supplies a G004 presentation | NO-GO | logical obstruction in `no-go-ledger.md` | requires a new stabilization theorem |
| NG-006 | add cancelling positive/rationally trivial cycles to force G004 injectivity | NO-GO | B005 restriction argument | replacement operations remain untested |
| NG-007 | semiregularity automatically survives B001 projective-space products | NO-GO | B006 extra-summand calculation | may survive under H^1(O_Z)=0 or a different presentation |
| NG-008 | high degree and nontrivial ambient vanishing cycles force a singularity for a specified Hodge class | NO-GO | BFNP Proposition 5.11 versus Corollary 5.15; Thomas Section 5 | requires a new class-specific local nonvanishing theorem |
| NG-009 | a nonzero nodal defect/relation space forces detection of a specified Hodge class | NO-GO | B009 and the linear pairing audit in G006 | requires construction of a relation outside the kernel of the specified class's pairing functional |

| NG-010 | Schnell's global tube surjectivity supplies a local Saito relation automatically | NO-GO | kernel/support audit in G007; B008, B010, B011 | requires an algebraic concentration theorem preserving the tube class, Hodge type, and pairing |

## Promotion rule

A claim moves to `PROVED` only when all dependencies are theorems with matching
fields, coefficients, cohomology, and scope. It moves to `FORMALLY VERIFIED`
only with a reproducible kernel-checked theorem and no project-local axiom for
the decisive content.
