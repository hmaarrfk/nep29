#!/usr/bin/env python3
from setuptools import setup, find_packages
import versioneer


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = ['requests', 'prettytable', ]

test_requirements = ['pytest', ]

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
    packages=find_packages(include=['nep29']),
    tests_require=test_requirements,
    url='https://github.com/hmaarrfk/nep29',
    entry_points={
        'console_scripts': [
            'nep29=nep29.nep29:main'
        ],
    },
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    zip_safe=False,
)
