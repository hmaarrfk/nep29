"""Top-level package for NEP29 Calculator."""

__author__ = 'Mark Harfouche'
__email__ = 'mark.harfouche@gmail.com'

from .nep29 import nep29_versions

__all__ = [
    'nep29_versions',
]


from . import _version
__version__ = _version.get_versions()['version']
del _version
