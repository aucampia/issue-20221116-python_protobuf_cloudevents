from ._version import __version__

__all__ = ["__version__"]


def whoami() -> str:
    return __name__
