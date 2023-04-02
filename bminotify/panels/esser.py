import time
import logging
import asyncio

import emoji

from bminotify import settings
from bminotify.notify import Bot
from bminotify.serial import SerialPort

logger = logging.getLogger(__name__)

class Esser:
    def __init__(self):
        pass


    def iq8(self):
        message = ''

        ser = SerialPort(encoding='ascii', newline=None)
        ser.open()

        try:
            while not settings.STOP_READ:
                try:
                    data = ser.read()
                    data = data.lstrip()


                    if len(data) > 1:
                        message = message + data


                    if len(message) > 1 and len(data) <= 1:
                        message = message.replace('F I R E', 'BRAND')
                        message = message.replace('FIRE', 'BRAND')
                        message = message.replace('B R A N D', 'BRAND')
                        message = message.replace('F A U L T', 'STORING')
                        message = message.replace('FAULT', 'STORING')
                        message = message.replace('S T O R I N G', 'STORING')

                        logger.info(f'\n {message}')

                        #Verzend alleen brand en storings meldingen
                        if message.startswith('BRAND') or message.startswith('Normaal') or message.startswith('STORING'):

                            if message.startswith('BRAND gereset'):
                                message = emoji.emojize(f':check_mark_button: {message}')
                            elif message.startswith('BRAND'):
                                message = emoji.emojize(f':fire: {message}')

                            if message.startswith('STORING hersteld'):
                                message = emoji.emojize(f':check_mark_button: {message}')
                            elif message.startswith('STORING'):
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

                        message=''

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
