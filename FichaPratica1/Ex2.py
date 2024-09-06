# Escreva um programa que requisite dois valores. O programa deverá utilizá-los como operandos para
# as seguintes operações aritméticas: soma, subtração, multiplicação e divisão. Apresente o resultado
# das operações e teste os resultados obtidos com vários casos

num1 = eval(input('Informe um numero: '))
num2 = eval(input('Informe um numero: '))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

print(f"Soma: {soma}")
print(f"Subtracao: {subtracao}")
print(f"Multiplicacao: {multiplicacao}")
print(f"Divisao: {divisao}")
