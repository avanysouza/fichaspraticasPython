# Crie um programa com um dicionário chamado tradutor onde as chaves são as palavras em inglês e os valores
# são as suas traduções.
# tradutor = {
#  "dog": "cachorro",
#  "cat": "gato",
#  "house": "casa",
#  "car": "carro"
# }

tradutor = {
    "development": "desenvolvimento",
    "storage": "armazenamento",
    "technology": "tecnologia",
    "code": "codigo"
}

consulta = input("Informe a palavra que deseja consultar a tradução: ")

print(f"Tradução da palavra {consulta}: {tradutor[consulta]}")