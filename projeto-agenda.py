def adicionar_contato(contatos, nome_contato, numero_contato, email):
    contato = {"nome": nome_contato, "telefone": numero_contato , "email": email, "favorito": False}
    contatos.append(contato)
    print(f"O Contato {nome_contato} foi adicionado com sucesso!")
    return

def ver_contatos(contatos):
    print(f"\n Lista de contatos: {contatos}")
    for indice, contato in enumerate(contatos, start=1):
        status = "⭐" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        numero_contato = contato["telefone"]
        email = contato["email"]
        print(f"{indice}, [{status}] {nome_contato}, {numero_contato}, {email}")
    return

contatos = []
while True:
    print("\n Menu do gerenciador de lista de tarefas")
    print("1. Adicionar novo contato")
    print("2. Ver contatos")
    print("3. Editar contatos")
    print("4. Marcar como favorito")
    print("5. Ver Favoritos")
    print("6. Apagar contato")

    escolha = input("Digite a sua escolha: ")


    if escolha == "1":
        nome_contato = input("Digite o nome do contato que deseja adicionar: ")
        numero_contato = input("Digite o numero do contato que deseja adicionar: ")
        email = input("Digite o email do contato que deseja adicionar: ")
        adicionar_contato(contatos, nome_contato, numero_contato, email)

    elif escolha == "2":
        ver_contatos(contatos)

    elif escolha == "7":
        break
    print('Programa finalizado')
    