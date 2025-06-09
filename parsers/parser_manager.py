import os
from parsers.txt_parser import parse_txt
from parsers.pdf_parser import parse_pdf
from parsers.docx_parser import parse_docx
from parsers.doc_parser import parse_doc       # импорт для .doc
from parsers.epub_fb2_parser import parse_epub_fb2
from parsers.rtf_parser import parse_rtf

class ParserManager:
    def parse(self, file_path):
        ext = os.path.splitext(file_path)[1].lower()
        text = ""

        try:
            if ext == ".txt":
                text = parse_txt(file_path)
            elif ext == ".pdf":
                text = parse_pdf(file_path)
            elif ext == ".docx":
                text = parse_docx(file_path)
            elif ext == ".doc":
                text = parse_doc(file_path)
            elif ext in [".fb2", ".epub"]:
                text = parse_epub_fb2(file_path)
            elif ext == ".rtf":
                text = parse_rtf(file_path)
            else:
                print(f"[ParserManager] ❌ Неизвестный формат файла: {file_path} (расширение: {ext})")
                return ""

            if text:
                print(f"[ParserManager] ✅ Парсинг завершён. Файл удалён: {file_path}")
            else:
                print(f"[ParserManager] ⚠️ Парсинг не дал результата. Файл удалён: {file_path}")

            return text

        except Exception as e:
            print(f"[ParserManager] 🔥 Ошибка при парсинге {file_path}: {e}")
            return ""

        finally:
            # Удаляем файл вне зависимости от результата
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except Exception as delete_error:
                    print(f"[ParserManager] ❌ Ошибка при удалении файла {file_path}: {delete_error}")
