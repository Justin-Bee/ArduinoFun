import pyb

from pyb import Pin

p_out = Pin('X1', Pin.OUT_PP)
p_out.high()
