import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import Config 
from handlers import handlers 


async def main():
  config = Config()
  bot = Bot(config.get_token())
  dp = Dispatcher()
  dp.include_router(handlers.router)
  await dp.start_polling(bot)


if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO)
  try:
    asyncio.run(main())
  except KeyboardInterrupt:
    print('Exit')
