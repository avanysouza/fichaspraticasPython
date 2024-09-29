#Escreva um programa que lê uma lista de tamanho 10 e encontra o maior elemento. Agora tente escrever o
#mesmo programa sem usar a função de ordenação.


numeros = [5,8,65,98,59,205,15,58,61,10]

#Função for para ler os 10 números inteiros e encontrar o maior

def encontrarmaior(numeros):
    maior = numeros[0]
    for i in range(0,len(numeros)):
        if numeros[i] > maior:
            maior = numeros[i]
    return maior

maior = encontrarmaior(numeros)
print(numeros)
print(maior)