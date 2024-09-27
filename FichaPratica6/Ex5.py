# Escreva um programa que lê uma lista, até que o utilizador introduza um número negativo (que não deve ser
# armazenado na lista) e calcula a média dos elementos.

num = 0
numeros = []
soma = 0

#Ciclo while enquanto o numero for menor que -1:
while num >=0:
    num = int(input("Informe um numero: "))
    if num >= 0:
        numeros.append(num)

for i in range(len(numeros)):
    soma += numeros[i]

def tamanhoVetor(numeros):
    for _ in numeros:
        count = numeros.count(numeros[i])
        return count

quantidade = tamanhoVetor(numeros)

media = soma / quantidade
print(f"A média dos elementos é igual a: {media}")