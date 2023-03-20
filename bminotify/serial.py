import time
import logging
import serial
import io

from bminotify import settings, panels


logger = logging.getLogger(__name__)

def serial_read():
    serial_port = SerialPort()
    serial_port.run()

class SerialPort:
    def __init__(self):
        self.ser = None
        self.ser_io = None

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
            self.ser_io = io.TextIOWrapper(io.BufferedRWPair(self.ser, self.ser), encoding='ascii', newline='\r\n')
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

    def run(self):
        self.open()
        if self.ser:
            try:
                while not settings.STOP_READ:
                    try:
                        data = self.read()
                        if data:                            
                            # print(data.strip())

                            if settings.BMC.str.lower() == 'penta':
                                notify = panels.Hertek()
                                notify.penta(data)
                            elif settings.BMC == None:
                                notify = panels.Generic()
                                notify.generic()

                    except serial.SerialException as e:
                        logger.error("Error reading from serial port!")
                        logger.error(f"{e}")
                        time.sleep(5)
                        self.open()
                        continue
                if settings.STOP_READ:
                    logger.info('Closing read thread.')
            except KeyboardInterrupt:
                pass
            finally:
                self.close()






 