k = int(input("Введите число k: "))

posld = ""
num = 2

while len(posld) < k:
    posld += str(num)
    num += 2

print(f"{k}-я цифра последовательности: {posld[k - 1]}")
