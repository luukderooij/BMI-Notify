import logging
import asyncio

from bminotify.notify import Bot


logger = logging.getLogger(__name__)

class Generic:
    def __init__(self):
        pass
    
    def generic(self, message):        
        logger.info(message)

        asyncio.get_event_loop().run_until_complete(Bot().send(message))