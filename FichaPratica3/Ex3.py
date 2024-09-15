#Faça um programa que imprima os números ímpares no intervalo de 531 a 750 inclusive. (Não necessita de
#input do utilizador)

numero = 530

while numero >= 530 and numero <= 749:
    numero += 1
    if(numero % 2 == 1):
        print(numero)