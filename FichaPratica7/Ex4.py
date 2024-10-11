# Crie um programa que tenha um dicionário que, dado uma lista, conte quantas vezes essa palavra está repetida
# na lista. Por exemplo:
# palavras = ["maçã", "banana", "laranja", "maçã", "laranja", "laranja"].
# “maçã” : 2
# “banana” : 1
# “laranja” : 3
# No final imprima o dicionário com a contagem de cada palavra

palavras = ["maçã", "banana", "laranja", "maçã", "laranja", "laranja"]
contagem = {}
def contadorPalavras(palavras):
    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem

print(f"Contagem das palavras presentes na lista: \n{contadorPalavras(palavras)}")

#print("\n".join(contadorPalavras(palavras)))