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
import brainrender
import cellfinder_core
import morphapi
