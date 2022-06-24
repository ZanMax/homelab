import time
import datetime
import os

while(True):
    CurrentTime = datetime.datetime.now()

    with open(r"/sys/class/thermal/thermal_zone0/temp") as File:
        CurrentTemp = File.readline()

    print(str(str(float(CurrentTemp) / 1000) + " °C"))
    time.sleep(3)
    os.system("clear")