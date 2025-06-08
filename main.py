import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from config import BOT_TOKEN
from handlers import handle_document
import os

os.makedirs("storage/uploads", exist_ok=True)
os.makedirs("storage/parsed", exist_ok=True)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()  # Убираем bot из аргументов

@dp.message(types.ContentType.DOCUMENT)  # новый синтаксис вместо @dp.message_handler
async def doc_handler(message: Message):
    await handle_document(message)

async def main():
    await dp.start_polling(bot)  # Передаём bot в start_polling

if __name__ == "__main__":
    asyncio.run(main())
