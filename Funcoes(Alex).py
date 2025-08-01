class Tarefa:
    def __init__(self):
        self.lista_afazeres = []

    def adicionar_tarefa(self):
        tarefa = input("Digite a tarefa que deseja adicionar: ")
        self.lista_afazeres.append(tarefa)

    def listar_tarefas(self):
        countdown = 0
        for tarefa in self.lista_afazeres:
            print(f"{countdown}-{tarefa}")
            countdown += 1
    
    def excluir_tarefas(self):
        
    


        
