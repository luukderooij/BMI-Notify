import logging
import asyncio

import emoji

from bminotify.notify import Bot


logger = logging.getLogger(__name__)

class Esser:
    def __init__(self):
        pass
    
    def esser8000(self, message):
        logger.info(f'Message {message}')

        if message>'':
                m_text += message + '\n' + '\r'
                c1, c2=True, False

        if message=='':
                c2=True

        if c1==True and c2==True and m_text.strip()>'':
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
                        message = emoji.emojize(f':fire: {m_text}')

                    if m_text.startswith('STORING hersteld'):
                        message = emoji.emojize(f':check_mark: {m_text}')
                    elif m_text.startswith('STORING'):
                        message = emoji.emojize(f':warning: {m_text}')
                        
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)

                    #asyncio.get_event_loop().run_until_complete(Bot().send(message))

                    try:
                        loop.run_until_complete(Bot().send(message))
                    except SystemExit:
                        logger.error('Could not send notification!')
                        raise
                    finally:
                        loop.close()


                m_text=''
                c1, c2=False, False








        # m_text = message

        # m_text=m_text.strip()

        # logger.info(f'M-text 1:  {m_text}')
        # m_text=m_text.replace('F I R E', 'BRAND')
        # m_text=m_text.replace('FIRE', 'BRAND')
        # m_text=m_text.replace('B R A N D', 'BRAND')
        # m_text=m_text.replace('F A U L T', 'STORING')
        # m_text=m_text.replace('FAULT', 'STORING')
        # m_text=m_text.replace('S T O R I N G', 'STORING')

        # logger.info(f'M-text 2:  {m_text}')

        # #Verzend alleen brand en storings meldingen
        # if m_text.startswith('BRAND') or m_text.startswith('Normaal') or m_text.startswith('STORING'):

        #     if m_text.startswith('BRAND gereset'):
        #         message = emoji.emojize(f':check_mark: {m_text}')
        #     elif m_text.startswith('BRAND'):
        #         message = emoji.emojize(f':fire: {m_text}')

        #     if m_text.startswith('STORING hersteld'):
        #         message = emoji.emojize(f':check_mark: {m_text}')
        #     elif m_text.startswith('STORING'):
        #         message = emoji.emojize(f':warning: {m_text}')
                
        #     logger.info(message)

        #     loop = asyncio.new_event_loop()
        #     asyncio.set_event_loop(loop)

        #     #asyncio.get_event_loop().run_until_complete(Bot().send(message))

        #     try:
        #         loop.run_until_complete(Bot().send(message))
        #     except SystemExit:
        #         logger.error('Could not send notification!')
        #         raise
        #     finally:
        #         loop.close()