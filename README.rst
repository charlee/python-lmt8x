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

.. |commits-since| image:: https://img.shields.io/github/commits-since/charlee/python-lmt8x/v1.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/charlee/python-lmt8x/compare/v1.0.0...master



.. end-badges

Transfer tables for LMT8x Temperature Sensors.

LMT8x (LMT84, LMT85, LMT86, LMT87) are a series of `analog temperature sensors <https://www.ti.com/sensors/temperature-sensors/overview.html>`_ made by Texus Instrument.
These sensors can provide -50°C ~ 150°C with ±0.4°C accuracy. Although the output voltage is nearly linear to the temperature, it does have a slight umbrella parabolic shape.
Therefore transfer tables are required to convert the voltage to the temperature.

Datasheets:

- `LMT84 <https://www.ti.com/lit/ds/symlink/lmt84.pdf>`_
- `LMT85 <https://www.ti.com/lit/ds/symlink/lmt85.pdf>`_
- `LMT86 <https://www.ti.com/lit/ds/symlink/lmt86.pdf>`_
- `LMT87 <https://www.ti.com/lit/ds/symlink/lmt87.pdf>`_


This package provides tranfer functions for LMT84, LMT85, LMT86, and LMT87 based on their transfer tables.
These funcitons basically do a binary search through the transfer tables and return the match.
If no match found, linear interpolation will be used to generate an approximate value.


Installation
============

::

    pip install lmt8x

You can also install the in-development version with::

    pip install https://github.com/charlee/python-lmt8x/archive/master.zip

Usage
======

`lmt8x` package provides functions `lmt84_v2t`, `lmt85_v2t`, `lmt86_v2t`, and `lmt87_v2t` for converting voltage to temperature.

- input voltage must be in mV.
- output temperature is in celsius.

::

  from lmt8x import lmt87_v2t     # or `lmt86_v2t`, `lmt85_v2t`, `lmt84_v2t`

  # read voltage from sensors.
  # v = read_sensor()

  # convert v to temperature.
  # the pamaeter must be in mV. Return value is in celsius.
  temp = lmt87_v2t(v * 1000)

  print('Temperature is %s C.' % temp)
  

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
