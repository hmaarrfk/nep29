import nep29
from nep29 import nep29_versions
import pytest


def test_project_import():
    pass

@pytest.mark.parametrize('vstring,expected', [
    ("1!2.3.4", (1, 2, 3)),
    ("1.2.3", (0, 1, 2)),
])
def test_major_minor_version(vstring, expected):
    from packaging.version import Version
    v = Version(vstring)
    assert nep29.nep29.major_minor_version(v) == expected


def test_pandas():
    # Pre-release information can be included as letters
    # not seperated by a '.' from the version number
    # the pandas package uses this notation.
    nep29_versions('pandas')
