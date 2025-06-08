from aiogram.types import Message
from aiogram import Bot
from config import PARSER_MANAGER
import os
from pathlib import Path

UPLOAD_DIR = Path("storage/uploads")
PARSED_DIR = Path("storage/parsed")

async def handle_document(message: Message, bot: Bot):
    document = message.document
    file_id = document.file_id
    file_name = document.file_name

    file_path = UPLOAD_DIR / file_name
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    PARSED_DIR.mkdir(parents=True, exist_ok=True)

    # Получаем файл и сохраняем его
    file = await bot.get_file(file_id)
    await bot.download_file(file.file_path, destination=file_path)

    # Парсинг текста
    parsed_text = PARSER_MANAGER.parse(str(file_path))

    if parsed_text:
        parsed_path = PARSED_DIR / (file_name + ".txt")
        with open(parsed_path, "w", encoding="utf-8") as f:
            f.write(parsed_text)
        await message.answer("✅ Файл обработан и текст сохранён.")
    else:
        await message.answer("⚠️ Не удалось обработать файл.")
