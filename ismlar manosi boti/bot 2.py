import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message
from ismlar import ismlar_manosi
from mykeys import auto_keyboard


TOKEN = "6809382344:AAHjPJARE9n-MYDh0-vBQYwLwWpKKRrMfRU" 
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
   await message.answer(text="salom",reply_markup=auto_keyboard().as_markup(resize_keyboard=True,input_field_placeholder="menyulardan  birini tanlang yoki isim kiriting👇👇"))

@dp.message(F.text)
async def ism_funksiyasi(message:Message):
    ism = message.text
    natija = ismlar_manosi(ism)
    await message.answer(text=natija)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
