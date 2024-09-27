# Implemente um programa que permita adicionar comissões mensais a uma lista de tamanho 12 (uma posição
# para cada mês) e calcular o seu total anual.

comissoes = []

#Ciclo for para solicitar as 12 comissoes mensais
for i in range(1, 13):
    comissoes.append(input(f"Informe a comissão do mês {i}: "))

print(comissoes)