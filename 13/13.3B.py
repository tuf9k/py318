def proverka(file):
    try:
        with open(file, 'r') as f:
            chisla = [float(line.strip()) for line in f]


        for i in range(1, len(chisla)):
            if chisla[i] < chisla[i - 1]:
                return False
        return True
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return False



file = 'test.txt'
rezultat = proverka(file)
print(rezultat)
