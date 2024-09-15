#Faça um programa que leia um número inteiro e imprima os 5 anteriores e os 5 seguintes.
#a. Por exemplo: Leu 15, deve imprimir: 10 11 12 13 14 16 17 18 19 20

numero = int(input("Informe um numero: "))


for i in range(5,0,-1):
    anteriores = numero - i
    print(anteriores)

for i in range(1,6):
    seguintes = numero + i
    print(seguintes)
