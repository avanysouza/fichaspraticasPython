#Escreva um programa que permita preencher uma lista de tamanho 10, seguidamente ordene a mesma por
#ordem crescente. (Sem usar funções se sort)

lista = []



for i in range(1, 11):
    lista.append(int(input(f"Informe um valor {i}: ")))

def ordemCrescente(lista):
    for i in range(len(lista)):
        #Comparar a posicao atual com a proxima e se for menor
        for n in range(len(lista) - 1):
            if lista[n] > lista[n + 1]:
                lista[n], lista[n + 1] = lista[n + 1], lista[n]

    return lista


print(lista)
print(ordemCrescente(lista))



