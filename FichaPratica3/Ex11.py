# Escreva um algoritmo que leia uma quantidade desconhecida de números inteiros positivos fornecidos pelo
# utilizador e conte quantos deles estão nos seguintes intervalos: [0.25], [26,50], [51,75] e [76,100]. A entrada de
# dados deve terminar quando for lido um número negativo.

numero = 0
intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0

while numero >=0:
    numero = int(input("Introduza um numero: "))
    if numero >= 0 and numero <= 25:
        intervalo1 += 1
    elif numero >= 26 and numero <= 50:
        intervalo2 += 1
    elif numero >= 51 and numero <= 75:
        intervalo3 += 1
    elif numero >= 76 and numero <= 100:
        intervalo4 += 1

print("--------")
print(f"[00,25]: {intervalo1}")
print(f"[26,50]: {intervalo2}")
print(f"[51,75]: {intervalo3}")
print(f"[76,100]: {intervalo4}")