#Escreva um programa que leia 3 números, seguidamente deve colocar os números no ecrã por ordem crescente.

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite um numero: '))

maior = 0
menor = 0
meio = 0

if(num1 < num2 and num1 < num3):
   menor = num1
elif(num2 < num1 and num2 < num3):
    menor = num2
else:
    menor = num3

if(num1 > num2 and num1 > num3):
    maior = num1
elif(num2 > num1 and num2 > num3):
    maior = num2
else:
    maior = num3

if(num1 > menor and num1 < maior):
    meio = num1
elif(num2 > menor and num2 < maior):
    meio = num2
else:
    meio = num3

print(f"{menor}, {meio}, {maior}")

