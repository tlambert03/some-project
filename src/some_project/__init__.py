from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("some-project")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "Talley Lambert"
__email__ = "talley.lambert@gmail.com"