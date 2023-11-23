from importlib.metadata import PackageNotFoundError, version

from ._conda_handles import _CELLFINDER_INSTALLED, _MORPHAPI_INSTALLED

try:
    __version__ = version("brainglobe")
except PackageNotFoundError:
    # package is not installed
    pass

# Expose tools under the brainglobe namespace
import bg_atlasapi
import bg_space
import brainreg
import brainglobe_segmentation

# Expose tools that may not be present
# if a conda install was performed
if _MORPHAPI_INSTALLED:
    # Import morphapi
    import morphapi

# cellfinder and associated packages
if _CELLFINDER_INSTALLED:
    import cellfinder_core
