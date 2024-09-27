# Implemente um programa de Cálculo do Preço de Terrenos (m/2) e análise imobiliária. Inicialmente deve ter um
# menu que pergunta qual a forma do nosso terreno, deve ter, no mínimo, as seguintes formas (pode implementar
# mais): quadrado, retângulo, triangular, circular


opcao =

forma= input(("Informe a forma do terreno: 1-Quadrado\n 2-Retangulo\n 3-Triangular\n 4-Circular\n"))
match forma:
    case 1:
        tamanho = input("Informe o tamanho do terreno: ")
    case 2:
        comprimento = input("Informe o comprimento do terreno: ")
        largura = input("Informe a largura do terreno: ")
    case 3:
        raio = input("Informe o raio do terreno: ")

