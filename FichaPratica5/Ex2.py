# Implemente uma função numeroMaisPequeno( ) que recebe três números inteiros como parâmetro e retorna o
# mais pequeno dos três.


def numeroMaisPequeno(num1, num2, num3):
    menor = num1

    if num1 < num2 and num1 < num3:
        menor = num1
    if num2 < num1 and num2 < num3:
        menor = num2
    if num3 < num1 and num3 < num2:
        menor = num3

    return menor

# 1 10 58 9 50 5 77 2 8
##Invocando a função dentro da função
menor= numeroMaisPequeno(numeroMaisPequeno(1,10,58),numeroMaisPequeno(9,50,5),numeroMaisPequeno(77,2,8))
print(menor)
