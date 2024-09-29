#Escreva um programa que permita preencher duas listas de tamanho 8. Seguidamente, crie uma nova lista
#contendo apenas os valores que estão presentes em ambas as listas iniciais

lista_um = []
lista_dois = []

#Preencher primeira lista
for i in range(1,9):
    lista_um.append(int(input(f"Lista 1 - Informe um valor {i}: ")))

#Preencher segunda lista
for m in range(1,9):
    lista_dois.append(int(input(f"Lista 2 - Informe um valor {m}: ")))

def listaNumerosIguais(lista_um, lista_dois):
    lista_iguais = []
    for n in range(len(lista_um)):
        if lista_um[n] in lista_dois:
            lista_iguais.append(lista_um[n])
    return lista_iguais

print("Lista com valores presentes nas duas listas: ",listaNumerosIguais(lista_um, lista_dois))