def funcao_bloco(tarefa):
    with open("Tarefas_salvas,"a") as afazer:
        afazer.write(tarefa,"/n")