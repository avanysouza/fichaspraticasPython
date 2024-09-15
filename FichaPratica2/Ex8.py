#Escreva um programa que leia três notas (0-20 valores) de um aluno, calcule a sua média final ponderada, e diga
#se está aprovado ou não (mais de 9.5). Ponderações: Nota 1: 25%; Nota 2: 35%; Nota 3:40%

nota1 = eval(input('Informe a nota 1: '))
nota2 = eval(input('Informe a nota 2: '))
nota3 = eval(input('Informe a nota 3: '))

media = (nota1 * 0.25) + (nota2 * 0.35) + (nota3 * 0.40)

if(media >= 9.5):
    print(f"Média:{media}! Você foi aprovado!")
else:
    print(f"Média:{media}! Voce foi reprovado!")