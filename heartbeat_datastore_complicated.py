
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
    return intesity + 1

def lighter_down(light_number, intensity):
    #this line needs to be modified to whatever the intensity should be
    strip.setPixelColorRGB(light_number, 255-intensity, 0, 0)
    strip.show()
    return intesity + 1


def heartbeat(light):
    if counter = 0:
        get_new_average()
        #TODO: replace current_time with how you get the current time
        start_time = current_time
        counter = 1
    #the 255 value is arbitrary
    #need to change it when you figure out the flash
    elif 0 < counter < 255:
        counter = lighter_up(light, counter)
    elif 255 < intesity <510:
        counter = lighter_down(light, counter)
    elif intensity > 510:
        #TODO: also need to get current_time to work here
        time_from_start = start_time - current_time
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
            #TODO:return an error

heartbeat(0)
