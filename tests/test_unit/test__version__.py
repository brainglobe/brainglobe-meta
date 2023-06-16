import brainglobe as bg


def test__version__():
    """Assert true if the __version__ method is available,
    and returns a string without error."""
    assert isinstance(bg.__version__, str)
