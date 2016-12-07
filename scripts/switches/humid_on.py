#!/usr/bin/python
import datetime

print("")
print("      #############################################")
print("      ##         Turning the humidifier - ON     ##")

### user settings

loc_settings = "/home/pragmo/pigitgrow/Pigrow/config/pigrow_config.txt"
locswitchlog = '/home/pragmo/pigitgrow/Pigrow/logs/switch_log.txt'

### defining variables

pi_set = {}   #the dictionary of settings

### loading settings

try:
    with open(loc_settings, "r") as f:
        for line in f:
            s_item = line.split("=")
            pi_set[s_item[0]]=s_item[1].rstrip('\n')
except:
    print("Settings not loaded, try running pi_setup")
    with open(locswitchlog, "a") as f:
        line = 'humid_on.py @' + str(datetime.datetime.now()) + '@ Failed - settings file error\n'
        f.write(line)
    print("Log writen:" + line)
    raise

# Using settings to do whatever it's supposed to do with them...

if 'gpio_humid' in pi_set and not pi_set['gpio_humid'] == '':
    gpio_pin = int(pi_set['gpio_humid'])
    gpio_pin_on = pi_set['gpio_humid_on']
    #import RPi.GPIO as GPIO
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(gpio_pin, GPIO.OUT)
    print("skipping gpio module as TESTING TEST TEST TEST")
    if gpio_pin_on == "low":
        #GPIO.output(gpio_pin, GPIO.LOW)
        print("skipping setting gpio LOW as TESTING TEST TEST TEST")
    elif gpio_pin_on == "high":
        #GPIO.output(gpio_pin, GPIO.HIGH)
        print("skipping settubg gpio HIGH as TESTING TEST TEST TEST")
    else:
        print("      !!       CAN'T DETERMINE GPIO DIRECTION    !!")
        print("      !!  run config program or edit config.txt  !!")
        print("      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        with open(locswitchlog, "a") as f:
            line = 'humid_on.py @' + str(datetime.datetime.now()) + '@ Failed - no direction set in config\n'
            f.write(line)
        print("Log writen:" + line)
        exit()

else:
    print("      !!               NO HUMIDIFIER SET         !!")
    print("      !!  run config program or edit config.txt  !!")
    print("      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    with open(locswitchlog, "a") as f:
        line = 'humid_on.py @' + str(datetime.datetime.now()) + '@ Failed - due to none set in config\n'
        f.write(line)
    print("Log writen:" + line)
    exit()

print("      ##            by switching GPIO "+str(gpio_pin)+" to "+gpio_pin_on+"  ##")
print("      #############################################")
with open(locswitchlog, "a") as f:
        line = 'humid_on.py @' + str(datetime.datetime.now()) + '@ Humidifier Turned on  \n'
        f.write(line)
print("Log writen:" + line)