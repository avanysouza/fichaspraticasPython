#Escreva um programa que leia dois números reais e pergunte ao utilizador qual a operação aritmética que quer
#realizar e apresente o resultado. O utilizador deve responder usando o símbolo da operação (exemplo: para fazer
#a soma, o utilizador deve escrever ‘+’). Se for inválido apresente erro.

num1 = float(input('Digite um valor: '))
num2 = float(input('Digite um valor: '))
operacao = input('Digite o operador: ')

match operacao:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)
    case _:
        print("Operação inválida! Digite um símbolo da operação desejada.")
