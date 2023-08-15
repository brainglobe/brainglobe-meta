from importlib.metadata import PackageNotFoundError, version
from warnings import warn

_CELLFINDER_INSTALLED = True
try:
    version("cellfinder_core")
except PackageNotFoundError as e:
    _CELLFINDER_INSTALLED = False
    warn(f"BrainGlobe: cellfinder-core unavailable. Caught {str(e)}")

_MORPHAPI_INSTALLED = True
try:
    version("morphapi")
except PackageNotFoundError as e:
    _MORPHAPI_INSTALLED = False
    warn(f"BrainGlobe: morphapi unavailable. Caught {str(e)}")
