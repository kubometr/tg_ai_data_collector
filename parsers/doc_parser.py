import textract

def parse_doc(file_path):
    try:
        text = textract.process(file_path).decode('utf-8')
        return text
    except Exception as e:
        print(f"[parse_doc] Ошибка при разборе файла {file_path}: {e}")
        return ""
