# Crie um programa que armazene uma lista de compras, sendo assim a chave será o nome do produto e tenha
# como valor o preço total. Seguidamente permita ao utilizador inserir novos produtos ou calcular o preço total.

#Lista de Compras

lista = {
    "Maca": 5,
    "Banana": 3,
    "Feijao": 4,
    "Cenoura": 1
}

#Função para calcular preço total da lista
def calcularPreco(lista):
    total = 0
    for _ in lista:
        total += lista[_]
    return total

#Função para adicionar produto na lista
def adicionarProduto(lista):
    item = input("Digite o item que deseja adicionar: ")
    preco = int(input("Digite o valor do item: "))
    lista[item] = preco

    return lista

opcao = 0

while(opcao != 4):
    print("\n**** Carrinho de Compras ****\n")
    print("1 - Adicionar produto na lista de compras: ")
    print("2 - Consultar lista de compras: ")
    print("3 - Calcular valor total da lista de compras: ")
    print("4 - Sair")
    opcao = int(input("\nDigite a opção desejada: "))
    match opcao:
        case 1:
            adicionarProduto(lista)
        case 2:
            print(lista)
        case 3:
            calcularPreco(lista)
            print(f"Valor total: {calcularPreco(lista)}")
        case 4:
            print("Bye Bye")
        case _:
            print("Opção invalida")