#Implemente um programa que, após pedir ao utilizador o saldo da conta bancária e montante a creditar/debitar
#(montante positivo ou negativo, respetivamente), apresente se a operação é válida, ou seja, se o saldo final se
#mantém positivo depois da operação.

saldo = eval(input("Digite o valor do saldo atual: "))
credito = eval(input("Digite o valor que deseja creditar: "))
debito = eval(input("Digite o valor que deseja creditar: "))
saldoFinal = 0


if debito > saldo:
    print("Operacao invalida! Saldo insuficiente!")
else:
    saldoFinal = saldo - debito
    print(f"Saldo final positivo. Saldo final: {saldoFinal}")

