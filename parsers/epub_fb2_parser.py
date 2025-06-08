import chardet
from bs4 import BeautifulSoup

def parse_epub_fb2(file_path):
    ext = file_path.lower().split('.')[-1]
    try:
        if ext == "epub":
            from zipfile import ZipFile
            text = ""
            with ZipFile(file_path, 'r') as z:
                for fname in z.namelist():
                    if fname.endswith((".html", ".xhtml")):
                        with z.open(fname) as f:
                            soup = BeautifulSoup(f.read(), "html.parser")
                            text += soup.get_text(separator="\n")
            return text.strip()

        elif ext == "fb2":
            # Читаем бинарно и пытаемся определить кодировку
            raw = open(file_path, "rb").read()
            detected = chardet.detect(raw)
            encoding = detected['encoding'] if detected['encoding'] else 'utf-8'

            # Открываем с найденной кодировкой
            text = raw.decode(encoding, errors='ignore')
            soup = BeautifulSoup(text, "xml")
            paragraphs = soup.find_all('p')
            return "\n".join(p.get_text() for p in paragraphs).strip()

        else:
            return ""
    except Exception as e:
        print(f"[parse_epub_fb2] Ошибка парсинга {file_path}: {e}")
        return ""
