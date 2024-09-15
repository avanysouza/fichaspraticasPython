#Faça um programa que leia dois números inteiros, representando os valores início e fim de um intervalo e
#imprima os números inteiros neste intervalo.

vInicio = int(input("Informe um numero inicial: "))
vFinal = int(input("Informe um numero final: "))
inicio = vInicio

print(vInicio)
while inicio >= vInicio and inicio < vFinal:
    inicio += 1
    print(inicio)
