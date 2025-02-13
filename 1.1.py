import math

x = float(input("Введите значение x: \n"))
y = float(input("Введите значение y: \n"))

left = abs(x ** 2 - x ** 3)
right = (7 * x) / (x ** 3 - 15 * x)
result1 = (left == right)

sin_x = math.sin(x)
cos_y = math.cos(y)
cos_x = math.cos(x)
sin_y = math.sin(y)
tg_xy = math.tan(x * y)
result2 = (sin_x + cos_y) * (cos_x - sin_y) * tg_xy

print("Результат первого выражения:", result1, "Результат второго выражения:", result2)
