#Escreva um programa que pergunta ao utilizador o tamanho de uma lista, seguidamente instancie uma lista com
#esse tamanho e permita ao utilizador preencher a mesma. No fim, imprima pela ordem de inserção.

quantidade = int(input("Quantos elementos quer inserir no Array: "))
lista = []

for i in range(quantidade):
    lista.append(int(input(f"Insira um número o Array [{i}]: ")))


print(lista)