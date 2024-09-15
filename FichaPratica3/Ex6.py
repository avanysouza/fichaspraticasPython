#Faça um programa que imprima os números inteiros de 1 a 100 inclusive, e no final imprima também o valor do
#seu somatório. (Não necessita de input do utilizador)

numero = 0
soma = 0

while numero >= 0 and numero <= 99:
    numero += 1
    soma+=numero
    print(numero)

print("-----")
print(f"Somatorio: {soma}")