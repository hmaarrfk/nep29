import nep29
from nep29 import nep29_versions
import pytest


def test_project_import():
    pass

def test_pandas():
    # Pre-release information can be included as letters
    # not seperated by a '.' from the version number
    # the pandas package uses this notation.
    nep29_versions('pandas')
