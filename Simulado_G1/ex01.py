class Satelite:
    def __init__(self, id, altitude, integridade=100):
        self.id = id
        self.altitude = altitude
        self.integridade = integridade
        self.proximo = None
        self.anterior = None

def cadastrar_satelite(lista, id, altitude):
    novo = Satelite(id, altitude)

    if lista is None:
        novo.proximo = novo
        novo.anterior = novo
        return novo

    ultimo = lista.anterior

    ultimo.proximo = novo
    novo.anterior = ultimo
    novo.proximo = lista
    lista.anterior = novo

    return lista

def listar_satelites(lista):
    if lista is None:
        print("Nenhum satélite cadastrado")
        return

    aux = lista
    while True:
        print(f"ID: {aux.id} | Integridade: {aux.integridade}")
        aux = aux.proximo
        if aux == lista:
            break

def simular_volta(lista, sat1, sat2):
    if lista is None:
        return None

    aux = lista

    while True:
        if aux.id == sat1 or aux.id == sat2:
            aux.integridade -= 20

        prox = aux.proximo

        if aux.integridade <= 0:
            if aux.proximo == aux:
                return None

            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

            if aux == lista:
                lista = aux.proximo

        aux = prox
        if aux == lista:
            break

    return lista

def main():
    lista = None

    for i in range(3):
        id = int(input("Digite o ID do satélite: "))
        altitude = int(input("Digite a altitude: "))
        lista = cadastrar_satelite(lista, id, altitude)

    listar_satelites(lista)

    for i in range(3):
        sat1 = int(input("ID do satélite 1: "))
        sat2 = int(input("ID do satélite 2: "))
        lista = simular_volta(lista, sat1, sat2)

    print("\nApós simulação:")
    listar_satelites(lista)

main()
