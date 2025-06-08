from zipfile import ZipFile
from bs4 import BeautifulSoup

def parse_epub_fb2(file_path):
    ext = file_path.lower().split('.')[-1]
    try:
        if ext == "epub":
            # EPUB — это ZIP архив с XHTML файлами
            text = ""
            with ZipFile(file_path, 'r') as z:
                # Найдём все html/xhtml файлы и соберём текст из них
                for fname in z.namelist():
                    if fname.endswith((".html", ".xhtml")):
                        with z.open(fname) as f:
                            soup = BeautifulSoup(f.read(), "html.parser")
                            text += soup.get_text(separator="\n")
            return text.strip()
        
        elif ext == "fb2":
            # FB2 — это XML, читаем через BeautifulSoup
            with open(file_path, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f, "xml")
                # Собираем весь текст из элементов <p> (абзацы)
                paragraphs = soup.find_all('p')
                return "\n".join(p.get_text() for p in paragraphs).strip()
        
        else:
            return ""
    except Exception as e:
        print(f"[parse_epub_fb2] Ошибка парсинга {file_path}: {e}")
        return ""
