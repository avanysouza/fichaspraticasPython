# Implemente um programa que peça ao utilizador dois valores e um carácter representando uma das quatro
# operações aritméticas (+, -, *, /). Apresente o resultado de aplicar a operação correspondente aos valores. No
# final, deverá perguntar ao utilizador se deseja repetir, permitindo-lhe efetuar novos cálculos.
# Exemplo: Deseja continuar? (introduza s/n)

def calculadora(num1, num2, operacao):
    match operacao:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        case _:
            return "Operação inválida!"


def main():
    while True:
        num1 = float(input("Introduza o primeiro valor: "))
        num2 = float(input("Introduza o segundo valor: "))

        operacao = input("Introduza a operação (+, -, *, /): ")

        resultado = calculadora(num1, num2, operacao)
        print(f"Resultado: {resultado}")

        opcao = input("Deseja continuar? (introduza s/n): ")
        if opcao != 's':
            print("Encerrando o programa.")
            break

main()
