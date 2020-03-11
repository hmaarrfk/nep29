"""Top-level package for NEP29 Calculator."""

__author__ = 'Mark Harfouche'
__email__ = 'mark.harfouche@gmail.com'

from .nep29 import nep29_versions


from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
