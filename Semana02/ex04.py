class No:
    def __init__(self, item):
        self.item = item
        self.proximo = None

def inserir_item_primeira_lista(lista1, item):
    novo_item = No(item)
    novo_item.proximo = lista1
    lista1 = novo_item
    return lista1

def listar_itens_primeira_lista(lista1):
    aux = lista1

    if aux == None:
        print("Lista vazia")
        return
    
    while aux is not None:
        print("Item", aux.item)
        aux = aux.proximo

def excluir_item_primeira_lista(lista1, item):
    aux = lista1
    anterior = None

    while aux is not None:
        if aux.item == item:
            if lista1 == aux:
                lista1 = lista1.proximo
                return lista1
            
            elif aux.proximo == None:
                anterior.proximo = None
                return lista1
            
            else:
                anterior.proximo = aux.proximo
                return lista1
        
        else:
            anterior = aux
            aux = aux.proximo
        
    print("Elemento não encontrado")
    return lista1

def inserir_item_segunda_lista(lista2, item):
    novo_item = No(item)
    novo_item.proximo = lista2
    lista2 = novo_item
    return lista2

def listar_itens_segunda_lista(lista2):
    aux = lista2

    if aux == None:
        print("Lista vazia")
        return
    
    while aux is not None:
        print("Item", aux.item)
        aux = aux.proximo

def excluir_item_segunda_lista(lista2, item):
    aux = lista2
    anterior = None

    while aux is not None:
        if aux.item == item:
            if lista2 == aux:
                lista2 = lista2.proximo
                return lista2
            
            elif aux.proximo == None:
                anterior.proximo = None
                return lista2
            
            else:
                anterior.proximo = aux.proximo
                return lista2
        
        else:
            anterior = aux
            aux = aux.proximo
        
    print("Elemento não encontrado")
    return lista2

def concatena(lista1, lista2):
    if lista1 is None:
        return lista2
    
    if lista2 is None:
        lista_concatenada = No(lista1.item)
        atual_novo = lista_concatenada
        atual_antigo = lista1.proximo
        while atual_antigo:
            atual_novo.proximo = No(atual_antigo.item)
            atual_novo = atual_novo.proximo
            atual_antigo = atual_antigo.proximo
        return lista_concatenada

    lista_concatenada = No(lista1.item)
    atual_novo = lista_concatenada
    atual_antigo = lista1.proximo

    while atual_antigo:
        atual_novo.proximo = No(atual_antigo.item)
        atual_novo = atual_novo.proximo
        atual_antigo = atual_antigo.proximo

    atual_novo.proximo = lista2

    aux = lista_concatenada

    if aux == None:
        print("Lista vazia")
        return
    
    while aux is not None:
        print("Item", aux.item)
        aux = aux.proximo

    return lista_concatenada

def menu():
    print("1 - Inserir item na primeira lista")
    print("2 - Listar itens da primeira lista")
    print("3 - Excluir item da primeira lista")
    print("4 - Inserir item na segunda lista")
    print("5 - Listar itens da segunda lista")
    print("6 - Excluir item da segunda lista")
    print("7 - Concatenar listas")
    print("8 - Sair")
    opc = int(input("Digite uma opção:"))
    return opc

def main():
    lista1 = None
    lista2 = None
    lista_concatenada = None
    opc = 0

    while opc != 8:
        opc = menu()

        if opc == 1:
            item = int(input("Digite um item para inserir:"))
            lista1 = inserir_item_primeira_lista(lista1, item)

        elif opc == 2:
            listar_itens_primeira_lista(lista1)

        elif opc == 3:
            item = int(input("Digite um item para excluir:"))
            lista1 = excluir_item_primeira_lista(lista1, item)

        if opc == 4:
            item = int(input("Digite um item para inserir:"))
            lista2 = inserir_item_segunda_lista(lista2, item)

        elif opc == 5:
            listar_itens_segunda_lista(lista2)

        elif opc == 6:
            item = int(input("Digite um item para excluir:"))
            lista2 = excluir_item_segunda_lista(lista2, item)

        elif opc == 7:
            lista_concatenada = concatena(lista1, lista2)

main()
