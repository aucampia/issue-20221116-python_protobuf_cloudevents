from ._version import __version__

__all__ = ["__version__"]


def whereami() -> str:
    return __name__
