class No:
    def __init__(self, nome, identificador):
        self.nome = nome
        self.identificador = identificador
        self.proximo = None
        self.anterior = None

def inserir_no(lista, aluno, identificador):
    novo = No(aluno, identificador)

    if lista == None:
        lista = novo
        return lista
    
    lista.anterior = novo
    novo.proximo = lista
    lista = novo
    return lista

def listar_nos(lista):
    aux = lista
    
    if aux == None:
        print("No não encontrado")
        return

    while aux != None:
        print("Nome:", aux.nome,
              "\nIdentificador:", aux.identificador)
        aux = aux.proximo

def remover_no(lista, nome):
    aux = lista

    while aux is not None:

        if aux.nome == nome:
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
    
    print("No não encontrado")
    return lista

def verificar_no(lista, opc2, aux2):
    aux = lista

    if aux == None:
        print("No não encontrado")
        return

    if opc2 == 1:
        while aux is not None:
            if aux2 == aux.nome:
                print("No existe",
                "\nNome:",aux.nome,
                "\nIdentificador:",aux.identificador)
                return
            aux = aux.proximo

    elif opc2 == 2:
        while aux is not None:
            if aux2 == aux.identificador:
                print("No existe",
                "\nNome:",aux.nome,
                "\nIdentificador:",aux.identificador)
                return
            aux = aux.proximo
    print("No não existe")

def menu1():
    print("1 - Inserir no")
    print("2 - Listar nos")
    print("3 - Remover no")
    print("4 - Verificar se no existe")
    print("5 - Sair")
    opc1 = int(input("Digite a opção:"))
    return opc1

def menu2():
    print("1 - Buscar por nome")
    print("2 - Buscar por identificador")
    opc2 = int(input("Digite a opção:"))
    return opc2

def main():
    lista = None
    opc1 = 0
    opc2 = 0

    while opc1 != 5:
        opc1 = menu1()
        
        if opc1 == 1:
            nome = str(input("Digite um nome:"))
            identificador = int(input("Digite um identificador:"))
            lista = inserir_no(lista, nome, identificador)

        elif opc1 == 2:
            listar_nos(lista)

        elif opc1 == 3:
            nome = str(input("Digite um nome:"))
            lista = remover_no(lista, nome)

        elif opc1 == 4:
            opc2 = menu2()
            if opc2 == 1:
                aux2 = str(input("Digite um nome:"))
                verificar_no(lista, opc2, aux2)

            elif opc2 == 2:
                aux2 = int(input("Digite um identificador:"))
                verificar_no(lista, opc2, aux2)

            else:
                print("Opção inválida")
            
main()