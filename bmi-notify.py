#!/usr/bin/env python3
import os
import time
import logging
import asyncio
import threading

from logging.handlers import RotatingFileHandler

from bminotify import settings, panels
from bminotify.config import Configuration
from bminotify.notify import Bot, weekly_test_schedule


__version__ = "1.0.4"
__date__ = "2-4-2023"


class BMINotify:
    def __init__(self):
        pass

    def start(self):
        settings.DATA_DIR = os.path.dirname(os.path.abspath(__file__))
        print(f"Path installation directory:: {settings.DATA_DIR}")

        settings.CONFIG_FILE = os.path.join(settings.DATA_DIR, "config.ini")
        print(f"Path config.ini: {settings.CONFIG_FILE}")

        Configuration(settings.CONFIG_FILE).initialize()

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        file_handler = RotatingFileHandler(settings.LOG_FILE, mode='a', maxBytes=5*1024*1024, 
                                 backupCount=2, encoding=None, delay=0)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        logger.info('Logger started!')

        if os.name == 'nt':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

        if settings.STARTUP_MSG:
            asyncio.get_event_loop().run_until_complete(Bot().send(f'BMI-Notify! \nVersie: {__version__} \nDatum: {__date__}'))

        logger.info("Starting system read thread.")

        if settings.BMC == 'penta':
            system = panels.Hertek()
            serial_read_tread = threading.Thread(target= system.penta)                            
        elif settings.BMC == 'iq8':
            system = panels.Esser()
            serial_read_tread = threading.Thread(target= system.iq8)
        elif settings.BMC == None:
            system = panels.Generic()
            serial_read_tread = threading.Thread(target= system.generic)

        serial_read_tread.start()


        logger.info("Starting weekly test thread.")

        test_tread = threading.Thread(target=weekly_test_schedule)
        test_tread.start()

        # Main loop
        while True:
            time.sleep(1)

            if settings.DEVELOPMENT:
                a = input("Type exit too stop: ")
                if a == 'exit':
                    settings.STOP_READ = True
                    settings.STOP_WEEKLY_TEST = True
                    break


def main():
    BMINotify().start()

if __name__ == "__main__":
    main()