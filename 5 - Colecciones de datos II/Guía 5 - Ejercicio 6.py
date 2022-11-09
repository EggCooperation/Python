lista_1 = ["h", "o", "l", "a", " ", "m", "u", "n", "d", "o"]
lista_2 = ["h", "o", "l", "a", " ", "l", "u", "n", "a"]
lista_3 = []

for i in lista_1:
    if (i in lista_2) and (i not in lista_3):
        lista_3.append(i)

print(lista_3)