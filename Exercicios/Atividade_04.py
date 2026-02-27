print("Lista telefonica")

contatos = {}

while True:
    print("1 - Cadastrar contatos")
    print("2 - Buscar contatos")
    print("3 - Excluir contato")
    print("4 - Exibir contatos salvos")
    print("5 - Sair")

    opcao = int(input("Digite a opção desejada: "))
    print()
    
    if opcao == 1:
        nome = input("Digite seu nome: ")
        telefone = int(input("Digite seu telefone: "))
        contatos[nome] = telefone
        print(f"Contato {nome} cadastrado com sucesso.")
        print()

    elif opcao == 2:
        nome_busca = input("Nome do contato que deseja buscar: ")
        if nome_busca in contatos:
            print(f"Telefone de {nome_busca}: {contatos[nome_busca]}")
        else:
            print("Contato não encontrado.")
        print()

        
    elif opcao == 3:
        excluirCTT = input("Contato que deseja excluir: ")
        if excluirCTT in contatos:
            del contatos[excluirCTT]
            print(f" {excluirCTT} excluído com sucesso.")
        else:
            print("Contato não encontrado.")
        print()

        
    elif opcao == 4:
        if contatos:
            print("Contatos cadastrados")
            for nome, telefone in contatos.items():
                print(f"Nome: {nome}, Telefone: {telefone}")
    elif opcao == 5:
        print("Saindo do programa")
        break
        print()


        

