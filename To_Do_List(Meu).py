#Lista de afazeres para revisão de python pós férias
import funcao_para_salvar_a_lista_meu as salvar_lista
import time
print("Bem vindo a sua Lista de Afazeres!")
lista_afazeres = []
Tarefas_concluidas = []


while True:
    time.sleep(1)
    afazer = input("""Você deseja o que da lista?:
    ----------------------------
    | -adicionar               |
    | -retirar                 |
    | -mostrar                 |
    | -marcar como concluido   |
    | -sair                    |   
    ----------------------------
    """)
    time.sleep(1)
    if afazer.lower() == "adicionar":

        tarefa = input("Digite a tarefa que deseja adicionar: ")
        lista_afazeres.append(tarefa)

        #Essa linha de código é para o banco de dados.
        salvar_lista.tarefas_pendentes(tarefa) #esse chama a função que faz a mágica

        print(f"Tarefa '{tarefa}' adicionada com sucesso!")

    elif afazer.lower() == "retirar":

        tarefa = input("Digite a tarefa que deseja remover: ")
        if tarefa in lista_afazeres:
            lista_afazeres.remove(tarefa)
            print(f"Tarefa '{tarefa}' retirada com sucesso!")

        else:
            print(f"Tarefa '{tarefa}' não encontrada na lista.")

    elif afazer.lower() == "mostrar":
        mostrar = input("Qual lista deseja Ver? (afazeres/concluidas/todas): ")

        if mostrar.lower() == "afazeres":
                if len(lista_afazeres) == 0:
                    print("Sua lista de afazeres está vazia.")
                else:
                    print("Tarefas Pendentes:")
                    salvar_lista.ler_bloco_notas()

        else:
            print("Você não tem tarefas concluídas.")
        
        if mostrar.lower() == "todas":
            if len(lista_afazeres) == 0 and len(Tarefas_concluidas) == 0:
                print("todas as suas listas estão vazias.")
            else:
                contador = 0
                print("Tarefas Pendentes:")
                for tarefa in lista_afazeres:
                    contador +=1
                    print(f"{contador}-{tarefa}")


                print("Tarefas Concluídas:")
                for tarefa in Tarefas_concluidas:
                    contador +=1
                    print(f"{contador}-[X]{tarefa}")


    elif afazer.lower() == "marcar como concluido":
        tarefa = input("Digite a tarefa que deseja marcar como concluída: ")
        if tarefa in lista_afazeres:
            salvar_lista.tarefas_feitas(tarefa,Tarefas_concluidas)

        else:
            print("Sua lista de afazeres está vazia.")

    elif afazer.lower() == "sair":
        print("Saindo da sua lista de afazeres. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção das opções descritas.")
