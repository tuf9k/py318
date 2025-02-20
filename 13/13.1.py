import random

def createfile(name, kolvonum):
    with open(name, 'w') as file:
        for _ in range(kolvonum):
            chislo = random.uniform(-100, 100)  # пределы рандома
            file.write(f"{chislo}\n")

def nayti_min_i_max(name):
    with open(name, 'r') as file:
        chisla = [float(line.strip()) for line in file]
    minnum = min(chisla)
    maxnum = max(chisla)
    return minnum, maxnum

name = 'chisla.txt'
kolvonum = 10  # Количество чисел в файле

createfile(name, kolvonum)
minnum, maxnum = nayti_min_i_max(name)
summa = minnum + maxnum

print(f"Минимальное число: {minnum}")
print(f"Максимальное число: {maxnum}")
print(f"Сумма минимального и максимального чисел: {summa}")