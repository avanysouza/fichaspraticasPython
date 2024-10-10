# Implemente uma função somatorio( ) que recebe um número inteiro como parâmetro e retorna o somatório de
# todos os seus dígitos

num = input("Digite um numero: ")

def somatorio(num):
    soma = 0
    for i in range (int(len(num))):
        soma += int(num[i])
    return soma

total = somatorio(num)

print(total)

