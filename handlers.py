import os
from aiohttp import ClientSession
from aiogram.types import Message
from config import PARSER_MANAGER
import traceback

UPLOAD_DIR = "storage/uploads"
PARSED_DIR = "storage/parsed"

async def download_file(bot, file_id: str, destination: str):
    file_info = await bot.get_file(file_id)
    file_url = f"https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}"
    async with ClientSession() as session:
        async with session.get(file_url) as resp:
            if resp.status == 200:
                with open(destination, "wb") as f:
                    f.write(await resp.read())


async def handle_document(message: Message):
    document = message.document
    file_name = document.file_name
    file_path = os.path.join(UPLOAD_DIR, file_name)

    await download_file(message.bot, document.file_id, file_path)

    try:
        if not os.path.exists(file_path):
            await message.answer("❌ Файл не был загружен.")
            return

        parsed_text = PARSER_MANAGER.parse(file_path)

        if parsed_text and parsed_text.strip():
            parsed_path = os.path.join(PARSED_DIR, file_name + ".txt")
            with open(parsed_path, "w", encoding="utf-8") as f:
                f.write(parsed_text)

            await message.answer("✅ Файл обработан и текст сохранён.")
        else:
            await message.answer("⚠️ Файл загружен, но не удалось его распарсить.")
    except Exception as e:
        await message.answer("❌ Произошла ошибка при обработке файла.")
        print("Ошибка парсера:", e)
        traceback.print_exc()
