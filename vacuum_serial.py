#!/usr/bin/python

import serial
from prometheus_client import Gauge, start_http_server

# Serial object
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)

# Format the data, to fit prometheus
def format_data(data):
    d = data.split(',')[1].split('E')
    first = float(d[0])
    second = float(d[1])
    result = (first * 10) ** second
    print(result)
    return result


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
