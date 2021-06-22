#!/usr/bin/python

import os, sys
import serial
from prometheus_client import Gauge, start_http_server
import time

# Serial object
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)

# Format the data, to fit prometheus
def format_data(data):
    pass

# Read the serial port, and set the gauge metric
def process_request():
    data = ser.readline()
    data = data.decode('utf-8')
    print(data)
    data = format_data(data)
    gauge.set(data)

if __name__ == '__main__':
    # Gauge metric object
    gauge = Gauge('vacuum_chamber_pressure', 'Vacuum chamber pressure')
    # Expose the metrics at endpoint port 8001
    start_http_server(8001)
    while True:
        process_request()
