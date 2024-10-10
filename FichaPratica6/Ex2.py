# Implemente um programa que permita adicionar comissões mensais a uma lista de tamanho 12 (uma posição
# para cada mês) e calcular o seu total anual.

comissoes = []
total = 0

#Ciclo for para solicitar as 12 comissoes mensais
for i in range(0, 12):
    comissoes.append(float(input(f"Informe a comissão do mês {i}: ")))

for i in range(0, 12):
    total += comissoes[i]

print(comissoes)
print(total)