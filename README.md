# NEP 29 Calculator


[![PyPI](https://img.shields.io/pypi/v/nep29.svg)](https://pypi.python.org/pypi/nep29)
[![Travis](https://img.shields.io/travis/hmaarrfk/nep29.svg)](https://travis-ci.com/hmaarrfk/nep29)


[NEP 29](https://numpy.org/neps/nep-0029-deprecation_policy.html) calculator tools

## Usage
```console
$ nep29 --help
usage: nep29 [-h] [--n_months N_MONTHS] [--n_minor N_MINOR] package

NEP 29 calculator.

positional arguments:
  package              Package to deprecation

optional arguments:
  -h, --help           show this help message and exit
  --n_months N_MONTHS  Number of months to keep supporting (default: 24)
  --n_minor N_MINOR    Number of minor versions to keep supporting (default: 3)

For more information, see https://numpy.org/neps/nep-0029-deprecation_policy.html
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

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter)
and the
[hmaarrfk/cookiecutter-pypackage](https://github.com/hmaarrfk/cookiecutter-pypackage)
project template.

### Development Lead

* Mark Harfouche <mark.harfouche@gmail.com>

### Contributors

* Hugo van Kemenade (hugovk)

## Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

### Report Bugs

Report bugs at https://github.com/hmaarrfk/nep29/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

### Write Documentation

NEP29 Calculator could always use more documentation, whether as part of the
official NEP29 Calculator docs, in docstrings, or even on the web in blog posts,
articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at https://github.com/hmaarrfk/nep29/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

### Get Started!

You can follow the scikit-image contribution document and adapt it accordingly.

