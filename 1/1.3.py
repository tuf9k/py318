# Ввод двух дат
year1 = int(input("Введите год первой даты: \n"))
month1 = int(input("Введите месяц первой даты: \n"))
day1 = int(input("Введите день первой даты: \n"))
hour1 = int(input("Введите час первой даты: \n"))
minute1 = int(input("Введите минуту первой даты: \n"))
second1 = int(input("Введите секунду первой даты: \n"))

year2 = int(input("Введите год второй даты: \n"))
month2 = int(input("Введите месяц второй даты: \n"))
day2 = int(input("Введите день второй даты: \n"))
hour2 = int(input("Введите час второй даты: \n"))
minute2 = int(input("Введите минуту второй даты: \n"))
second2 = int(input("Введите секунду второй даты: \n"))


if year1 > year2:
    result = True
elif year1 == year2:
    if month1 > month2:
        result = True
    elif month1 == month2:
        if day1 > day2:
            result = True
        elif day1 == day2:
            if hour1 > hour2:
                result = True
            elif hour1 == hour2:
                if minute1 > minute2:
                    result = True
                elif minute1 == minute2:
                    if second1 > second2:
                        result = True
                    else:
                        result = False
                else:
                    result = False
            else:
                result = False
        else:
            result = False
    else:
        result = False
else:
    result = False

print("Результат:", result)
