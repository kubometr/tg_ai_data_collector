from aiogram.types import Message
from aiogram import Bot
from config import PARSER_MANAGER
import os
from pathlib import Path

UPLOAD_DIR = Path("storage/uploads")
PARSED_DIR = Path("storage/parsed")

async def handle_document(message: Message):
    bot = message.bot  # Получаем объект бота прямо из message
    document = message.document

    file_info = await bot.get_file(document.file_id)
    file_path = os.path.join("storage/uploads", document.file_name)

    # Скачиваем документ
    await bot.download_file(file_info.file_path, destination=file_path)

    # Парсим
    parsed_text = PARSER_MANAGER.parse(file_path)
    if parsed_text:
        parsed_path = os.path.join("storage/parsed", document.file_name + ".txt")
        with open(parsed_path, "w", encoding="utf-8") as f:
            f.write(parsed_text)
        await message.answer("Файл обработан и текст сохранён.")
    else:
        await message.answer("Не удалось обработать файл.")
