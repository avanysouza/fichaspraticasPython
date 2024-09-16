# Escreva um programa que leia uma sequência de números inteiros do utilizador e determine se a sequência
# está em ordem crescente

count = 0
contador = int(input("Quantos numeros desejam inserir: "))
anterior = None
crescente = True


while count < contador:
    for i in range (0,contador):
        numero = int(input("Introduza um numero: "))
        if numero < anterior:
            crescente:False
        else:
            crescente:True
            print("Crescente")
        count += 1



