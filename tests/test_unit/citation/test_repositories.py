import importlib

import pytest

from brainglobe.citation.repositories import Repository


def test_throw_on_bad_repo() -> None:
    """
    Test that we cannot construct a repository that doesn't exist.
    """
    with pytest.raises(
        ValueError, match="Repository brainglobe/dont-exist does not exist"
    ):
        Repository("dont-exist", ["a", "b", "c"])


def test_all_repos_reachable() -> None:
    """
    Test that all brainglobe repositories we have created are reachable.

    Due to how Python imports work, importing REPOSITORIES will essentially run
    repositories.py as a script, and thus will throw the __post_init__ error on
    validation if any of the repositories have an invalid URL.

    We can achieve this by simply importing the submodule through importlib.
    """
    bg_c_r = importlib.import_module("brainglobe.citation.repositories")

    assert hasattr(bg_c_r, "REPOSITORIES")


def test_alias_syntax() -> None:
    """
    Test that the in keyword behaves as expected for determining if a
    tool resides inside a repository.
    """
    r = Repository("BrainGlobe", ["BG"])

    # Explicit alias that was included, case-insensitive
    assert "bG" in r, "Could not located expected tool alias."
    # Repository name itself should be an implicit alias
    assert "brainglobe" in r, "Could not use repository name as tool alias."
    # Not an alias will return false
    assert "not-an-alias" not in r, "Unexpected alias present in class."
