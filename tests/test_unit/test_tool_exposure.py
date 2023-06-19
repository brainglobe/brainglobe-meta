import inspect

import brainglobe as bg

# Tools that will be exposed in the brainglobe module/namespace
EXPOSED_TOOLS = [
    "bg_atlasapi",
    "bg_space",
    "brainreg",
    "brainreg_segment",
    "cellfinder_core",
    "morphapi",
]


def test_tool_exposure() -> None:
    """Assert that each of the user-facing tool sub-modules can be imported."""

    for exposed_tool in EXPOSED_TOOLS:
        assert hasattr(
            bg, exposed_tool
        ), f"brainglobe has no (exposed) tool {exposed_tool}"
        assert inspect.ismodule(
            getattr(bg, exposed_tool)
        ), f"brainglobe.{exposed_tool} is not a submodule"
