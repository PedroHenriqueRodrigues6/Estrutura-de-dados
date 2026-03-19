class No:
    def __init__(self, item):
        self.item = item
        self.proximo = None

def inserir_item(lista, item):
    novo_item = No(item)
    novo_item.proximo = lista
    lista = novo_item
    return lista

def listar_itens(lista):
    aux = lista

    if aux == None:
        print("Lista vazia")
        return
    
    while aux is not None:
        print("Item:", aux.item)
        aux = aux.proximo

def remover_item(lista, item):
    aux = lista
    anterior = None

    while aux is not None:
        if aux.item == item:
            if lista == aux:
                lista = lista.proximo
                return lista
            
            elif aux.proximo == None:
                anterior.proximo = None
                return lista
            
            else:
                anterior.proximo = aux.proximo
                return lista
            
        else:
            anterior = aux
            aux = aux.proximo

    print("Elemento não encontrado")
    return lista

def menu():
    print("1 - Inserir item")
    print("2 - Listar item")
    print("3 - Remover item")
    print("4 - Sair")
    opc = int(input("Digite uma opção:"))
    return opc

def main():
    lista = None
    opc = 0

    while opc != 4:
        opc = menu()

        if opc == 1:
            item = float(input("Digite um item para inserir:"))
            lista = inserir_item(lista, item)

        elif opc == 2:
            listar_itens(lista)
        
        elif opc == 3:
            item = float(input("Digite um item para excluir:"))
            lista = remover_item(lista, item)

main()
