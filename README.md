# NEP29 Calculator


[![pypi](https://img.shields.io/pypi/v/nep29.svg)](https://pypi.python.org/pypi/nep29)
[![Travis](https://img.shields.io/travis/hmaarrfk/nep29.svg)](https://travis-ci.org/hmaarrfk/nep29)
[![Docs](https://readthedocs.org/projects/nep29/badge/?version=latest)](https://nep29.readthedocs.io/en/latest/?badge=latest)


NEP29 Calculator tools

Usage
-----
```bash
$ nep29 --help
usage: nep29 [-h] [--n_months N_MONTHS] [--n_minor N_MINOR] package

NEP29 calcaulator.

positional arguments:
  package              Package to deprecation

optional arguments:
  -h, --help           show this help message and exit
  --n_months N_MONTHS  Number of months to keep supporting
  --n_minor N_MINOR    Number of minor versions to keep supporting
```

Example:
```bash
nep29 numpy
[('1.19.0', '2020-06-20 20:37:45.624482'),
 ('1.18.0', '2019-12-22 15:51:31.822488'),
 ('1.17.0', '2019-07-26 18:35:56.431887'),
 ('1.16.0', '2019-01-14 03:02:28.527716')]
```

Credits
-------

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter)
and the
[hmaarrfk/cookiecutter-pypackage](https://github.com/hmaarrfk/cookiecutter-pypackage)
project template.

