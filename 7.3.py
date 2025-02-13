array1 = list(map(int, input("Введите элементы первого массива через пробел: ").split()))
array2 = list(map(int, input("Введите элементы второго массива через пробел: ").split()))

k = int(input("Введите число k: "))
result = array1[:k] + array2 + array1[k:]

print("Объединенный массив:", result)