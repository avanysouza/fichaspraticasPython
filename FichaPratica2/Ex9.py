#Crie um programa que mostre o menor de três números inteiros lidos.

num1 = eval(input('Informe um numero: '))
num2 = eval(input('Informe um numero: '))
num3 = eval(input('Informe um numero: '))

if(num1 < num2 and num1 < num3):
   menor = num1
elif(num2 < num1 and num2 < num3):
    menor = num2
else:
    menor = num3

print(f'O menor valor digitado foi {menor}')