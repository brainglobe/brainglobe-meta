import inspect

import pytest
from importlib_metadata import PackageNotFoundError

import brainglobe as bg

# Tools that will be exposed in the brainglobe module/namespace
EXPOSED_TOOLS = [
    "bg_atlasapi",
    "bg_space",
    "brainreg",
    "brainglobe_segmentation",
    "cellfinder_core",
]
OPTIONAL_TOOLS = ["morphapi", "cellfinder"]


def test_tool_exposure() -> None:
    """Assert that each of the user-facing tool sub-modules can be imported."""

    for exposed_tool in EXPOSED_TOOLS:
        assert hasattr(
            bg, exposed_tool
        ), f"brainglobe has no (exposed) tool {exposed_tool}"
        assert inspect.ismodule(
            getattr(bg, exposed_tool)
        ), f"brainglobe.{exposed_tool} is not a submodule"

    # Determine if optional dependencies were installed,
    # and exposed if necessary

    # morphapi - should be exposed if installed
    if bg._MORPHAPI_INSTALLED:
        assert hasattr(
            bg, "morphapi"
        ), "morphapi is installed but not exposed."
        assert inspect.ismodule(
            bg.morphapi
        ), "brainglobe.morphapi is not a module"
    else:
        assert not hasattr(bg, "morphapi")

    # cellfinder - should not be exposed if installed
    # cellfinder_core - should be exposed if installed
    if bg._CELLFINDER_INSTALLED:
        assert not hasattr(
            bg, "cellfinder"
        ), "brainglobe.cellfinder is exposed"
        assert hasattr(
            bg, "cellfinder_core"
        ), "brainglobe.cellfinder_core is not exposed"
    else:
        # cellfinder_core should be aliased to a function
        # that throws an error when invoked
        with pytest.raises(PackageNotFoundError):
            bg.cellfinder_core()
