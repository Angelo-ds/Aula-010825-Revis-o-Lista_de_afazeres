#Lista de afazeres para revisão de python pós férias
print("Bem vindo a sua Lista de Afazeres!")
while True:
    lista_afazeres = []
    afazer = input("Você deseja adicionar, retirar algo da lista, ou mostrar o que tem na lista?:  ")
    if afazer.lower() == "adicionar":
        tarefa = input("Digite a tarefa que deseja adicionar: ")
        lista_afazeres.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada com sucesso!")
    elif afazer.lower() == "retirar":
        tarefa = input("Digite a tarefa que deseja retirar: ")
    print(f"Tarefa '{tarefa}' retirada com sucesso!")
    else:
        print("Opção inválida. Por favor, digite 'adicionar' ou 'retirar'.")