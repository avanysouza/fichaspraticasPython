#Um banco autoriza a conceção de um crédito especial aos seus clientes, num montante variável com base no seu
#saldo médio do último ano. Faça um programa que leia o saldo médio de um cliente e calcule o valor do crédito
#especial de acordo com a seguinte tabela. Mostre uma mensagem com o saldo médio e o valor de crédito.

saldoMedio = eval(input("Digite o valor do saldo medio: "))
credito = 0

if(saldoMedio >0 and saldoMedio<= 2000):
    credito = 0
elif(saldoMedio >2000 and saldoMedio<= 4000):
    credito = saldoMedio * 0.20
elif(saldoMedio >4000 and saldoMedio<= 6000):
    credito = saldoMedio * 0.30
else:
    credito = saldoMedio * 0.40

print(f"Saldo médio: {saldoMedio:.2f}, Valor de crédito: {credito:.2f}")