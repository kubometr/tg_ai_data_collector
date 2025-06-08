import os
from parsers.parser_manager import ParserManager

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

PARSER_MANAGER = ParserManager()
