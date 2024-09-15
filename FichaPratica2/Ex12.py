#Implemente um programa de menu (opções do menu: 1. Criar 2. Atualizar 3. Eliminar 4. Sair). Se uma das opções
#1, 2 ou 3 for escolhida, imprima na tela a opção selecionada, se for a 4 não deve fazer nada. Caso a opção for
#inválida, deve informar o utilizador.


print("--- Menu ---")
print(" 1. Criar")
print(" 2. Atualizar")
print(" 3. Eliminar")
print(" Sair")
print("------")
opcao = int(input("Digite o número da opção desejada: "))

match opcao:
    case 1:
        print("Opção selecionada: 1 - Criar")
    case 2:
        print("Opção selecionada: 2 - Atualizar")
    case 3:
        print("Opção selecionada: 1 - Eliminar")
    case 4:
        print("")
    case _:
        print("Opção invalida!")