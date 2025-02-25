import math

n = int(input("Введите размер матрицы n: "))

matrica = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0:
            matrica[i][j] = float('inf')
        else:
            matrica[i][j] = (math.cos(i) / math.sin(i)) ** 2 - math.sqrt(3) * j + 2

sumsecstolb = sum(matrica[i][1] for i in range(n))

minelthirdstr = min(matrica[2])

proizotric = 1
for i in range(n):
    for j in range(n):
        if matrica[i][j] < 0:
            proizotric *= matrica[i][j]

print("Сумма эл-ов 2 столбца:", sumsecstolb)
print("Минимальный эл-т 3 строки:", minelthirdstr)
print("Произведение отрицательных эл-e:", proizotric)