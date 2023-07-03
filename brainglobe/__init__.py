from importlib.metadata import PackageNotFoundError, version

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
# cellfinder, and cellfinder_core
_CELLFINDER_INSTALLED = True
try:
    import cellfinder_core
except ImportError:
    _CELLFINDER_INSTALLED = False
