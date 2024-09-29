# Escreva um programa que lê uma lista de tamanho 10 e verifica se os elementos estão em ordem crescente.

numeros = [15,20,30,54,1,5,500,16,18,48]
def verificarOrdem(numeros):
    for i in range(len(numeros) - 1):
        if numeros[i] > numeros[i + 1]: #compara o numero atual com o proximo, por isso o +1
            return False
    return True

# Verificando se a lista está em ordem crescente
if verificarOrdem(numeros):
    resultado = "A lista está em ordem crescente."
else:
    resultado = "A lista não está em ordem crescente."

print(numeros)
print(resultado)