#Lista de afazeres para revisão de python pós férias
print("Bem vindo a sua Lista de Afazeres!")
lista_afazeres = []
Tarefas_concluidas = []
while True:
    afazer = input("""Você deseja o que da lista?:
    ----------------------------
    | -adicionar               |
    | -retirar                 |
    | -mostrar                 |
    | -marcar como concluido   |
    | -sair                    |
    ----------------------------
    """)
    if afazer.lower() == "adicionar":
        
        tarefa = input("Digite a tarefa que deseja adicionar: ")
        lista_afazeres.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada com sucesso!")

    elif afazer.lower() == "retirar":

        tarefa = input("Digite a tarefa que deseja retirar: ")
        if tarefa in lista_afazeres:
            lista_afazeres.remove(tarefa)
            print(f"Tarefa '{tarefa}' retirada com sucesso!")

        else:
            print(f"Tarefa '{tarefa}' não encontrada na lista.")

    elif afazer.lower() == "mostrar":
        mostrar = input("Qual lista deseja Ver? (afazeres/concluidas): ")

        if mostrar.lower() == "afazeres":
            if lista_afazeres:
                if len(lista_afazeres) == 0:
                    print("Sua lista de afazeres está vazia.")
                else:
                    print("Tarefas Pendentes:")
                    for tarefa in lista_afazeres:
                        print(f"[ ] {tarefa}")

        elif mostrar.lower() == "concluidas":
            if Tarefas_concluidas:
                print("Tarefas Concluídas:")
                for tarefa in Tarefas_concluidas:
                    print(f"[X] {tarefa}")
        else:
            print("Você não tem tarefas concluídas.")

    elif afazer.lower() == "marcar como concluido":
        tarefa = input("Digite a tarefa que deseja marcar como concluída: ")
        if tarefa in lista_afazeres:
            lista_afazeres.remove(tarefa)
            Tarefas_concluidas.append(tarefa)
            print(f"[X] {tarefa} - Concluída")
        else:
            print("Sua lista de afazeres está vazia.")

    elif afazer.lower() == "sair":
        print("Saindo da sua lista de afazeres. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção das opções descritas.")
