class Clientes:
    def __init__(self, nome, fatia):
        self.nome = nome
        self.fatia = fatia
        self.proximo = None
        self.anterior = None

def menu():
    print("1 - Adicionar cliente")
    print("2 - Remover cliente")
    print("3 - Passar fatia")
    print("4 - Sair")
    opcao = int(input("Digite uma opção:"))
    return opcao

def adicionar_cliente(lista, nome):
    novo = Clientes(nome, False)

    if lista is None:
        novo.proximo = novo
        novo.anterior = novo
        lista = novo
        return lista

    lista.anterior.proximo = novo
    novo.anterior = lista.anterior
    lista.anterior = novo 
    novo.proximo = lista
    lista = novo
    return lista

def remover_cliente(lista, nome):
    aux = lista

    if lista is None:
        print("Nenhum cliente no restaurante")
        return None

    while True:

        if aux.nome == nome:
            if aux == aux.proximo == aux.anterior: 
                print("O cliente foi embora, restaurante vazio")
                return None
            
            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

            if aux == lista:
                lista = lista.proximo
            return lista

        aux = aux.proximo
        if aux == lista:
            print("Cliente não encontrado")
            return lista

def passar_fatia(lista):
    if lista is None:
        print("Nenhum cliente no restaurante")
        return

    aux = lista

    while True:
        if aux.fatia:
            print("Cliente", aux.nome, "passou a fatia para", aux.proximo.nome)

            aux.fatia = False
            aux.proximo.fatia = True
            return

        aux = aux.proximo
        if aux == lista:
            break

    lista.fatia = True
    print("Cliente", lista.nome, "pegou a primeira fatia")

def main():
    lista = None
    opcao = 0

    while opcao != 4:
        opcao = menu()

        if opcao == 1:
            nome = str(input("Digite o nome do cliente:"))
            lista = adicionar_cliente(lista, nome)

        elif opcao == 2:
            nome = str(input("Digite o nome do cliente:"))
            lista = remover_cliente(lista, nome)

        elif opcao == 3:
            passar_fatia(lista)

        elif opcao == 4:
            return

        else:
            print("Opção inválida")

main()