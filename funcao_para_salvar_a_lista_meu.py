def tarefas_pendentes(lista_afazeres):
    pendentes = 0
    with open("Tarefas_pendentes","a") as afazer:

        for tarefa in lista_afazeres:
            afazer.write(f"{pendentes}-{tarefa}\n")
            pendentes +=1


def ler_bloco_notas():
     with open("Tarefas_pendentes") as leitura:
          print(leitura.read())


def tarefas_feitas(tarefa,tarefa_concluidas):
     completas = 0
     with open("Tarefas_pendentes","a") as concluidas:
            for tarefa in tarefa_concluidas:
                concluidas.write(f"[X]{tarefa}\n")
                completas +=1
