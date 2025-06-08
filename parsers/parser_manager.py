import os
from parsers.txt_parser import parse_txt
from parsers.pdf_parser import parse_pdf
from parsers.docx_parser import parse_docx
from parsers.epub_fb2_parser import parse_epub_fb2

class ParserManager:
    def parse(self, file_path):
        ext = os.path.splitext(file_path)[1].lower()
        if ext == ".txt":
            return parse_txt(file_path)
        elif ext == ".pdf":
            return parse_pdf(file_path)
        elif ext == ".docx":
            return parse_docx(file_path)
        elif ext in [".fb2", ".epub"]:
            return parse_epub_fb2(file_path)
        else:
            return ""
