m, n = 10, 40  # Пример диапазона
k, l = 3, 5    # Пример простых чисел

k_or_l = {x for x in range(m, n + 1) if x % k == 0 or x % l == 0}

kl = {x for x in range(m, n + 1) if x % (k * l) == 0}

print("Числа, делящиеся на", k, "или", l, ":", k_or_l)
print("Числа, делящиеся на произведение", k * l, ":", kl)
