#Na fórmula 1, os pontos no final de cada corrida são atribuidos da seguinte forma:
#a. 1º Lugar: 10 pontos
#b. 2º Lugar: 8 pontos
#c. 3º Lugar: 6 pontos
#d. 4º Lugar: 5 pontos
#e. 5º Lugar: 4 pontos
#f. 6º Lugar: 3 pontos
#g. 7º Lugar: 2 pontos
#h. 8º Lugar: 1 ponto
#Escreva um programa que leia o lugar em que o piloto terminou e escreva quantos pontos ganhou.

posicao = int(input("Introduza o seu lugar na corrida: "))
pontuacao = 0

match posicao:
    case 1:
        pontuacao = 10
    case 2:
        pontuacao = 8
    case 3:
        pontuacao = 6
    case 4:
        pontuacao = 5
    case 5:
        pontuacao = 4
    case 6:
        pontuacao = 3
    case 7:
        pontuacao = 2
    case 8:
        pontuacao = 1
    case _:
        print("Não ganhou pontos!")


print(f"Ganhou {pontuacao} pontos")