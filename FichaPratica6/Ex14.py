#Escreva um programa que permita preencher uma lista de tamanho 10, seguidamente ordene a mesma por
#ordem crescente. (Sem usar funções se sort)

lista = []

for i in range(1, 11):
    lista.append(int(input(f"Informe um valor {i}: ")))
