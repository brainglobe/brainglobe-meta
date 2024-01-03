from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("brainglobe")
except PackageNotFoundError as e:
    # package is not installed
    pass
