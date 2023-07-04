from importlib.metadata import PackageNotFoundError, version

from ._tensorflow_handle import _CELLFINDER_FUNCTIONAL as _CELLFINDER_INSTALLED

try:
    __version__ = version("brainglobe")
except PackageNotFoundError:
    # package is not installed
    pass

# Expose tools under the brainglobe namespace
import bg_atlasapi
import bg_space
import brainreg
import brainreg_segment

# Expose tools that may not be present
# if a conda install was performed

# morphapi
_MORPHAPI_INSTALLED = True
try:
    import morphapi
except ImportError:
    _MORPHAPI_INSTALLED = False

# cellfinder and associated packages
if _CELLFINDER_INSTALLED:
    import cellfinder_core
else:
    # Under the cellfinder_core name,
    # import an error-throwing function that points users to the
    # instructions for getting the cellfinder tool working
    from ._tensorflow_handle import throw_error_on_call as cellfinder_core
