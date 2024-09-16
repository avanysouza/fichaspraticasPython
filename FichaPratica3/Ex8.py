# Faça um programa que vai pedindo números ao utilizador até que este introduza o número -1. O computador
# deve dizer a média dos números introduzidos (excluindo o -1)

numero = 0
soma = 1
count = -1

while(numero != -1):
    numero = int(input("Digite um numero: "))
    soma += numero
    count +=1

media = soma / count

print(f"Média: {media}")