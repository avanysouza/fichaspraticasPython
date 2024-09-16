# Faça um algoritmo que leia dois números inteiros, representando os valores início e fim de um intervalo e
# imprima os múltiplos de 5 entre eles

inicio = int(input("Introduza um numero: "))
fim = int(input("Introduza um numero: "))

for i in range(inicio,fim+1):
    if(i % 5 == 0):
        print(i)