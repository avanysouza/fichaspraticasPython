

listaContactos=[]

contacto={
    "nome":"Avany Souza",
    "telemovel": "965618151",
    "morada": "Braga"
}

listaContactos.append(contacto)

def pesquisarContato(consulta):
    for contacto in listaContactos:
        if contacto["nome"].upper() == consulta.upper():
            print(f'O contacto "{contacto["nome"]}" está presente na lista de contatos.')
            print(f'Telemóvel: {contacto["telemovel"]}, Morada: {contacto["morada"]}')
        else:
            print("Esse contacto nao existe na lista")

opcao=0

while(opcao!=4):
    print("**** Lista de Contactos ****")
    print("1.Adicionar novo contato")
    print("2.Consultar lista de contatos")
    print("3.Pesquisar um Contacto")
    print("4.Sair")
    opcao=int(input("Insira a opcao desejada: "))

    match(opcao):
        case 1:
            print("\nAdicionar novo contato")
            nome=input("Nome: ")
            telemovel=input("Telemovel: ")
            morada = input("Morada: ")

            novoContacto = {
                "nome": nome,
                "telemovel": telemovel,
                "morada": morada
            }

            listaContactos.append(novoContacto)

        case 2:
            print("\nConsultar lista de contatos")
            for contacto in listaContactos:
                print(contacto)
        case 3:
            print("\nPesquisar um Contacto")
            consulta=input("Digite o nome que deseja consultar: ")

            print(pesquisarContato(consulta))


        case 4: print("\nSair")
        case _: print("\nOpção invalida")
