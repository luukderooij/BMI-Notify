import time
import logging
import asyncio

import emoji

from bminotify import settings
from bminotify.notify import Bot
from bminotify.serial import SerialPort


logger = logging.getLogger(__name__)

class Hertek:
    def __init__(self):
        pass
    
    def penta(self, message):
        message = ''
        print('hiereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')

        ser = SerialPort(encoding='ascii', newline=None)
        ser.open()

        try:
            while not settings.STOP_READ:
                try:
                    data = ser.read()
                    print(data)
                    message = data.lstrip()
                    print(message)

                    # if not message.startswith('TOEGANGSNIVEAU') and not message.startswith('Normaal'):
                    #         print('_______________________________________________\n' + ' \n' + message)
                    #         if message.startswith('BRAND'):
                    #             message = emoji.emojize(f':fire: {message}')
                    #         elif message.startswith('Brandmld Hersteld'):
                    #             message = emoji.emojize(f':check_mark: {message}')
                    #         elif message.startswith('Storingen Hersteld'):
                    #             message = emoji.emojize(f':check_mark: {message}')
                    #         elif message.startswith('System Normaal'):
                    #             message = emoji.emojize(f':check_mark: {message}')
                    #         else:
                    #             message = emoji.emojize(f':warning: {message}')
                    #         logger.info(message)
                    #         asyncio.get_event_loop().run_until_complete(Bot().send(message))
                    #         loop = asyncio.new_event_loop()
                    #         asyncio.set_event_loop(loop)
                    #         try:
                    #             loop.run_until_complete(Bot().send(message))
                    #         except SystemExit:
                    #             logger.error('Could not send notification!')
                    #             raise
                    #         finally:
                    #             loop.close()

                except Exception as e:
                    logger.error("Error reading from serial port!")
                    logger.error(e)
                    time.sleep(5)
                    ser.open()
                    continue
                if settings.STOP_READ:
                    logger.info('Closing read thread.')

        except KeyboardInterrupt:
            pass
        finally:
            ser.close()




        # if not message.startswith('TOEGANGSNIVEAU') and not message.startswith('Normaal'):
        #     print('_______________________________________________\n' + ' \n' + message)

        #     if message.startswith('BRAND'):
        #         message = emoji.emojize(f':fire: {message}')
        #     elif message.startswith('Brandmld Hersteld'):
        #         message = emoji.emojize(f':check_mark: {message}')
        #     elif message.startswith('Storingen Hersteld'):
        #         message = emoji.emojize(f':check_mark: {message}')
        #     elif message.startswith('System Normaal'):
        #         message = emoji.emojize(f':check_mark: {message}')
        #     else:
        #         message = emoji.emojize(f':warning: {message}')
                
        #     logger.info(message)

        #     asyncio.get_event_loop().run_until_complete(Bot().send(message))