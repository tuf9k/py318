import re

def remove_extra_spaces(text):
    text = re.sub(r'\s{3,}', '  ', text)
    text = re.sub(r'\s+\.', '.', text)
    text = text.rstrip()

    return text

input_text = "Это   пример строки с   лишними пробелами.   "
cleaned_text = remove_extra_spaces(input_text)
print(cleaned_text)
