def load_srs(file_path):
    with open(file_path, "r") as file:
        text = file.read()
    return text

def clean_text(text):
    text = text.lower()
    return text