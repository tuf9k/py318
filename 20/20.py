from roman_numerals import k_rimskomu, iz_rimskogo, slozhit_rimskie, vychitat_rimskie, umnozhit_rimskie, \
    tselochisl_dividit_rimskie, ostatok_rimskie, sravnit_rimskie


def sortirovat_rimskij_massiv(rimskij_massiv):
    desyatichnye_massiv = [iz_rimskogo(num) for num in rimskij_massiv]
    desyatichnye_massiv.sort()
    sortirovannij_rimskij_massiv = [k_rimskomu(num) for num in desyatichnye_massiv]
    return desyatichnye_massiv, sortirovannij_rimskij_massiv


rimskie_chisla = ["XII", "IX", "XX", "V", "III"]
desyatichnye_sortirovannye, rimskie_sortirovannye = sortirovat_rimskij_massiv(rimskie_chisla)

print("Отсортированные числа в десятичной системе:", desyatichnye_sortirovannye)
print("Отсортированные числа в римской системе:", rimskie_sortirovannye)


def find_common_numbers(decimal_array, roman_array):
    roman_set = set(roman_array)
    common_numbers = []

    for num in decimal_array:
        roman_num = k_rimskomu(num)
        if roman_num in roman_set:
            common_numbers.append((num, roman_num))

    return
