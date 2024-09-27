# Escreva uma função que leia um valor inteiro positivo (deve solicitar números até que seja inteiro e positivo) e
# crie uma outra função que imprima numa linha um número de asteriscos igual ao valor inserido pelo utilizador.



def lerNumero():
    num = int(input("Introduza um numero: "))
    if (num >= 0):
        print(num)
        return num
    else:
        print("Numero invalido")

quantidade = lerNumero()

def imprimirAsteriscos(quantidade):
    for i in range(quantidade):
        return print("*" * quantidade)

imprimirAsteriscos(quantidade)