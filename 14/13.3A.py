rasshifr_text = ''

with open('file.txt', 'r', encoding='utf-8') as file:
    zashifr_text = file.read()


for simvol in zashifr_text:
    if 'а' <= simvol <= 'я':
        if simvol == 'а':
            rasshifr_text += 'я'
        else:
            rasshifr_text += chr(ord(simvol) - 1)
    elif 'А' <= simvol <= 'Я':
        if simvol == 'А':
            rasshifr_text += 'Я'
        else:
            rasshifr_text += chr(ord(simvol) - 1)
    else: #для символов
        rasshifr_text += simvol

with open('rasshifr_file.txt', 'w', encoding='utf-8') as file:
    file.write(rasshifr_text)

print("Текст успешно расшифрован и записан в файл 'rasshifr_file.txt'")
