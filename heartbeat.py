import board
import time
import analogio
import neopixel
 
pixels = neopixel.NeoPixel(board.A2, 8, brightness=.2)
pixels.fill((0,0,0))
pixels.show()
#pixels[0] = (50, 100, 200)
#pixels.show()


adc = analogio.AnalogIn(board.A1)

def flash():
    for i in range(100, 255, 20):
        pixels[0] = (i, 0, 0)
        pixels.show()
    for i in range(255, 0, -10):
        pixels[0] = (i, 0, 0)
        pixels.show()
 
while True:
    #formatted for the plotter, you can just do print(adc.value) for the number
    print((adc.value,))
    if adc.value > 50000:
        flash()
    # flash()
    time.sleep(.1)
    