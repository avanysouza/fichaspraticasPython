#Faça um programa que imprima os números pares no intervalo de 1 a 400 inclusive. (Não necessita de input do
#utilizador). Exemplo de execução:

numero = 0

while numero >= 0 and numero <= 400:
    numero = numero + 1
    if(numero % 2 == 0):
        print(numero)