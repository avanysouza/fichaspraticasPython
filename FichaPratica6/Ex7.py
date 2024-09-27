# Implemente um programa que armazene nu uma lista 10 valores pedidos ao utilizador, e retorne o maior valor
# par inserido. Caso não exista, deverá informar o utilizador

valores = []
pares = []

for i in range(1, 11):
    valores.append(input(f"Informe um valor {i}: "))

def numerosPares(valores):
    for k in range(len(valores)):
        if int(valores[k]) % 2 == 0:
            pares.append(int(valores[k]))
    return pares

print("Lista de numeros: ",valores)
print("Numeros pares: ", numerosPares(valores))


def maiorPar(pares):
    maior = 0
    for m in range(len(pares)):
        if int(pares[m]) > maior:
            maior = int(pares[m])
        return maior

print("Maior numero par: ", maiorPar(pares))



