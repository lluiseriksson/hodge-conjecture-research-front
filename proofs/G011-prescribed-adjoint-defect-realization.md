---
brick_id: G011
status: NO-GO
base_field: C
variety: an arbitrary polarized smooth projective X of dimension 2n, a specified primitive rational Hodge class zeta, a chosen nonzero global detector, and a sought sufficiently ample independent-node hypersurface Y_0
smoothness: X and the reference fibers are smooth; Y_0 has only ordinary double points imposing independent conditions on |L| locally
projectivity: X and Y_0 are projective
dimension: dim_C X = 2n and dim_C Y_0 = 2n-1
codimension: middle codimension n on X; Y_0 has codimension 1 and its node stratum has codimension equal to the number of independent nodes
coefficient_field: Q for Hodge, homology, and relation data; C for the adjoint coherent-cohomology presentation
cohomology_theory: primitive Betti homology and cohomology, monodromy tubes, quotiented thimbles, nodal vanishing cycles, local intersection cohomology, mixed Hodge structures, and coherent cohomology of the adjoint node ideal
hodge_type: zeta has rational type (0,0) after Tate twist; every nodal rational relation has type (0,0), but the coherent defect presentation alone carries no rational class-pairing certificate
cycle_class_map: CH^n(X)_Q -> H^{2n}(X,Q(n))
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B010-B011, B015-B016, and B022-B027
claim: Every specified nonzero global detector of a primitive rational Hodge class can be realized, up to retaining its nonzero pairing, by a vector in the adjoint node-evaluation defect of one independent-node high-degree hypersurface, compatibly with the Saito relation and ambient-class maps.
falsifier: a polarized smooth projective 2n-fold and primitive rational Hodge class with a nonzero global detector for which every independent-node adjoint defect subspace maps into the annihilator of that class
---

# G011 - Prescribed adjoint-defect realization

## Falsifiable theorem sought

Given

\[
 0\ne\zeta\in
 H^{2n}_{\mathrm{prim}}(X,\mathbf Q(n))\cap H^{0,0}
\]

and a global detector supplied by B011, construct \(L\gg0\), an
independent-node member \(Y_0\in|L|\) with node scheme \(\Delta\), and a
vector in the adjoint evaluation defect

\[
 c\in H^1(X,I_\Delta\otimes K_X\otimes L^n)
\]

whose corresponding nodal relation \(\beta_c\) satisfies

\[
 \langle\zeta,\gamma_{\beta_c}\rangle\ne0.
\]

The construction must include the vector-level comparison from the coherent
defect to Saito's rational relation space and the ambient primitive class; an
equality of dimensions is insufficient. B026 then supplies the exact
numerical consistency check, B010 supplies Hodge type and the pairing, and
B015 supplies the controlled independent-node local geometry. Universally,
this proves G010 and hence the terminal-equivalent detection statement.

## Attempt 1 - Use only positive adjoint defect

Choose a nodal member with
\(h^1(I_\Delta\otimes K_X\otimes L^n)>0\). B026 proves that a relation and a
nonzero extra-homology class exist. B031 shows that their canonical map to
primitive ambient homology may be zero. Even when its image is nonzero, it
may be contained in \(\zeta^\perp\), and no defect vector is tied to the
chosen global detector. These are NG-027 and NG-023 respectively.

## Re-entry condition

Construct a global incidence correspondence over the nodal Severi locus
whose fiber is the adjoint evaluation cokernel, equip it with a rational
comparison to the Saito relation local system and its canonical
extra-to-primitive map, and prove that the section or cycle induced by the
chosen global detector has nonzero \(\zeta\)-pairing in at least one fiber.
The construction must not start from an algebraic representative of
\(\zeta\).

## Final obstruction

B027 proves that the full independence hypothesis forces this adjoint defect
group to vanish for all sufficiently high powers when \(n\ge2\). G011 is
therefore closed as part of NG-024; G012 retains only partwise independence.
