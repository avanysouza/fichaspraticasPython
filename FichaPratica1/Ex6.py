# Escreva um programa que leia dois valores inteiros e os armazene na variáveis valor1 e valor2. Permute
# o valor das variáveis e apresente o resultado. De seguida, verifique se consegue efetuar esta troca sem
# criar variáveis adicionais

valor1 = int(input('Digite o valor 1: '))
valor2 = int(input('Digite o valor 2: '))

valor2 = valor1
valor1 = valor2

print(f"Valor 1 = {valor1}")
print(f"Valor 2 = {valor2}")