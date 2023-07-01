gabarito = open("data/gabarito.txt", "r").readlines()
respostas = open("data/respostas.txt", "r").readlines()

total = 0
certas = 0
erradas = 0
for i in range(len(gabarito)):
    esperado = gabarito[i][0:1]
    respondido = respostas[i][0:1]
    if respondido != 'D':
        if esperado == respondido:
            total += 1
            certas += 1
            print(respondido, esperado, "+1")
        else:
            total -= 1
            erradas += 1
            print(respondido, esperado, "-1")
    else:
        print(respondido, esperado, "+0")

print("Pontuação: ", total)
print("Certas: ", certas)
print("Erradas: ", erradas)
