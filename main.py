import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import ContentTypeFilter
from aiogram.types import Message
from config import BOT_TOKEN
from handlers import handle_document
import os

os.makedirs("storage/uploads", exist_ok=True)
os.makedirs("storage/parsed", exist_ok=True)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def doc_handler(message: Message):
    await handle_document(message)

def register_handlers(dp: Dispatcher):
    dp.message.register(doc_handler, ContentTypeFilter(content_types=[types.ContentType.DOCUMENT]))

async def main():
    register_handlers(dp)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
