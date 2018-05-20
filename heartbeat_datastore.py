# TODO: recieve info over serial
#serial_bit = the 1 or 0
#new_average = the running average between beats
#old_average = the old average
#old_average_timestamp = when the old average was upated


def animation():
    #pulse the light
def average_animation(pulse_time):
    #run the animation so that it flashes according to the new_average rate
    #flash (takes X amount of time)
    #wait in a resing state for pulse_time- x amount of time
def decay():
    #make the light timing start to decay

#take the average time between beats as the new benchmark average time
def average_update():
    old_average = new_average
    old_average_timestamp = the current time


# if there is a pulse
if serial_bit == 1:
    #run the animation
    animation()
    average_update()

#if there isn't a pulse
elif serial_bit == 0:
    #if the average hasn't updated
    #there probably hasn't been a beat since the last reading
    if new_average == old_average:
        #if it has been the same for a long time
        if (currenttime - old_average_timestamp) > a long time:
            decay()
        # if it's still pretty close to when it was last updated
        elif (currenttime - old_average_timestamp) < a long time:
            average_animation(new_average)
    #if the average has updated
    #there was a flash during the previous animation
    else:
        average_animation(new_average)
        average_update

else:
    #there has been some sort of horrible error
