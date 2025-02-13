x = float(input("Введите координату x: \n"))
y = float(input("Введите координату y: \n"))

in_square1 = (-6 <= x <= -3) and (-3 <= y <= 7)
in_square2 = (-3 <= x <= -1) and (2 <= y <= 7)

result = in_square1 or in_square2

print("Результат:", result)
