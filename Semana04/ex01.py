class Atletas:
    def __init__(self, id, bastao):
        self.id = id
        self.bastao = bastao
        self.proximo = None
        self.anterior = None

def menu():
    print("1 - Adicionar atleta")
    print("2 - Remover atleta")
    print("3 - Passar bastão")
    print("4 - Sair")
    opcao = int(input("Digite uma opção:"))
    return opcao

def adicionar_atleta(lista, id):
    novo = Atletas(id, False)

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

def remover_atleta(lista, id):
    aux = lista

    if lista is None:
        print("Nenhum atleta cadastrado")
        return None

    while True:

        if aux.id == id:
            if aux == aux.proximo == aux.anterior: 
                print("Único atleta cadastrado")
                return None
            
            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

            if aux == lista:
                lista = lista.proximo
            return lista

        aux = aux.proximo
        if aux == lista:
            print("Atleta não encontrado")
            return lista

def passar_bastao(lista, voltas):
    if lista is None:
        print("Nenhum atleta cadastrado")
        return

    aux = lista
    tem = False

    while True:
        if aux.bastao:
            tem = True
            break
        aux = aux.proximo
        if aux == lista:
            break

    if not tem:
        lista.bastao = True

    for i in range(voltas):
        print("\nTurno", i+1)

        atual = lista
        while True:
            if atual.bastao:
                print("Atleta", atual.id, "está com o bastão")

                atual.bastao = False
                atual.proximo.bastao = True
                break

            atual = atual.proximo

            if atual == lista:
                break
            
def main():
    lista = None
    opcao = 0

    while opcao != 4:
        opcao = menu()

        if opcao == 1:
            id = int(input("Digite o ID de um atleta:"))
            lista = adicionar_atleta(lista, id)

        elif opcao == 2:
            id = int(input("Digite o ID de um atleta:"))
            lista = remover_atleta(lista, id)

        elif opcao == 3:
            voltas = int(input("Quantos turnos deseja simular? "))
            passar_bastao(lista, voltas)

        elif opcao == 4:
            return

        else:
            print("Opção inválida")

main()
