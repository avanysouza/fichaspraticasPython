#Determine e escreva o montante de impostos a pagar sobre um salário anual lido, tendo em conta o seguinte:
#a. Salário até 15.000€ inclusive paga taxa de 20%
#b. Salário de 15.000€ a 20.000€ inclusive paga taxa de 30%
#c. Salário de 20.000€ a 25.000€ inclusive paga taxa de 35%
#d. Salário superior a 25.000€ paga taxa de 40%

salario = eval(input("Informe o salario anual: "))

if(salario <= 15000):
    print(f"Paga taxa de 20%: {salario*0.20:.2f}")
elif(salario > 15000 and salario <= 20000):
    print(f"Paga taxa de 30%: {salario*0.30:.2f}")
elif(salario > 2000 and salario <= 25000):
    print(f"Paga taxa de 30%: {salario*0.35:.2f}")
else:
    print(f"Paga taxa de 40%: {salario*0.40:.2f}")