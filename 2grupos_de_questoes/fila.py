class Fila:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None

def enfileirar(fila, fim_fila, dado):
    novo = Fila(dado)

    print("Elemento adicionado")
    if fim_fila == None and fila == None:
        fim_fila = fila = novo
        return fila, fim_fila
    
    fim_fila.proximo = novo
    novo.anterior = fim_fila
    fim_fila = novo
    return fila, fim_fila

def desenfileirar(fila, fim_fila):
    if fila is None:
        print("Fila vazia")
        return None, None
    
    elif fila == fim_fila:
        print("Elemento removido")
        return None, None
    
    print("Elemento removido")
    fila.proximo.anterior = None
    fila = fila.proximo
    return fila, fim_fila

def percorrer(fila):
    if fila == None:
        print("Fila vazia")

    aux = fila
    print("Fila completa")
    while aux != None:
        print(" - ", aux.dado)
        aux = aux.proximo

def topo(fila):
    if fila == None:
        print("Fila vazia")

    print("Elemento do topo")
    print(" - ", fila.dado)

def esta_vazia(fila):
    if fila == None:
        print("Fila vazia")
    else:
        print("Fila não está vazia")

def tamanho(fila):
    if fila == None:
        print("Fila vazia")
    
    tamanho = 0
    aux = fila
    while aux != None:
        tamanho += 1
        aux = aux.proximo

    print("Tamanho da fila:", tamanho)

def media(fila):
    if fila == None:
        print("Fila vazia")
    
    media = 0
    aux = fila
    while aux != None:
        media += aux.dado
        aux = aux.proximo
    
    tamanho = 0
    aux = fila
    while aux != None:
        tamanho += 1
        aux = aux.proximo

    media = media/tamanho
    print("Média:", media)

def main():
    fila = fim_fila = None

    for i in range(3):
        if i == 0:
            dado = 123
            fila, fim_fila  = enfileirar(fila, fim_fila, dado)
        elif i == 1:
            dado = 456
            fila, fim_fila = enfileirar(fila, fim_fila, dado)
        else:
            dado = 789
            fila, fim_fila = enfileirar(fila, fim_fila, dado)

    percorrer(fila)
    fila, fim_fila = desenfileirar(fila, fim_fila)
    percorrer(fila)
    
    print("--------------------")
    esta_vazia(fila)
    dado = 789
    fila, fim_fila = enfileirar(fila, fim_fila, dado)
    percorrer(fila)
    topo(fila)
    fila, fim_fila = desenfileirar(fila, fim_fila)
    percorrer(fila)
    topo(fila)
    fila, fim_fila = desenfileirar(fila, fim_fila)
    fila, fim_fila = desenfileirar(fila, fim_fila)
    esta_vazia(fila)

    print("--------------------")
    for i in range(3):
        if i == 0:
            dado = 123
            fila, fim_fila = enfileirar(fila, fim_fila, dado)
        elif i == 1:
            dado = 456
            fila, fim_fila = enfileirar(fila, fim_fila, dado)
        else:
            dado = 789
            fila, fim_fila = enfileirar(fila, fim_fila, dado)

    percorrer(fila)
    tamanho(fila)
    media(fila)

main()