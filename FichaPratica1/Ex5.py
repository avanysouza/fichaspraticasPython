# Escreva um programa que determine a média aritmética de um conjunto de 3 valores introduzidos pelo
# utilizador. Tendo em consideração os valores introduzidos, deverá também apresentar a média
# ponderada considerando as seguintes ponderações: 20%, 30%, 50%

num1 = eval(input("Insira um valor:"))
num2 = eval(input("Insira um valor:"))
num3 = eval(input("Insira um valor:"))

#Calculo da média

media = (num1 + num2 + num3)/3
mediaPonderada = (num1 * 0.2) + (num2 * 0.3) + (num3 * 0.5)

print(f"Media: {media}")
print(f"Media Ponderada: {mediaPonderada}")
