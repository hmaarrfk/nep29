import nep29
from nep29 import nep29_versions
import pytest
from unittest.mock import patch, Mock
from datetime import datetime
from packaging.version import Version


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


def _mock_release_info(release_info):
    # returns a mock for the requests.Response object
    def _make_release_entry(version, date, packagetype='sdist'):
        return version, [{
            'packagetype': packagetype,
            'upload_time_iso_8601': date + 'T00:00:00.000000Z'
        }]

    package = {'releases': dict(_make_release_entry(*info)
                                for info in release_info)}
    request = Mock()
    request.json = Mock(return_value=package)
    return request


@patch.object(nep29.nep29, 'datetime', Mock(wraps=datetime))
def _nep29_versions_test(request_mock, expected, *args, **kwargs):
    # core code to run tests of nep29_versions from a mock for the
    # requests.Response object as a list of expected version strings;
    # additional args/kwargs passed to nep29_versions
    nep29.nep29.datetime.utcnow.return_value = datetime(2021, 1, 1)
    with patch('nep29.nep29.requests.get', Mock(return_value=request_mock)):
        results = nep29_versions('foo', *args, **kwargs)

    found_versions = set(r[0] for r in results)
    assert found_versions == set(Version(v) for v in expected)


@pytest.mark.parametrize('releases,expected', [
    # NOTE: for these tests we patch so that today is 2021-01-01, midnight.
    # All mock releases are at midnight GMT.
    (
        # default: include up to 3 minor versions if released long ago
        _mock_release_info([('2.0.0', '2015-01-01'),
                            ('1.2.0', '2014-01-01'),
                            ('1.1.0', '2013-01-01'),
                            ('1.0.0', '2012-01-01')]),
        ['2.0.0', '1.2.0', '1.1.0']
    ),
    (
        # default: include all minor versions first released in 24 months
        _mock_release_info([('1.9.0', '2020-12-01'),
                            ('1.8.0', '2020-09-01'),
                            ('1.7.0', '2020-06-01'),
                            ('1.6.0', '2020-01-01'),
                            ('1.5.0', '2019-06-01'),
                            ('1.4.0', '2018-12-01')]),
        ['1.9.0', '1.8.0', '1.7.0', '1.6.0', '1.5.0']
    ),
    (
        # default: release candidates should not be included
        _mock_release_info([('2.0.0.rc0', '2020-12-01'),
                            ('1.3.0', '2020-11-01'),
                            ('1.2.0', '2020-10-01'),
                            ('1.1.0', '2020-09-01')]),
        ['1.3.0', '1.2.0', '1.1.0']
    ),
])
def test_nep29_versions(releases, expected):
    _nep29_versions_test(releases, expected)


def test_nep29_versions_allow_rc():
    releases = _mock_release_info([('2.0.0.rc0', '2020-12-01'),
                                   ('1.3.0', '2020-11-01'),
                                   ('1.2.0', '2020-10-01'),
                                   ('1.1.0', '2020-09-01')])
    expected = ['2.0.0.rc0', '1.3.0', '1.2.0', '1.1.0']
    _nep29_versions_test(releases, expected, skip_rc=False)


@pytest.mark.parametrize('package', [
    # Pre-release information can be included as letters
    # not seperated by a '.' from the version number
    # the pandas package uses this notation.
    'pandas',
    # h5py contains a pre-release
    # With something like an invalid version
    #       Invalid version: '1.3.0.dev-r634'
    'h5py',
])
def test_pypi_package(package):
    nep29_versions(package)
