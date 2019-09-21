import pyb
#import Pin so we can use it in the project
from pyb import Pin

#set p_out to Pin X1
p_out = Pin('X1', Pin.OUT_PP)

#just a variable so the loop never stops
x=0
#while loop to continually blink the led in Pin X1
while x==0:
     p_out.high()
     pyb.delay(500)
     p_out.low()
     pyb.delay(500)
