text = "Текста на русском языке, вау мяу прикольно."
gluhie = set("пфктшсхцчщ") 
slova = text.lower().split()  
result = set()

for bukva in gluhie:
    cnt = sum(1 for slovo in slova if bukva not in slovo) 
    if cnt == 1:  
        result.add(bukva)

print("Глухие согласные, не входящие только в одно слово:", sorted(result))
