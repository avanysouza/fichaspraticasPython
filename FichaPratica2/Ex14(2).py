#Escreva um programa que leia 3 números, seguidamente deve colocar os números no ecrã por ordem crescente.

#SOLUÇÃO DO FORMADOR VITOR

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite um numero: '))


if(num1 < num2 and num1 < num3 ):
    if(num2 < num3):
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)
if(num2 < num1 and num2 < num3):
    if(num1 < num3):
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)
if(num3 < num1 and num3 < num2):
    if(num1 < num2):
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)