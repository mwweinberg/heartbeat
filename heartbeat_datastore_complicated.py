from neopixel import *
import time

# LED strip configuration:
LED_COUNT      = 16      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

counter = 0
time_from_start = 0
new_average = 0

#eventually this will be get_new_average(sensor_number)
def get_new_average():
    #average is going to be time in .... ms?
    #eventually it will be the average from the arduino
    new_average = int(input("new average? "))

def lighter_up(light_number, intensity):
    #this line needs to be modified to whatever the intensity should be
    strip.setPixelColorRGB(light_number, intensity, 0, 0)
    strip.show()
    return intensity + 1

def lighter_down(light_number, intensity):
    #this line needs to be modified to whatever the intensity should be
    strip.setPixelColorRGB(light_number, 255-intensity, 0, 0)
    strip.show()
    return intensity + 1


def heartbeat(light):
    #acknowledge that counter is a global variable
    global counter

    if counter == 0:
        get_new_average()
        #this counts seconds from an arbitrary start point
        start_time = int(time.perf_counter())
        counter = 1
    #the 255 value is arbitrary
    #need to change it when you figure out the flash
    elif 0 < counter < 255:
        counter = lighter_up(light, counter)
    elif 255 < counter <510:
        counter = lighter_down(light, counter)
    elif counter > 510:
        #difference between the start time and now
        time_from_start = int(time.perf_counter()) - start_time
        #if the time from the start of the flash is less than the
        #duration of the heartbeat, as defiend by new_average
        if time_from_start < new_average:
            #just wait it out
            pass
        #if the time from start has hit the new_average
        #it is time for a new heartbeat
        elif time_from_start >= new_average:
            counter = 0
        else:
            print("There was an error in heartbeat()")
while True:
    heartbeat(0)
