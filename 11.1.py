text = "Это строка троки: в ней есть двоеточия: и еще одно: вау"
replace_count = 0
text_list = list(text)

for i in range(len(text_list)):
    if text_list[i] == ':':
        text_list[i] = ';'
        replace_count += 1

new_text = ''.join(text_list)
print("Исходная строка:", text)
print("Измененная строка:", new_text)
print("Количество замен:", replace_count)