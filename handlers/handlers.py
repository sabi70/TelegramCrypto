from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ParseMode
from database import DataBase

database = DataBase()
router = Router()


@router.message(Command('start'))
async def on_start(message: Message):
  await message.answer_photo(
    photo='https://overclockers.ru/st/legacy/blog/422417/472220_O.png',
    caption=database.get_greeting(),
    parse_mode=ParseMode.HTML
    )
