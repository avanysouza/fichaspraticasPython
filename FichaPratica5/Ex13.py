# Implemente um programa de Cálculo do Preço de Terrenos (m/2) e análise imobiliária. Inicialmente deve ter um
# menu que pergunta qual a forma do nosso terreno, deve ter, no mínimo, as seguintes formas (pode implementar
# mais): quadrado, retângulo, triangular, circular
import math

print("Cálculo do Preço de Terrenos (m/2)")
print("-----------")
forma= int(input("Digite a opção correspondente a forma do terreno:\n 1-Quadrado\n 2-Retangulo\n 3-Triangular\n 4-Circular\n "))

valor = 0

match forma:
    case 1:
        lado = input("Informe o tamanho de um dos lados do terreno: ")
        preco = float(input("Informe o preço do terreno:"))
        tipologia = input("Informe o tipologia do terreno: ")
    case 2:
        comprimento = print(input("Informe o comprimento do terreno: "))
        largura = input("Informe a largura do terreno: ")
        preco = float(input("Informe o preço do terreno:"))
        tipologia = input("Informe o tipologia do terreno: ")
    case 3:
        base = input("Informe o tamanho da base do terreno: ")
        altura = float(input("Informe a altura do terreno:"))
        preco = float(input("Informe o preço do terreno:"))
        tipologia = input("Informe o tipologia do terreno: ")
    case 4:
        raio = input("Informe o raio do terreno: ")
        preco = float(input("Informe o preço do terreno:"))
        tipologia = input("Informe o tipologia do terreno: ")
    case _:
        print("Opcao invalida")

def areaQuadrado(lado):
    area = lado**2
    return area

def areaRetangulo(largura, comprimento):
    area = largura * comprimento
    return area

def areaTriangular(base, altura):
    area = base * altura / 2
    return area

def areaCircular(raio):
    pi = math.pi
    area = pi * raio**2
    return area

def calcularMetro(area, preco):
    valor = preco / area
    return valor

if tipologia == "Urbano":
    if valor >=450 and valor <=750:
        print("Preço dentro do valor do mercado")
    elif valor >=150 and valor <=500:
        print("Preço está fora do valor do mercado")

