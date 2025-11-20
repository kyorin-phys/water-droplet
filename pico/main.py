import time
from machine import Pin

# GPIO setting
SOL_PIN = 2
HALF_PIN = 3
FULL_PIN = 4

# TIME setting (ms)
TSOL = 50     # solenoid open time
TS = 10       # shutter ON/OFF 
TDELAY = 200  # shutter delay
TWAKEUP = 500 # camera wake up
TWAIT = 8000  # sleep for next shoot 

# PIN init state
sol_pin = Pin(SOL_PIN, Pin.OUT)
sol_pin.value(0)

half_pin = Pin(HALF_PIN, Pin.OUT)
half_pin.value(0)

full_pin = Pin(FULL_PIN, Pin.OUT)
full_pin.value(0)

def loop():
    half_pin.value(1)
    time.sleep_ms(TWAKEUP)

    sol_pin.value(1)
    time.sleep_ms(TSOL)
    sol_pin.value(0)
    
    time.sleep_ms(TDELAY)
    full_pin.value(1)
    time.sleep_ms(TS)
    full_pin.value(0)
    half_pin.value(0)
    
    time.sleep_ms(TWAIT)

try:
    while True:
        loop()
except KeyboardInterrupt:
    print('interrupted!')
finally:
    sol_pin.value(0)
    print('sol pin is off.')