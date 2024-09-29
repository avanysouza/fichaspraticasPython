#Escreva um programa que permita preencher uma lista de tamanho 10 e, seguidamente, pesquisar se a lista tem
#um determinado valor. No final deve indicar se o valor existe ou não, e caso exista, indique também o índice de
#todas as ocorrências.

valores = []

for i in range(1, 11):
    valores.append(input(f"Informe um valor {i}: "))

pesquisa = input("Informe o numero para pesquisa: ")

def pesquisarNumero(valores, pesquisa):
    indice = []
    for m in range(len(valores)):
        if valores[m] == pesquisa:
            indice.append(m)
    return indice

indice_pesquisa = pesquisarNumero(valores, pesquisa)

if pesquisarNumero(valores, pesquisa):
    print(f"{pesquisa} existe na lista nos indices {indice_pesquisa}")
else:
    print(f"{pesquisa} não existe na lista!")