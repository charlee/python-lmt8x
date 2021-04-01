========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-lmt8x/badge/?style=flat
    :target: https://python-lmt8x.readthedocs.io/
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.com/charlee/python-lmt8x.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/charlee/python-lmt8x

.. |version| image:: https://img.shields.io/pypi/v/lmt8x.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/lmt8x

.. |wheel| image:: https://img.shields.io/pypi/wheel/lmt8x.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/lmt8x

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/lmt8x.svg
    :alt: Supported versions
    :target: https://pypi.org/project/lmt8x

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/lmt8x.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/lmt8x

.. |commits-since| image:: https://img.shields.io/github/commits-since/charlee/python-lmt8x/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/charlee/python-lmt8x/compare/v0.0.0...master



.. end-badges

Transfer tables for LMT8x Temperature Sensors.

* Free software: MIT license

Installation
============

::

    pip install lmt8x

You can also install the in-development version with::

    pip install https://github.com/charlee/python-lmt8x/archive/master.zip


Documentation
=============


https://python-lmt8x.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
