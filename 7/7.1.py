N = int(input("Введите количество чисел N: "))
K = float(input("Введите число K: "))

numbers = []
for i in range(N):
    num = float(input(f"Введите число {i+1}: "))
    numbers.append(num)

less_K = 0
min_K = 0
biggest_K = 0

for num in numbers:
    if num < K:
        less_K += 1
    elif num == K:
        min_K += 1
    else:
        biggest_K += 1

print(f"меньше K: {min_K}")
print(f"равно K: {less_K}")
print(f"больше K: {biggest_K}")
