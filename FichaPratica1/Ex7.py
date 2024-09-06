# Escreva um programa que requisite ao utilizador o preço de 3 produtos adquiridos. Apresente o valor
# a pagar, considerando que deverá ter um desconto de 10% sobre o total dos produtos.

valor1 = eval(input("Digite o valor do produto 1: "))
valor2 = eval(input("Digite o valor do produto 2: "))
valor3 = eval(input("Digite o valor do produto 3: "))

total = valor1 + valor2 + valor3
print(f"Valor a pagar: {total - (total * 0.1)}")
