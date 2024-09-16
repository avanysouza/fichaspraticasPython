# Faça um programa que leia um número inteiro (variável limite), um incremento (variável salto) e imprima os
# números inteiros de 0 até limite inclusive, com incremento de salto. Suponha que limite e salto são maiores que
# zero.

limite = int(input("Introduza um limite: "))
salto = int(input("Introduza um salto: "))

for i in range (0, limite, 5):
        print(i)