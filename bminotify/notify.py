import logging
import asyncio
import time

import schedule
import telegram
from telegram.ext import Application

from bminotify import settings

logger = logging.getLogger(__name__)


def weekly_test():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        loop.run_until_complete(Bot().send('Wekelijkse test melding'))
    except SystemExit:
        logger.error('Could not send weekly test notification!')
        raise
    finally:
        loop.close()

def weekly_test_schedule():
    schedule.every(10).seconds.do(weekly_test)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        if settings.STOP_WEEKLY_TEST:
            break


class Bot:
    def __init__(self):
        try:         
            self.application = Application.builder().token(settings.BOT_TOKEN).build()
        except:
            logger.error("Something went wrong with setting up the bot!")


    async def send(self, msg):
        if settings.CHAT_ID:
            try:
                await self.application.bot.send_message(chat_id=settings.CHAT_ID, text=msg)
            except telegram.error.InvalidToken as e: 
                logger.error("Invalid bot token!")
                logger.error(e)
            except telegram.error.Forbidden as e: 
                logger.error('Bot doesnt have rights to preform requested action.')
                logger.error(e)
            except:
                logger.error("Something went wrong with sending the messsage!")
        else: 
            logger.info('First set up a chat id')



