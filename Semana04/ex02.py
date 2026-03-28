class Paradas:
    def __init__(self, parada):
        self.parada = parada
        self.proximo = None
        self.anterior = None

def menu():
    print("1 - Adicionar parada de ônibus")
    print("2 - Remover parada de ônibus")
    print("3 - Mostrar paradas")
    print("4 - Sair")
    opcao = int(input("Digite uma opção:"))
    return opcao

def adicionar_parada(lista, parada):
    novo = Paradas(parada)

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

def remover_parada(lista, parada):
    aux = lista

    if lista is None:
        print("Nenhuma parada inserida")
        return None

    while True:

        if aux.parada == parada:
            if aux == aux.proximo == aux.anterior: 
                print("Única parada inserida")
                return None
            
            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

            if aux == lista:
                lista = lista.proximo
            return lista

        aux = aux.proximo
        if aux == lista:
            print("Parada não encontrada")
            return lista

def mostrar_paradas(lista):
    if lista is None:
        print("Nenhuma parada inserida")
        return

    aux = lista

    while True:
        print(aux.parada)
        aux = aux.proximo

        if aux == lista:
            break
            
def main():
    lista = None
    opcao = 0

    while opcao != 4:
        opcao = menu()

        if opcao == 1:
            parada = str(input("Digite uma parada de ônibus:"))
            lista = adicionar_parada(lista, parada)

        elif opcao == 2:
            parada = str(input("Digite uma parada de ônibus:"))
            lista = remover_parada(lista, parada)

        elif opcao == 3:
            mostrar_paradas(lista)

        elif opcao == 4:
            return

        else:
            print("Opção inválida")

main()