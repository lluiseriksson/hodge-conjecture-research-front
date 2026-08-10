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

Rules:

- no `sorry`, admitted theorem, or project-local axiom may carry open
  algebraicity content on a stable branch;
- conditional interfaces must expose every hypothesis in their type;
- a kernel-checked implication from an explicit hypothesis package is labeled
  `CONDITIONAL`, not `FORMALLY VERIFIED` as a solution of that hypothesis;
- toolchain version and theorem inventory must accompany any future code.
