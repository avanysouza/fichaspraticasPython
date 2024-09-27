# Escreva um método chamado "imprimirTabuada" que recebe um número inteiro como parâmetro e imprime a
# tabuada desse número de 1 a 10.

num = input("Informe um numero: ")

def imprimirTabuada(num):
    for i in range(1,11):
        resultado = int(num)*int(i)
        print(f"{num} x {i} = {resultado}")

imprimirTabuada(num)