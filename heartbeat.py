import board
import digitalio
import time
import analogio
import pulseio
 
#led = digitalio.DigitalInOut(board.D13)
#led.direction = digitalio.Direction.OUTPUT
led = pulseio.PWMOut(board.D13, frequency=5000, duty_cycle=0)


adc = analogio.AnalogIn(board.A1)

#https://learn.adafruit.com/circuitpython-essentials/circuitpython-pwm
def flash():
    #on
    led.duty_cycle = 65535 
    #fade out
 
while True:
    #print("Hello, CircuitPython!")
    print((adc.value,))
    for i in range(100):
        # PWM LED up and down
        if i < 50:
            led.duty_cycle = int(i * 2 * 65535 / 100)  # Up
        else:
            led.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
        time.sleep(0.01)