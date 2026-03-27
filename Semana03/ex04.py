class No:
    def __init__(self, descricao, prazo):
        self.descricao = descricao
        self.prazo = prazo
        self.proximo = None
        self.anterior = None

def inserir_tarefa(lista, descricao, prazo):
    novo = No(descricao, prazo)

    if lista == None:
        lista = novo
        return lista
    
    lista.anterior = novo
    novo.proximo = lista
    lista = novo
    return lista

def remover_tarefa(lista, descricao):
    aux = lista

    while aux is not None:

        if aux.descricao == descricao:
            if aux.proximo == aux.anterior == None:
                return None
            
            elif aux.anterior == None:
                lista = aux.proximo
                lista.anterior = None
                return lista
            
            elif aux.proximo == None:
                aux.anterior.proximo = None
                return lista

            else:
                aux.anterior.proximo = aux.proximo
                aux.proximo.anterior = aux.anterior
                return lista

        else:
            aux = aux.proximo
    
    print("Tarefa não encontrada")
    return lista

def listar_tarefas(lista):
    aux = lista
    
    if aux == None:
        print("Nenhuma tarefa")
        return

    while aux != None:
        print("Descrição:", aux.descricao,
              "\nPrazo:", aux.prazo,
              "\n------------------------------")
        aux = aux.proximo

def menu():
    print("1 - Inserir tarefa")
    print("2 - Remover tarefa")
    print("3 - Listar tarefas")
    print("4 - Sair")
    opc = int(input("Digite uma opção:"))
    return opc

def main():
    lista = None
    opc = 0

    while opc != 4:
        opc = menu()
        
        if opc == 1:
            descricao = str(input("Digite uma descrição para a tarefa:"))
            prazo = str(input("Digite um prazo:"))
            lista = inserir_tarefa(lista, descricao, prazo)

        elif opc == 2:
            descricao = str(input("Digite a descrição da tarefa que deseja remover:"))
            lista = remover_tarefa(lista, descricao)

        elif opc == 3:
            listar_tarefas(lista)

        elif opc == 4:
            return

        else:
            print("Opção inválida")

main()