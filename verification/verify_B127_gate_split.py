"""Finite logic model for B127 and NG102."""


def clean_incidence(support_nonempty: bool, cleanup_holds: bool) -> bool:
    return support_nonempty and cleanup_holds


for support in (False, True):
    for cleanup in (False, True):
        clean = clean_incidence(support, cleanup)
        assert not clean or support
        assert clean == (support and cleanup)

# Nonempty support alone does not formally imply clean incidence.
assert clean_incidence(True, False) is False

print("PASS: B127 splits terminal support from conditional clean cleanup")
