from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("some-project")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "Talley Lambert"
__email__ = "talley.lambert@gmail.com"


def func(x: int, y: str) -> bool:
    return x == 5
