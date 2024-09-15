#Escreva um programa que leia dois valores numéricos e apresente o maior e depois o menor


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


print(f"{maior}      {menor}")