# Crie um programa para a gestão de funcionários de uma empresa, o qual terá uma lista de dicionários de
# funcionários, sendo a chave o seu id. Terá também outras informações associadas como nome, anoNascimento,
# cargo e salário. O programa deve ter um menu que permitam:
# • Adicionar novos funcionários
# • Remover funcionários
# • Editar dados de um funcionário (pesquisa pelo ID), nomeadamente, cargo e salário.
# • Listar todos os funcionários da empresa com os seus respetivos dados.
# • Apresentar as informações de um funcionário através de pesquisa pelo ID.
# • Calcular quanto a empresa paga em salários, por mês, no total.
# • Cálculo de aumentos: Pergunta ao utilizador uma percentagem e, de seguida, calcula quanto a empresa
# passaria a pagar em salários por mês, no total, tendo em conta aquele aumento aplicado a todos os
# funcionários

funcionarios = []

#Funcao para adicionar funcionários na lista de dicionarios
def adicionarFuncionario(funcionarios):
    print("\nAdicionar novo funcionário:")
    id = int(input("Id: "))
    nome = input("Nome: ")
    anoNascimento = input("Ano: ")
    cargo = input("Cargo: ")
    salario = input("Salario: ")

    novoFuncionario = {
        "id": id,
        "nome": nome,
        "anoNascimento": anoNascimento,
        "cargo": cargo,
        "salario": salario
    }

    funcionarios.append(novoFuncionario)

#Função para remover funcionários
def removerFuncionario(funcionarios):
    funcionarios.pop()

#Editar dados de um funcionário (pesquisa pelo ID), nomeadamente, cargo e salário.
def editarFuncionario(funcionarios):
    pesquisa = int(input("Informe o id do funcionario: "))
    for i in range(len(funcionarios)):
        if(pesquisa==funcionarios[i]["id"]):
            #Alterar os dados do funcionario pesquisado:
            funcionarios[i]["cargo"] = input("Cargo: ")
            funcionarios[i]["salario"] = input("Salario: ")

    else:
        return "Funcionario não localizado!"


adicionarFuncionario(funcionarios)
print(funcionarios)
editarFuncionario(funcionarios)
print(funcionarios)