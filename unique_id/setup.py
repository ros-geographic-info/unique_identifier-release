#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['unique_id'],
    package_dir={'': 'src'},
    install_requires=['genpy', 'uuid'],
    )

setup(**d)
