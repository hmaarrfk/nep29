# NEP 29 Calculator


[![PyPI](https://img.shields.io/pypi/v/nep29.svg)](https://pypi.python.org/pypi/nep29)
[![Travis](https://img.shields.io/travis/hmaarrfk/nep29.svg)](https://travis-ci.org/hmaarrfk/nep29)
[![Docs](https://readthedocs.org/projects/nep29/badge/?version=latest)](https://nep29.readthedocs.io/en/latest/?badge=latest)


[NEP 29](https://numpy.org/neps/nep-0029-deprecation_policy.html) calculator tools

Usage
-----
```console
$ nep29 --help
usage: nep29 [-h] [--n_months N_MONTHS] [--n_minor N_MINOR] package

NEP 29 calculator.

positional arguments:
  package              Package to deprecation

optional arguments:
  -h, --help           show this help message and exit
  --n_months N_MONTHS  Number of months to keep supporting
  --n_minor N_MINOR    Number of minor versions to keep supporting
```

Example:
```console
$ nep29 numpy
| version |    date    |
|---------|------------|
|  1.19.0 | 2020-06-20 |
|  1.18.0 | 2019-12-22 |
|  1.17.0 | 2019-07-26 |
|  1.16.0 | 2019-01-14 |
```

Credits
-------

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter)
and the
[hmaarrfk/cookiecutter-pypackage](https://github.com/hmaarrfk/cookiecutter-pypackage)
project template.

