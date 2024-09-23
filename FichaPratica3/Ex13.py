# Escreva um programa que leia uma sequência de números inteiros do utilizador e determine se a sequência
# está em ordem crescente

count = 1
contador = int(input("Quantos numeros desejam inserir: "))
crescente = True

anterior = int(input("Introduza um numero: "))


while count < contador:
    atual = int(input("Introduza um numero: "))
    count += 1
    if atual <= anterior:
        crescente:False

    anterior = atual

if crescente:
    print("Crescente")
else:
    print("Nao crescente")