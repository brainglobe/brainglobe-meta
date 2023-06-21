import inspect

import brainglobe as bg

# Tools that will be exposed in the brainglobe module/namespace
EXPOSED_TOOLS = [
    "bg_atlasapi",
    "bg_space",
    "brainreg",
    "brainreg_segment",
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
    if bg._CELLFINDER_INSTALLED:
        assert not hasattr(
            bg, "cellfinder"
        ), "brainglobe.cellfinder is exposed"
