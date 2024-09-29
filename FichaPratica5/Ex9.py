# Implemente uma função somatorio( ) que recebe um número inteiro como parâmetro e retorna o somatório de
# todos os seus dígitos


def somatorio(num):
    for i in range(1,num):
        soma = num + i
        print(soma)


print(somatorio(22))