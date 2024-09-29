#Implemente um programa que permita adicionar 10 números inteiros a uma lista e que os imprima pela ordem
#de inserção.

numeros = []

#Ciclo for para solicitar os 10 números inteiros
for i in range(1,11):
    numeros.append(input(f"Insira um número no Array {i}: "))

print(numeros)


