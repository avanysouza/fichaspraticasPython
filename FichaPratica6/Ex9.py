# Escreva um programa que permita preencher uma lista de tamanho 10 e, seguidamente, pesquisar se a lista tem
# determinado valor

valores = []

for i in range(1, 11):
    valores.append(input(f"Informe um valor {i}: "))

pesquisa = input("Informe o numero para pesquisa: ")
encontrado = 0


for i in range(len(valores)):
    if valores[i] == pesquisa:
        encontrado = i
