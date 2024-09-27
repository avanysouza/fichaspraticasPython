# Escreva um programa que permita adicionar 10 números inteiros a uma lista e que os imprima pela ordem inversa
# de inserção.

valores = []

for i in range(1, 11):
    valores.append(input(f"Informe um valor {i}: "))

print(valores)

valores.sort(reverse=True)
inverso=valores
print(inverso)