import pyb

from pyb import Pin


p_out = Pin('X1', Pin.OUT_PP)
p_out.high()

x=0

while x==0:
     p_out.high()
     pyb.delay(500)
     p_out.low()
     pyb.delay(500)
