#!/usr/bin/env python
# -*- encoding: utf8 -*-
import glob
import inspect
import io
import os

from setuptools import find_packages
from setuptools import setup

changelog = os.path.join(os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe()))), "CHANGELOG.md")
with open(changelog, "rt") as fh:
    changelog = fh.read()

long_description = """
Source code: https://github.com/adjtomo/pyflex

Documentation: http://krischer.github.io/pyflex

%s""".strip() % changelog


def read(*names, **kwargs):
    return io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")).read()


setup(
    name="pyflex",
    version="0.2.0",
    license='GNU General Public License, Version 3 (GPLv3)',
    description="Python port of the FLEXWIN package",
    long_description=long_description,
    author="adjTomo Development Team",
    author_email="adjtomo@gmail.com",
    url="https://github.com/adjtomo/pyflex",
    packages=find_packages(),
    # packages=find_packages("pyflex"),
    # package_dir={"": "pyflex"},
    # py_modules=[os.path.splitext(os.path.basename(i))[0]
    #             for i in glob.glob("pyflex/*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list:
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    keywords=[
        "seismology", "flexwin", "science", "tomography", "inversion"
    ],
    install_requires=[
        "obspy >= 1.0", "flake8", "pytest", "nose"
    ],
    extras_require={
        "docs": ["sphinx", "ipython", "runipy"]
    }
)
