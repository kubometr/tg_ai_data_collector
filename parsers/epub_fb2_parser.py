def parse_epub_fb2(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return ""
