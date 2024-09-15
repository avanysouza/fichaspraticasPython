#Determine e escreva o montante de impostos a pagar sobre um salário anual lido, tendo em conta o seguinte:
#a. Salário até 15.000€ inclusive paga taxa de 20%
#b. Salário superior a 15.000€ paga taxa de 30%

salario = eval(input("Informe o salario anual: "))

if(salario <= 15000):
    print(f"Paga taxa de 20%: {salario*0.20:.2f}")
else:
    print(f"Paga taxa de 30%: {salario*0.30:.2f}")

