class No:
    def __init__(self, nome, pais_origem):
        self.nome = nome
        self.pais_origem = pais_origem
        self.proximo = None

def inserir_satelite(lista, nome, pais_origem):
    novo = No(nome, pais_origem)

    if lista is None:
        return novo

    aux = lista
    while aux.proximo:
        aux = aux.proximo

    aux.proximo = novo
    return lista

def listar_satelites(lista):
    if lista is None:
        print("Lista vazia")
        return

    aux = lista
    while aux:
        print(aux.nome, "-", aux.pais_origem)
        aux = aux.proximo

def remover_satelite(lista, nome):
    if lista is None:
        return None

    if lista.nome == nome:
        return lista.proximo

    ant = lista
    atual = lista.proximo

    while atual:
        if atual.nome == nome:
            ant.proximo = atual.proximo
            return lista
        ant = atual
        atual = atual.proximo

    return lista

def main():
    lista = None

    lista = inserir_satelite(lista, "Hubble", "Estados Unidos")
    lista = inserir_satelite(lista, "James Webb", "Estados Unidos")
    lista = inserir_satelite(lista, "Amazônia-1", "Brasil")

    print("Lista inicial:")
    listar_satelites(lista)

    lista = remover_satelite(lista, "Hubble")

    print("\nApós remover Hubble:")
    listar_satelites(lista)

main()