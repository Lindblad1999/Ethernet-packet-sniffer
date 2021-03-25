#!/usr/bin/python

import os, sys
import serial
from prometheus_client import Gauge, Summary, start_http_server
import time

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)

if __name__ == '__main__':
    gauge = Gauge('python_vacuum_pressure_gauge', 'Vacuum chamber pressure')
    start_http_server(8000)
    while True:
        data = ser.readline()
        print(data)
        gauge.set(data)

# while True:
#     line = ser.readline()
#     if len(line) == 0:
#         print("Timeout!")
#         sys.exit()
#     print(line)
