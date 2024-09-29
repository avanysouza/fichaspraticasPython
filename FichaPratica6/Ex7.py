# Implemente um programa que armazene nu uma lista 10 valores pedidos ao utilizador, e retorne o maior valor
# par inserido. Caso não exista, deverá informar o utilizador

valores = []

for i in range(1, 11):
    valores.append(input(f"Informe um valor {i}: "))

def numerosPares(valores):
    pares = []
    for k in range(len(valores)):
        if int(valores[k]) % 2 == 0:
            pares.append(int(valores[k]))
    return pares

listaPares = numerosPares(valores)

if listaPares:
    print("Numeros pares: ", listaPares)


    def maiorPar(listaPares):
        maior = listaPares[0]
        for m in range(len(listaPares)):
            if int(listaPares[m]) > maior:
                maior = int(listaPares[m])
        return maior

    print("Maior numero par: ", maiorPar(listaPares))
else:
    print("Não há numeros pares na lista!")





