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

    # Now check the optional dependencies
    # morphapi
    bg_has_morphapi = hasattr(bg, "morphapi")
    if bg._MORPHAPI_INSTALLED:
        assert (
            bg_has_morphapi
        ), "brainglobe has morphapi, but it is flagged as installed"
        assert inspect.ismodule(
            getattr(bg, "morphapi")
        ), "brainglobe.morphapi is not a submodule"
    else:
        assert (
            not bg_has_morphapi
        ), "brainglobe has morphapi, but it is flagged as not installed"
    # cellfinder
    bg_has_cellfinder = hasattr(bg, "cellfinder")
    if bg._CELLFINDER_INSTALLED:
        assert (
            bg_has_cellfinder
        ), "brainglobe has cellfinder, but it is flagged as installed"
    else:
        assert (
            not bg_has_cellfinder
        ), "brainglobe has cellfinder, but it is flagged as not installed"
