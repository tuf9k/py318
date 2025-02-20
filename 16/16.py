from vstavka import vstavit

spisok = input("Введите числа через пробел: ").split()
spisok = [int(chislo) for chislo in spisok]

newnum = int(input("Введите число для вставки: "))
pozic = int(input("Введите позицию для вставки (начиная с 0): "))

noviy_spisok = vstavit(spisok, newnum, pozic)
print("Новый список:", noviy_spisok)