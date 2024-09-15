#Escreva um programa que leia 3 números, seguidamente deve perguntar ao utilizador se quer ordem crescente
#‘C’ ou decrescente ‘D’, e deve colocar os números no ecrã por ordem decrescente ou crescente de acordo com a
#escolha.

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite um numero: '))

opcao = int(input('Digite um opcao para exibir os numeros: 1-Crescente 2-Decrescente '))

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

match opcao:
    case 1:
        print(f"{menor}, {meio}, {maior}")
    case 2:
        print(f"{maior}, {meio}, {menor}")
    case _:
        print("Opção invalida!")