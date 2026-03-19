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
        print("Item", aux.item)
        aux = aux.proximo

def excluir_item(lista, item):
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

def maiores(lista, n):
    aux = lista
    contador = 0

    while aux is not None:
        if aux.item > n:
            contador += 1
            aux = aux.proximo

        else:
            aux = aux.proximo

    print("Quantidade de nós:", contador)
    return lista

def menu():
    print("1 - Inserir item")
    print("2 - Listar itens")
    print("3 - Excluir item")
    print("4 - Contar nós")
    print("5 - Sair")
    opc = int(input("Digite uma opção:"))
    return opc

def main():
    lista = None
    opc = 0

    while opc != 5:
        opc = menu()

        if opc == 1:
            item = int(input("Digite um item para inserir:"))
            lista = inserir_item(lista, item)

        elif opc == 2:
            listar_itens(lista)

        elif opc == 3:
            item = int(input("Digite um item para excluir:"))
            lista = excluir_item(lista, item)

        elif opc == 4:
            n = int(input("Digite um item:"))
            lista = maiores(lista, n)

main()
