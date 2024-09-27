# O exercício deve ser resolvido no mesmo ficheiro (por exemplo: Ex_03), deve acrescentar as funções conforme
# solicitado. No início não conseguirá testar se as funções funcionam ou não (uma vez que não é pedido para
# desenvolver nada de forma a executar), considere fazer o exercício 4 em concorrente para conseguir perceber se
# está tudo como esperado.
# a) Implemente uma função que determina se um número (passado por argumento) é par ou ímpar, a função
# deve retornar true se par ou false se ímpar
# b) Implemente uma função que determina se um número (passado por argumento) é positivo ou negativo, a
# função deve retornar true se zero ou positivo, ou false se negativo.
# c) Implemente uma função que determina se um número (passado por argumento) é ou não primo, a função
# deve retornar true se primo ou false se não primo.
# d) Implemente uma função que determina se um número (passado por argumento) é perfeito, a função deve
# retornar true se perfeito ou false se não perfeito (Os números perfeitos são iguais à soma dos seus divisores:
# 6 pode ser dividido por 1, 2 e 3 e, quando soma esses números, o resultado é 6).
# e) Implemente uma função que determina se um número (passado por argumento) é triangular, a função deve
# retornar true se triangular ou false se não triangular (Um número triangular é um número que pode ser
# representado pela soma de números inteiros consecutivos. Exemplo: 6 = 1+2+3 ou 15=1+2+3+4+5).


#ALINEA A
def par(num):
    if(num%2==0):
        return True
    else:
        return False
#ALINEA B
def numeroPositivo(num):
    if(num>=0):
        return True
    else:
        return False

#ALINEA C
def primo(num):
    primo = True

    for i in range(2, num):
        if(num%i==0):
            primo = False

    if primo:
        return True
    else:
        return False

#ALINEA D

