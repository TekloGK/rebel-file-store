import asyncio
import warnings
from bot import bot
from handlers import logger
import time


bot_loop = asyncio.get_event_loop()

def main_func():
    async def start_services():
      try:
		 await bot.start() 
      except:
         logger.error('error', exc_info=True)
         
    bot_loop.run_until_complete(start_services())
    bot_loop.run_forever()
	
if __name__ == "__main__":
    warnings.filterwarnings("ignore", message="There is no current event loop")
    main_func()
