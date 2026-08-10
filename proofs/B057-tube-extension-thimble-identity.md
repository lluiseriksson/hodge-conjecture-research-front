---
brick_id: B057
status: PROVED
base_field: C
variety: the pullback of a projective hyperplane family to a meridian system in a plane net, with a fixed smooth reference fiber and ordinary Lefschetz meridians
smoothness: fibers along the detector loop are smooth; each enclosed generic discriminant point has one ordinary double point
projectivity: the universal hyperplane family is projective; the extension-chain calculation is topological over the chosen paths
dimension: dim_C X = 2n; vanishing cycles have real dimension 2n-1 and thimble extensions have dimension 2n
codimension: middle codimension n; meridians surround smooth codimension-one points of the discriminant curve
coefficient_field: Q
cohomology_theory: singular relative homology, Picard-Lefschetz monodromy, extension chains, Lefschetz thimbles, and primitive ambient homology
hodge_type: no Hodge type is asserted; the distributed relation is topological
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); the extension class is not asserted algebraic
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B013, B022, B056, Schnell tube definition (S023), and Lairez-Pichon-Pharabod-Vanhove equations (5), (7), and (10) (S029)
claim: For a monodromy-fixed class and a Picard-Lefschetz meridian factorization of its loop, B013's telescoping relation coefficients are, up to the universal orientation sign, exactly the coefficients in the ordered sum of Lefschetz-thimble extensions tracing that class; its primitive ambient image is the original Schnell tube class.
falsifier: a factorization for which the path-composition formula gives different thimble coefficients from B013 or whose extension trace maps to an ambient class different from Schnell's tube modulo the reference fiber
---

# B057 - The distributed relation is the tube extension chain

Let

\[
 g=\ell_r\cdots\ell_1,\qquad
 M_i=(\ell_i)_*
\]

be a factorization by oriented Lefschetz meridians; inverse meridians are
allowed, with their orientation absorbed into the rank-one coefficient.
Write

\[
 \alpha_0=\alpha,\qquad
 \alpha_i=M_i\alpha_{i-1},
\]

and assume \(g\alpha=\alpha\). The Picard-Lefschetz formula has the
rank-one form

\[
 M_i-I=d_i m_i,\qquad
 d_i=\delta_i,\qquad
 m_i(v)=\varepsilon\langle v,\delta_i\rangle,
\]

with the dimension-dependent sign \(\varepsilon\).

## Extension formula

For a path \(\ell\), let \(\tau_\ell\) be extension of a fiber class along
that path. Equation (5) of S029 gives

\[
 \tau_{\ell'\ell}
 =\tau_\ell+\tau_{\ell'}\ell_*.
\]

Induction therefore gives

\[
 \tau_g(\alpha)
 =\sum_{i=1}^r\tau_{\ell_i}(\alpha_{i-1}).
\]

Orient all thimbles consistently so that the universal sign in equation
(10) is absorbed into their generators. It then identifies each summand
with

\[
 \tau_{\ell_i}(\alpha_{i-1})
 =m_i(\alpha_{i-1})\Delta_i.
\]

Consequently the coefficient vector in this ordered thimble-extension
expression for \(\tau_g(\alpha)\) is

\[
 c_i=m_i(\alpha_{i-1})
 =\varepsilon\langle\alpha_{i-1},\delta_i\rangle,
\]

which is exactly B013's telescoping coefficient vector.

No linear independence of repeated meridian thimbles is used here. In a
single generic Lefschetz disk, S029 Lemma 1 makes the distinct thimbles a
basis; for a general net word, the displayed formula is an ordered
chain-level expression.

Equation (7), or direct telescoping, gives

\[
 \partial\tau_g(\alpha)
 =\sum_i c_i\delta_i
 =(g-I)\alpha=0.
\]

Thus the distributed relation is not merely parallel numerical
bookkeeping: it is the boundary-zero extension chain traced by the
monodromy-fixed class.

## Ambient class

Schnell defines the tube by flatly tracing \(\alpha\) around \(g\) and
closing the trace by a chain in the reference fiber. This is the same
extension chain \(\tau_g(\alpha)\); changing the closing chain changes its
class only by the image of reference-fiber homology. Hence B057's thimble
combination maps to

\[
 [\tau_g(\alpha)]
 \in H_{2n}(X,\mathbf Q)/H_{2n}(X\cap H_0,\mathbf Q),
\]

the original Schnell tube class. If the chosen tube pairs nontrivially with
\(\zeta\), this ambient quotient class is nonzero.

The result does not concentrate the thimbles at one singular member or give
the relation type \((0,0)\). Those remain specialization obligations.
