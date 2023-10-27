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
    
    def penta(self):
        message = ''
        reconnect = 0

        ser = SerialPort(encoding='ascii', newline=None)
        ser.open()

        try:
            while not settings.STOP_READ:
                if settings.STOP_READ:
                    logger.info('Closing Hertek Penta read loop.')
                    break
                
                try:
                    data = ser.read()
                    data = data.lstrip()

                    if len(data) > 1:
                        message = message + data

                    if len(message) > 1 and len(data) <= 1:
                        logger.info(message)
                        if not message.startswith('TOEGANGSNIVEAU') and not message.startswith('Normaal'):
                            if message.startswith('BRAND'):
                                message = emoji.emojize(f':fire: {message}')
                            elif message.startswith('Brandmld Hersteld'):
                                message = emoji.emojize(f':check_mark: {message}')
                            elif message.startswith('Storingen Hersteld'):
                                message = emoji.emojize(f':check_mark: {message}')
                            elif message.startswith('System Normaal'):
                                message = emoji.emojize(f':check_mark: {message}')
                            else:
                                message = emoji.emojize(f':warning: {message}')
                            
                            loop = asyncio.new_event_loop()
                            asyncio.set_event_loop(loop)

                            try:
                                loop.run_until_complete(Bot().send(message))
                            except SystemExit:
                                logger.error('Could not send notification!')
                                raise
                            finally:
                                loop.close()

                        message = ""

                except Exception as e:
                    if reconnect > 5:
                        settings.STOP_READ = True
                    logger.error("Error reading from serial port!")
                    logger.error(e)
                    time.sleep(5)
                    ser.open()
                    reconnect += 1
                    continue
                except KeyboardInterrupt:
                    settings.STOP_READ = True

        except KeyboardInterrupt:
            pass
        finally:
            ser.close()

