#Faça um programa que leia um número inteiro e imprima os números inteiros de 0 até este número.

numero = int(input("Informe um numero: "))
inicial = 0

while numero > inicial:
    inicial += 1
    print(inicial)