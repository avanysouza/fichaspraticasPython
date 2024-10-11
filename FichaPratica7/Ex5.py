# Crie um programa que tenha um dicionário onde cada chave é associada a uma lista de valores. Sendo assim,
# teremos o dicionário formandos que contenha os seguintes dados:
# "João" tem as notas [8, 7, 9]
# "Maria" tem as notas [16, 19, 18]
# "Ana" tem as notas [19, 18, 20]
# O programa deve permitir pesquisar por nome e apresenta a média do formando

#Dicionario com listas de valores
alunos = {
    "Joao": [8,7,9],
    "Maria": [16,19,18],
    "Ana": [19,18,20]
}

#Função para obter as notas de cada aluno conforme pesquisa
def obterNotas(pesquisa):
    if pesquisa in alunos:
        return alunos[pesquisa]
    else:
        return "Aluno não localizado!"

#Função para realizar o cálculo das notas do aluno:
def mediaAluno(notas):
    media = 0
    quantidade = len(notas)
    media = sum(notas) / quantidade
    return media


#Solicitar ao utilizador o nome para pesquisa:
pesquisa = input("Informe o nome do aluno: ")

#Atribuir notas conforme função para obter as notas por aluno pesquisado
notas = obterNotas(pesquisa)


print(f"O aluno {pesquisa} teve média igual a: {mediaAluno(notas)}")