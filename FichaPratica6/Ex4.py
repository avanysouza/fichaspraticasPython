# Escreva um programa que lê uma lista de tamanho 10 e encontra o menor elemento. Agora tente escrever o
# mesmo programa sem usar a função de ordenação

numeros = [15,20,30,54,1,5,500,16,18,48]

def menorNumero(numeros):
    menor = numeros[0]
    for i in range(len(numeros)):
        if numeros[i] < menor:
            menor = numeros[i]
    return menor


print("O menor número da lista é: ", menorNumero(numeros))

