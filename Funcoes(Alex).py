class Tarefa:
    def __init__(self):
        self.lista_afazeres = []

    def adicionar_tarefa(self):
        tarefa = input("Digite a tarefa que deseja adicionar: ")
        self.lista_afazeres.append(tarefa)

    def listar_tarefas(self):
        
