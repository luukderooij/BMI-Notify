import time
import logging
import serial
import io

from bminotify import settings, panels


logger = logging.getLogger(__name__)

class SerialPort:
    def __init__(self, encoding, newline):
        self.ser = None
        self.ser_io = None
        self.encoding = encoding
        self.newline = newline

    def open(self):
        try:
            self.ser = serial.Serial(
                    port=settings.COM_PORT,
                    baudrate=settings.BAUDRATE,
                    parity=settings.PARITY,  
                    stopbits=settings.STOPBITS,
                    bytesize=settings.BYTESIZE,
                    timeout=settings.TIMEOUT
                )
            self.ser_io = io.TextIOWrapper(io.BufferedRWPair(self.ser, self.ser), encoding=self.encoding, newline=self.newline)
        except Exception as e:
            logger.error(f"Could not open the COM port!")
            logger.error(f"{e}")

    def close(self):
        self.ser.close()

    def write(self, data):
        self.ser_io.write(data)
        self.ser_io.flush()

    def read(self):
        return self.ser_io.readline()