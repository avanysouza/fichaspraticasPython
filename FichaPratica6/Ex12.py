#Escreva um programa que pergunta ao utilizador o tamanho de uma lista, seguidamente instancie uma lista com
#esse tamanho e permita ao utilizador preencher o mesmo. Finalmente, pergunte qual o valor a remover, deve
#remover todas as ocorrências desse valor da lista.

quantidade = int(input("Quantos elementos quer inserir no Array: "))
lista = []

for i in range(quantidade):
    lista.append(int(input(f"Insira um número o Array [{i}]: ")))


print(lista)

remover = int(input("Digite o número que deseja remover da lista: "))
def removerNumero(lista,remover):
    for m in range(len(lista)):
        if lista[m] == remover:
            lista.remove(lista[m])
    return lista

lista_alterada = removerNumero(lista,remover)

print(f"Lista com o valor {remover} removido: ",lista_alterada)