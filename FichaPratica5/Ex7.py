# Implemente o programa “Análise de um Número” que pergunte um número ao utilizador e, de seguida, apresente
# um menu de opções ao utilizador, que permitem analisar o número inserido. Esse menu de opções deve ter o
# seguinte aspeto:
# 1. Par ou Ímpar
# 2. Positivo ou Negativo
# 3. Primo ou Não Primo
# 4. Perfeito ou Não Perfeito
# 5. Triangular ou Não Triangular
# 6. Trocar de Número

num = input("Informe um número:")
opcao = input("Escolha uma opção: ")
opcao = 7

while opcao != 7:
    print("Análise de um Número")
    print("1. Par ou Ímpar")
    print("2. Positivo ou Negativo")
    print("3. Primo ou Não Primo")
    print("4. Perfeito ou Não Perfeito")
    print("5. Triangular ou Não Triangular")
    print("6. Trocar de Número")

match opcao:
    case 1:

    case 2:

    case 3:

    case 4:

    case 5:

    case 6:

def par(num):
    if num % 2 == 0:
        return True
    else:
        return False

def positivo(num):
    if num >=0:
        return True
    else:
        return False

def primo(num):
    primo = True

    for i in range(2, num):
        if(num%i==0):
            primo = False

    if primo:
        return True
    else:
        return False

def perfeito(num):
    perfeito = True
    for i in range(2, num):


#Implantar resolucao para a função
def triangular(num):


# Implantar resolucao para a função
def trocaNumero(num):
