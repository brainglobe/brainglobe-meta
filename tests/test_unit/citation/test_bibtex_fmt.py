from typing import List

import pytest

from brainglobe.citation.bibtex_fmt import supported_bibtex_entry_types


@pytest.fixture()
def entry_types_we_support() -> List[str]:
    """
    All Bibtex entry types that we support for writing BrainGlobe references.
    """
    return ["article", "software"]


def test_supported_entry_types(entry_types_we_support) -> None:
    """
    Check that we support all the entry types that we are expecting to.
    """
    dict_of_classes = supported_bibtex_entry_types()
    list_of_entry_types = sorted(list(dict_of_classes.keys()))

    assert sorted(list_of_entry_types) == sorted(entry_types_we_support), (
        "Mismatch between entry types we expect to support, "
        "and those we actually do.\n"
        f"Expect to support: {sorted(entry_types_we_support)}"
        f"Actually supporting: {sorted(list_of_entry_types)}"
    )
    return
