# roman_numerals.py

def k_rimskomu(n):
    znach = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    simvoly = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    rimskoye_chislo = ''
    for i in range(len(znach)):
        while n >= znach[i]:
            rimskoye_chislo += simvoly[i]
            n -= znach[i]
    return rimskoye_chislo

def iz_rimskogo(s):
    rimskie_numeraly = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500,
        'M': 1000
    }
    obshchaya_summa = 0
    predydushchee_znachenie = 0
    for char in reversed(s):
        znachenie = rimskie_numeraly[char]
        if znachenie < predydushchee_znachenie:
            obshchaya_summa -= znachenie
        else:
            obshchaya_summa += znachenie
        predydushchee_znachenie = znachenie
    return obshchaya_summa

def slozhit_rimskie(a, b):
    return k_rimskomu(iz_rimskogo(a) + iz_rimskogo(b))

def vychitat_rimskie(a, b):
    return k_rimskomu(iz_rimskogo(a) - iz_rimskogo(b))

def umnozhit_rimskie(a, b):
    return k_rimskomu(iz_rimskogo(a) * iz_rimskogo(b))

def tselochisl_dividit_rimskie(a, b):
    return k_rimskomu(iz_rimskogo(a) // iz_rimskogo(b))

def ostatok_rimskie(a, b):
    return k_rimskomu(iz_rimskogo(a) % iz_rimskogo(b))

def sravnit_rimskie(a, b):
    a_val = iz_rimskogo(a)
    b_val = iz_rimskogo(b)
    return {
        'ravno': a_val == b_val,
        'ne_ravno': a_val != b_val,
        'bolshe': a_val > b_val,
        'menshe': a_val < b_val,
        'bolshe_ravno': a_val >= b_val,
        'menshe_ravno': a_val <= b_val
    }
