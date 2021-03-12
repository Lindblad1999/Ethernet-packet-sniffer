# ============================================================================
# Find out which serial/usb ports are in use and assign to the correct Arduino
# ============================================================================
import glob
import serial


def getSerialPorts():
    global _serialPortUnit2

    # Create list of potential ports
    ports = glob.glob('/dev/tty[A-Za-z]*')

    # Get rid of the ones we aren't interested in
    port_exceptions = ['dev/ttyprintk']
    for port in port_exceptions:
        if port in ports:
            ports.remove(port)

    # Assume we only have 2 devices connected
    # A USB to serial converter and a straight serial port
    for port in ports:
        try:
            s = serial.Serial(port, 9600, timeout=0, rtscts=0)
            if port.find("USB") != -1:
                print("Found USB")
            else:
                # Check it's not the internal serial port...
                if port != '/dev/ttyAMA0':
                    # This is where my Arduino is connected...
                    _serialPortUnit2 = serial.Serial(port, 9600, timeout=2, rtscts=0)
                    print("ARD {}".format(port))

        except (OSError, serial.SerialException):
            pass
