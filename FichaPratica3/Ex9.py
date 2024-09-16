# Faça um programa que leia um número inteiro e imprima os números pares entre 2 e o número lido inclusive.
# Suponha que o número lido da entrada será maior que 2

numero = int(input("Digite um numero inteiro: "))
inicial = 2


for i in range (inicial, numero+1):
    if i % 2 == 0:
        print(i)