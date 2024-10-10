#Crie um programa com um dicionário simples de animais. Para cada letra do alfabeto, deve ter uma lista com
#animais cujo nome comece por essa letra (por exemplo: “A” : [“Andorinha”,”Avestruz”,”Alforreca”]).
#Seguidamente deve perguntar ao utilizador uma letra e imprime na consola todos os animais guardados.

dicAnimais = {
    "A": ["Arara","Anta", "Águia"],
    "B": ["Burro"],
    "C": ["Camelo","Cachorro"],
    "D": ["Dromedario","Dinossauro"]
}

consultaAnimais = input("Informe a letra do animal que deseja consultar: ")

print(dicAnimais[consultaAnimais])
