#Escreva um programa que permita preencher uma lista de tamanho 15, seguidamente crie duas novas listas:
#a. Uma com os valores pares da lista inicial. (0 podemos considerar par)
#b. Uma com os valores ímpares da lista inicial.

lista = []

for i in range(1, 16):
    lista.append(int(input(f"Informe um valor {i}: ")))

#LETRA A
def listaPares(lista):
    listaPares = []
    for m in range(len(lista)):
        if lista[m] % 2 == 0:
            listaPares.append(lista[m])
    return listaPares

#LETRA B

def listaImpares(lista):
    listaImpares = []
    for o in range(len(lista)):
        if lista[o] % 2 != 0:
            listaImpares.append(lista[o])
    return listaImpares


print(f"Lista inicial: ", lista)
print(f"Lista pares: ", listaPares(lista))
print(f"Lista impares: ", listaImpares(lista))