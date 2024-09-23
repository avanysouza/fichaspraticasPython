#Escreva um programa que lê um valor em euros (múltiplo de 5) e calcula qual o menor número possível de notas
#de 200, 100, 50, 20, 10, 5 em que o valor pode ser decomposto. Escrever o valor lido e a relação de notas
#necessárias.

valor = int(input('Informe o valor: '))

#Notas de 200
notas = valor//200
print("Notas de 200: ", notas)

valor=valor%200


#Notas de 100
notas = valor//100
print("Notas de 100: ", notas)

valor=valor%100

#Notas de 50
notas = valor//50
print("Notas de 50: ", notas)

valor=valor%50

#Notas de 20
notas = valor//20
print("Notas de 20: ", notas)

valor=valor%20


#Notas de 10
notas = valor//10
print("Notas de 10: ", notas)

valor=valor%10

#Notas de 5
notas = valor//5
print("Notas de 5: ", notas)

valor=valor%5



