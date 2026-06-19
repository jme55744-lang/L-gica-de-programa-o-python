fila = []
historico = []
while True:
    print("/n =====MENU=====")
    print("1 - adicionar cliente")
    print("2 - atender cliente")
    print("3 - mostrar fila")
    print("4 - mostrar histórico")
    print("5 - buscar cliente")
    print("6 - sair")
    opcao = input("Escolha uma opção:")

    if opcao == "1":
        nome = input("Nome do cliente:")
        idade = input("Idade do cliente")
        cliente = {"nome": nome, "idade": idade}
        fila.append(cliente)
        print("Cliente adicionado a fila")
    elif opcao == "2":
        if len(fila)== 0:
            print("A fila esta vazia")
        else:
            atendido = fila.pop(0)
            print("Cliente atendido")
            print("nome:", atendido["nome"])
            print("idade:", atendido["idade"])
            historico.append(atendido)
    elif opcao == "3":
        if len(fila)==0:
            print("a fila esta vazia")
        else:
            print("/n cliente na fila")
            for cliente in fila:
                print(cliente["nome"], "-", cliente[idade], "anos")
    elif opcao == "4":
        if len(fila)==0:
            print("nenhum atendimento realizado")
        else:
            print("/n cliente na fila")
            for cliente in fila:
                print(cliente["nome"], "-", cliente[idade], "anos")
    elif opcao == "5":
        if len(fila)==0 and len(historico)==0:
            print("não há clientes cadastrados")
        else:
            nome_busca = input("digite o nome do cliente: ")
            encontrado = False
            for cliente in fila:
                if cliente ["nome"].lower()==nome_busca.lower():
                    print("cliente esta na fila")
                    print("nome:", cliente, ["nome"])
                    print("idade:", cliente, ["idade"])
                    encontrado = True
            for cliente in historico:
                if cliente ["nome"].lower()==nome_busca.lower():
                    print("cliente esta na fila")
                    print("nome:", cliente, ["nome"])
                    print("idade:", cliente, ["idade"])
                    encontrado = True
                if not encontrado:
                    print("cliente não encontrado")
    elif opcao == "6":
        print("programa encerrado")
    else:
        print("opção inválida")