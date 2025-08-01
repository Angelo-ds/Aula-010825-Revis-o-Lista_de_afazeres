#Lista de afazeres para revisão de python pós férias
print("Bem vindo a sua Lista de Afazeres!")
lista_afazeres = []
while True:
    afazer = input("""Você deseja o que da lista?:
    ---------------------
    | -adicionar        |
    | -retirar          |
    | -mostrar          |
    | -sair             |
    ---------------------
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
        if lista_afazeres:
            print("Lista de Afazeres:")
            for tarefa in lista_afazeres:
                print(f"- {tarefa}")
        else:
            print("Sua lista de afazeres está vazia.")
    elif afazer.lower() == "sair":
        print("Saindo da sua lista de afazeres. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção das opções descritas.")
