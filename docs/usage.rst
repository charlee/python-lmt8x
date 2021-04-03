=====
Usage
=====

`lmt8x` package provides functions `lmt84_v2t`, `lmt85_v2t`, `lmt86_v2t`, and `lmt87_v2t` for converting voltage to temperature.

- input voltage must be in mV.
- output temperature is in Celsius.

::

  from lmt8x import lmt87_v2t     # or `lmt86_v2t`, `lmt85_v2t`, `lmt84_v2t`

  # read voltage from sensors.
  # v = read_sensor()

  # convert v to temperature.
  # the pamaeter must be in mV. Return value is in celsius.
  temp = lmt87_v2t(v * 1000)

  print('Temperature is %s C.' % temp)
  