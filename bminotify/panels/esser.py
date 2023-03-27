import logging
import asyncio

import emoji

from bminotify.notify import Bot


logger = logging.getLogger(__name__)

class Esser:
    def __init__(self):
        pass
    
    def esser8000(self, message):
        m_text=m_text.strip()
        m_text=m_text.replace('F I R E', 'BRAND')
        m_text=m_text.replace('FIRE', 'BRAND')
        m_text=m_text.replace('B R A N D', 'BRAND')
        m_text=m_text.replace('F A U L T', 'STORING')
        m_text=m_text.replace('FAULT', 'STORING')
        m_text=m_text.replace('S T O R I N G', 'STORING')


        #Verzend alleen brand en storings meldingen
        if m_text.startswith('BRAND') or m_text.startswith('Normaal') or m_text.startswith('STORING'):

            if m_text.startswith('BRAND gereset'):
                message = emoji.emojize(f':check_mark: {m_text}')
            elif m_text.startswith('BRAND'):
                message = emoji.emojize(f':fire: {message}')

            if m_text.startswith('STORING hersteld'):
                message = emoji.emojize(f':check_mark: {m_text}')
            elif m_text.startswith('STORING'):
                message = emoji.emojize(f':warning: {m_text}')
                
            logger.info(message)

            asyncio.get_event_loop().run_until_complete(Bot().send(message))