class Garagem:
    def __init__(self, carro):
        self.carro = carro
        self.anterior = None
        self.proximo = None

def inserir(pilha, carro):
    novo = Garagem(carro)

    novo.proximo = pilha
    if pilha is not None:
        pilha.anterior = novo

    return novo

def criar_pilha(pilha):
    carros = [
        "Opala", "Chevette", "Corsel 2", "Fusca", "Kombi", "Monza",
        "Maverick", "Impala", "Puma", "Gol chaleira", "HB20",
        "Santa Matilde", "Kadett", "Dodge Dart", "Pajero",
        "Fiat 147", "Galaxy", "Dodge Ram", "Saveiro rebaixada", "Omega"
    ]

    for carro in carros:
        pilha = inserir(pilha, carro)

    return pilha

def remover_carro(pilha, carro):
    retirados = []

    aux = pilha
    encontrado = False
    while aux is not None:
        if aux.carro == carro:
            encontrado = True
            break
        aux = aux.proximo

    if not encontrado:
        print("Carro não encontrado!")
        return pilha, retirados

    atual = pilha
    while atual.proximo is not None:
        atual = atual.proximo

    while atual is not None:
        retirados.append(atual.carro)

        if atual.carro == carro:
            if atual.anterior is not None:
                atual.anterior.proximo = None
            else:
                pilha = None
            break

        atual = atual.anterior

    return pilha, retirados

def mostrar_pilha(pilha):
    aux = pilha
    while aux != None:
        print(" - ", aux.carro)
        aux = aux.proximo

def main():
    pilha = None
    pilha = criar_pilha(pilha)

    print("Carros na garagem")
    mostrar_pilha(pilha)

    carro = str(input("Digite o carro que deseja retirar:"))
    pilha, retirados = remover_carro(pilha, carro)

    print("Carros retirados da garagem")
    for i in retirados:
        print(" - ", i)

main()