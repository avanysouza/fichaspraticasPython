#Escreva um programa que pergunta ao utilizador o tamanho de uma lista, seguidamente instancie uma lista com
#esse tamanho e permita ao utilizador preencher a mesma. Finalmente, pergunte um novo valor e em que posição
#quer colocar.

quantidade = int(input("Quantos elementos quer inserir no Array: "))
lista = []

for i in range(quantidade):
    lista.append(int(input(f"Insira um número o Array [{i}]: ")))

print(lista)

novoValor = int(input("Novo valor: "))
indice = int(input(f"Índice do novo valor(0-{quantidade-1}): "))

lista.insert(indice, novoValor)

#Imprimir a lista com o novo valor inserido no indice
print(lista)
