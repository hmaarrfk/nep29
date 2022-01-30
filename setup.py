#!/usr/bin/env python3
from setuptools import setup, find_packages


def get_version_and_cmdclass(pkg_path):
    """Load version.py module without importing the whole package.

    Template code from miniver
    """
    import os
    from importlib.util import module_from_spec, spec_from_file_location

    version_py = os.path.join(pkg_path, "_version.py")
    spec = spec_from_file_location("version", version_py)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.__version__, module.get_cmdclass(pkg_path)


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = ['requests', 'prettytable', 'packaging', ]

test_requirements = ['pytest', ]

version, cmdclass = get_version_and_cmdclass(r"nep29")

setup(
    author="Mark Harfouche",
    author_email='mark.harfouche@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
    description="NEP29 Calculator tools",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='nep29',
    name='nep29',
    packages=find_packages(),
    tests_require=test_requirements,
    url='https://github.com/hmaarrfk/nep29',
    entry_points={
        'console_scripts': [
            'nep29=nep29.nep29:main'
        ],
    },
    version=version,
    cmdclass=cmdclass,
    zip_safe=False,
)
