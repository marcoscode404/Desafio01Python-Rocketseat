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

def editar_contato(contatos, indice_contato, novo_nome_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["nome"] = novo_nome_contato
        print(f"Contato {indice_contato} atualizado para {novo_nome_contato}")
    else:
        print("Indice do contato inválido")
    return

def favoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    contato = contatos[indice_contato_ajustado]
    contato["favorito"] = not contato.get("favorito", False)
    print(f"Contato {indice_contato} marcado como favorito")
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

    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("Digite o número o numero do contato que deseja atualizar: ")
        novo_nome = input("Digite o novo nome do contato: ")
        editar_contato(contatos, indice_contato, novo_nome)

    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja favoritar: ")
        favoritar_contato(contatos, indice_contato)

    elif escolha == "7":
        break
    print('Programa finalizado')
    