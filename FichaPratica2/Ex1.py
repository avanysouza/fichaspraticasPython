#Leia dois números inteiros e escreva na consola o maior deles.

num1 = eval(input('Informe um numero: '))
num2 = eval(input('Informe um numero: '))

if(num1 > num2):
    print(f"Maior {num1}")
elif (num1 == num2):
        print(f"Os numeros sao iguais")
else:
    print(f"Maior: {num2}")


