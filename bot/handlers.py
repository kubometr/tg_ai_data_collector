from aiogram.types import Message
from config import PARSER_MANAGER
import os

UPLOAD_DIR = "storage/uploads"
PARSED_DIR = "storage/parsed"

async def handle_document(message: Message):
    document = message.document
    file_name = document.file_name

    file_path = os.path.join(UPLOAD_DIR, file_name)
    await document.download(destination_file=file_path)

    parsed_text = PARSER_MANAGER.parse(file_path)
    if parsed_text:
        parsed_path = os.path.join(PARSED_DIR, file_name + ".txt")
        with open(parsed_path, "w", encoding="utf-8") as f:
            f.write(parsed_text)
        await message.reply("Файл обработан и текст сохранён.")
    else:
        await message.reply("Не удалось обработать файл.")
