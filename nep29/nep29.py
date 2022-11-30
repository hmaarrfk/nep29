"""
# NEP 29

NEP 29 reads

> When a project releases a new major or minor version, we recommend that they
> support at least [...] all minor versions of NumPy released in the prior
> 24 months from the anticipated release date with a minimum of 3 minor
> versions of NumPy

This means we have to create the union of two sets:

1. Releases that are in the last X months -- only consider X.X.0 releases
2. A certain number of minor versions.

Copyright Mark Harfouche 2019
"""
from datetime import datetime, timedelta
from prettytable import PrettyTable, MARKDOWN
import requests
from packaging.version import Version, InvalidVersion


def major_minor_version(version):
    """Given a version, returns the tuple epoch, major, minor"""
    # version.release works in either packaging 19 or 20
    # as of packaging 20+, can use version.major, version.minor instead
    major, minor = version.release[:2]
    return version.epoch, major, minor


def keep_oldest_minor_only(version_dates):
    vd_dict = {}
    for version, date in version_dates:
        major_minor = major_minor_version(version)
        if major_minor in vd_dict:
            if vd_dict[major_minor][1] > date:
                vd_dict[major_minor] = (version, date)
        else:
            vd_dict[major_minor] = (version, date)
    return [val
            for _, val in vd_dict.items()]


def get_versions_dates(package_name, skip_rc=True):
    r = requests.get(f"https://pypi.org/pypi/{package_name}/json")
    response = r.json()
    release_dates = []
    for k, v in response['releases'].items():
        # NOTE: for a version that doesn't comply to PEP 440, this will
        # raise packaging.version.InvalidVersion:
        try:
            version = Version(k)
        except InvalidVersion:
            pass
        for item in v:
            if item['packagetype'] == 'sdist':
                if version.is_prerelease:
                    if skip_rc or not version.pre[0] == 'rc':
                        # skip unless we do not skip RCs and this is RC
                        continue
                # alt: interpret skip_rc as allow any prerelease (e.g, betas)
                # if skip_rc and version.is_prerelease:
                    # continue
                upload_time = item['upload_time_iso_8601']
                for format in ['%Y-%m-%dT%H:%M:%S.%fZ',
                               '%Y-%m-%dT%H:%M:%SZ']:
                    try:
                        date = datetime.strptime(upload_time, format)
                        break
                    except ValueError:
                        pass
                else:
                    raise ValueError(
                        f"Could not convert {upload_time} into a standard "
                        "datetime object")

                release_dates.append((version, date))

    release_dates.sort(key=lambda x: x[1], reverse=True)
    return release_dates


def good_nep29_date(version_dates, n_months=24, release_date=None):
    delta_time = timedelta(days=365 / 12 * n_months)

    if release_date is None:
        release_date = datetime.utcnow()

    oldest_release_date = release_date - delta_time
    good_versions_date = [vd[1] > oldest_release_date
                          for vd in version_dates]
    return good_versions_date


def good_nep29_minor(version_dates, n_minor=3):
    major_minor_version_dates = [(major_minor_version(v), date)
                                 for v, date in version_dates]

    unique_major_minor = set()
    n_unique_major_minor = []
    for mm, date in major_minor_version_dates:
        unique_major_minor.add(mm)
        n_unique_major_minor.append(len(unique_major_minor))

    # Find out if it is a new "minor" version
    new_major_minor = [bool(n_current - n_old)
                       for n_current, n_old in zip(n_unique_major_minor[1:],
                                                   n_unique_major_minor[:-1])]
    # The very newest release is always "new"
    new_major_minor = [1] + new_major_minor

    good_versions_minor = [n <= n_minor and new
                           for n, new in zip(n_unique_major_minor,
                                             new_major_minor)]
    return good_versions_minor


def nep29_versions(package_name, *,
                   n_months=24, n_minor=3,
                   skip_rc=True,
                   release_date=None,
                   consider_first_minor_only=True):
    version_dates = get_versions_dates(package_name, skip_rc=skip_rc)
    if consider_first_minor_only:
        version_dates = keep_oldest_minor_only(version_dates)
    good_nep29_date_indicator = good_nep29_date(version_dates,
                                                n_months=n_months,
                                                release_date=release_date)
    good_nep29_minor_indicator = good_nep29_minor(version_dates,
                                                  n_minor=n_minor)

    # Take the combination of the two sets
    good_indicator = [g1 or g2
                      for g1, g2 in zip(good_nep29_date_indicator,
                                        good_nep29_minor_indicator)]

    valid_releases = [vd
                      for vd, good in zip(version_dates, good_indicator)
                      if good]

    valid_releases.sort(reverse=True)
    return valid_releases


def main():
    import argparse
    parser = argparse.ArgumentParser(
            description="NEP 29 calculator.",
            epilog=(
                "For more information, see "
                "https://numpy.org/neps/nep-0029-deprecation_policy.html"
            ),
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('package', type=str, help='Package to deprecation')
    parser.add_argument('--n_months', type=int, default=24,
                        help='Number of months to keep supporting')
    parser.add_argument('--n_minor', type=int, default=3,
                        help='Number of minor versions to keep supporting')
    args = parser.parse_args()

    package = args.package
    n_months = args.n_months
    n_minor = args.n_minor
    version_dates = nep29_versions(package, n_months=n_months, n_minor=n_minor)
    t = PrettyTable(["version", "date"])
    t.set_style(MARKDOWN)
    for version, date in version_dates:
        t.add_row([version, date.strftime('%Y-%m-%d')])
    print(t)


"""
from pprint import pprint
print("SciPy NEP 29 requirements")
pprint(nep29_versions('scipy', n_months=24, n_minor=3))

print("NumPy NEP 29 requirements")
pprint(nep29_versions('numpy', n_months=24, n_minor=3))
"""
