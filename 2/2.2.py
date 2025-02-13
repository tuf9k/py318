x1 = float(input("Введите x1: \n"))
y1 = float(input("Введите y1: \n"))
x2 = float(input("Введите x2: \n"))

x3 = float(input("Введите x3: \n"))
y3 = float(input("Введите y3: \n"))
x4 = float(input("Введите x4: \n"))

x_left = max(x1, x3)
x_right = min(x2, x4)
y_top = min(y1, y3)
y_bottom = 0


if x_left < x_right and y_top > y_bottom:
    width = x_right - x_left
    height = y_top - y_bottom
    area = width * height
    print("Прямоугольники пересекаются. Площадь пересечения:", area)
else:
    print("Прямоугольники не пересекаются.")
