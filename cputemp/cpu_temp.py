#!/usr/bin/python3
from time import sleep, strftime, time
from gpiozero import CPUTemperature

cpu = CPUTemperature()

def log_temp(samples,interval):
    with open("/home/pi/cpu_temp.csv", "a") as log:
        for x in range(samples):
            temp = cpu.temperature
            data = "{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp))
            print(data, end='')
            log.write(data)
            sleep(interval)

while True:
    log_temp(6,10)
