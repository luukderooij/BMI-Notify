import logging
import asyncio

import emoji

from bminotify.notify import Bot


logger = logging.getLogger(__name__)

class Hertek:
    def __init__(self):
        pass
    
    def penta(self, message):
        if not message.startswith('TOEGANGSNIVEAU') and not message.startswith('Normaal'):
            print('_______________________________________________\n' + ' \n' + message)

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
                
            logger.info(message)

            asyncio.get_event_loop().run_until_complete(Bot().send(message))