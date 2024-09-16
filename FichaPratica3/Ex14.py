# Escreva um programa que calcule e imprima o fatorial de um número inteiro não-negativo n. Utilize o ciclo
# while.

numero = int(input("Digite um numero: "))
fatorial = 1

while numero > 0:
    fatorial = fatorial * numero
    numero = numero - 1


print(f"Fatorial = {fatorial}")
