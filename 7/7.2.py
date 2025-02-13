
N = int(input("Введите количество чисел N: "))

numbers = []
for i in range(N):
    num = float(input(f"Введите число {i+1}: "))
    numbers.append(num)

min_num = min(numbers)
max_num = max(numbers)

if numbers[3] >= 0:
    mnj = min_num ** 2
else:
    mnj = max_num ** 2
for i in range(N):
    numbers[i] *= mnj
print("Результат:", numbers)
