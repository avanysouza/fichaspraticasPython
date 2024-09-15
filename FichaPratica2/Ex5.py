#Escreva um programa que leia dois valores numéricos e apresente o menor e depois o maior.

num1 = eval(input('Informe um numero: '))
num2 = eval(input('Informe um numero: '))

if(num1 > num2):
   menor = num2
   maior = num1
elif(num1 < num2):
    menor = num1
    maior = num2
else:
    print(f"Os numeros sao iguais")


print(f"{menor}      {maior}")