#!/usr/bin/env python3

barPressure = float(input("Enter barometric pressure:\n"))
time = input("Enter device time as 'min:sec'\n").split(':') #time zones
heading = float(input("Enter device's compass heading:\n"))
accel = float(input("Enter device's accelerometer reading\n"))


print("Hello world!")

print(barPressure, time, heading, accel)


#Ordering of datatypes:
#1: Time (Compare to current world times to find phone's timezone.)
#2 Movement (Compass + directional accelerometer to determine if the phone is moving and in what direction)
#3 Wi-fi location (Find list of wifi signals meeting the pre-determined criteria
#4 Barometer (Match those wi-fi signals to the given height of the phone.)
