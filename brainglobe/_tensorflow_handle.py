from importlib.metadata import PackageNotFoundError, version


def throw_error_on_call() -> None:
    raise PackageNotFoundError(
        "Python cannot locate the tensorflow package, "
        "which is required to use cellfinder tools. "
        "Please manually install tensorflow into your environment; "
        "see https://github.com/brainglobe/brainglobe-meta#installation "
        "for more details."
    )


_CELLFINDER_FUNCTIONAL = True
try:
    version("tensorflow")
except PackageNotFoundError:
    # No tensorflow is visible to the Python interpreter.
    # Do not expose the cellfinder_core package as it is unusable.
    # Instead, import a cellfinder_core name that will
    # throw an error if invoked.
    _CELLFINDER_FUNCTIONAL = False
