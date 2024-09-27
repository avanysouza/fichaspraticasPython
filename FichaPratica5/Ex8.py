# Escreva um programa para desenhar um quadrado no ecrã. Esse quadrado deverá ser desenhado por uma função
# para a qual são passados três argumentos: caracter a utilizar, número de linhas e número de colunas. Segue-se
# um exemplo do algoritmo a ser executado, ilustrando o pretendido

def desenhar(caracter,linhas,colunas):
    for i in range(colunas,linhas):
        print(caracter*i)
    for k in range(linhas):
        print(caracter*k)


print(desenhar("z", 4, 3))