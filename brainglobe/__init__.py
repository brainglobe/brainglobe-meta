from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("brainglobe")
except PackageNotFoundError:
    # package is not installed
    pass

# Expose tools under the brainglobe namespace
