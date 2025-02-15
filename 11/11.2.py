text = "Пример текста вау мяу."
glas = "аеёиоуыэюя"
glas_count = sum(1 for char in text.lower() if char in glas)
sogl_count = sum(1 for char in text.lower() if char.isalpha() and char not in glas)

print("Гласных:", glas_count)
print("Согласных:", sogl_count)

if glas_count > sogl_count:
    print("Гласных больше")
elif sogl_count > glas_count:
    print("Согласных больше")
else:
    print("Гласных и согласных поровну")
