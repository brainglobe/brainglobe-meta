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
import cellfinder_core

# Determine if optional dependencies were installed,
# and expose if necessary.
# morphapi
_MORPHAPI_INSTALLED = True
try:
    import morphapi
except ImportError:
    _MORPHAPI_INSTALLED = False
# cellfinder - not exposed, but still check
_CELLFINDER_INSTALLED = True
try:
    import cellfinder
except ImportError:
    _CELLFINDER_INSTALLED = False
