class Satelite:
    def __init__(self, nome, altitude, combustivel, ativo):
        self.nome = nome
        self.altitude = altitude
        self.combustivel = combustivel
        self.ativo = ativo
        self.proximo = None
        self.anterior = None

def menu():
    print("\n1 - Adicionar satélite")
    print("2 - Remover satélite")
    print("3 - Simular volta")
    print("4 - Percurso horário")
    print("5 - Percurso anti-horário")
    print("6 - Reposicionamento")
    print("7 - Mostrar desativados")
    print("8 - Mostrar ativados")
    print("9 - Sair")
    return int(input("Escolha: "))

def adicionar_satelite(lista, nome, altitude, combustivel, ativo):
    if altitude < 300:
        print("Altitude inválida")
        return lista

    novo = Satelite(nome, altitude, combustivel, ativo)

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

def remover_satelite(lista, nome):
    if lista is None:
        return None

    aux = lista

    while True:
        if aux.nome == nome:
            if aux.proximo == aux:
                return None

            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

            if aux == lista:
                lista = aux.proximo

            return lista

        aux = aux.proximo
        if aux == lista:
            break

    return lista

def simular_volta(lista):
    if lista is None:
        return None

    aux = lista

    while True:
        aux.combustivel -= 10

        if aux.combustivel <= 0:
            aux.ativo = False

        aux = aux.proximo
        if aux == lista:
            break

    return lista

def percurso_horario(lista):
    if lista is None:
        return

    aux = lista
    while True:
        print(aux.nome)
        aux = aux.proximo
        if aux == lista:
            break

def percurso_antihorario(lista):
    if lista is None:
        return

    aux = lista.anterior
    inicio = aux

    while True:
        print(aux.nome)
        aux = aux.anterior
        if aux == inicio:
            break

def reposicionamento(lista, nome, nova_altitude):
    if nova_altitude < 300:
        print("Altitude inválida")
        return lista

    aux = lista

    while True:
        if aux.nome == nome:
            aux.altitude = nova_altitude
            return lista

        aux = aux.proximo
        if aux == lista:
            break

    return lista

def mostrar_desativados(lista):
    if lista is None:
        return

    aux = lista
    while True:
        if not aux.ativo:
            print(aux.nome)
        aux = aux.proximo
        if aux == lista:
            break

def mostrar_ativados(lista):
    if lista is None:
        return

    aux = lista
    while True:
        if aux.ativo:
            print(aux.nome)
        aux = aux.proximo
        if aux == lista:
            break

def main():
    lista = None
    opc = 0

    while opc != 9:
        opc = menu()

        if opc == 1:
            nome = input("Nome: ")

            altitude = 0
            while altitude < 300:
                altitude = int(input("Altitude (>=300): "))

            combustivel = 100
            ativo = True

            lista = adicionar_satelite(lista, nome, altitude, combustivel, ativo)

        elif opc == 2:
            nome = input("Nome do satélite a remover: ")
            lista = remover_satelite(lista, nome)

        elif opc == 3:
            lista = simular_volta(lista)

        elif opc == 4:
            percurso_horario(lista)

        elif opc == 5:
            percurso_antihorario(lista)

        elif opc == 6:
            nome = input("Nome do satélite: ")
            nova_altitude = int(input("Nova altitude: "))
            lista = reposicionamento(lista, nome, nova_altitude)

        elif opc == 7:
            print("\nSatélites desativados:")
            mostrar_desativados(lista)

        elif opc == 8:
            print("\nSatélites ativados:")
            mostrar_ativados(lista)

        elif opc == 9:
            print("Encerrando...")

        else:
            print("Opção inválida")

main()