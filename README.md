# heartbeat
heartbeat matrix installation

datastore.ino is designed to read a sensor (right now it is a potentiometer but eventually a heartrate monitor) and send 1) if there was a reading in a relevant range, and 2) the aveage time between relevant readings, over serial

heartbeat_datastore.py is designed to poll the arduino over serial and respond accordingly
