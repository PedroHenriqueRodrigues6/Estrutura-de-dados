import random

class Pilha:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None

def empilhar(pilha, dado):
    novo = Pilha(dado)

    print("Elemento adicionado")
    if pilha is None:
        pilha = novo
        return pilha
    
    novo.proximo = pilha
    pilha.anterior = novo
    pilha = novo
    return pilha

def desempilhar(pilha):
    if pilha is None:
        print("Pilha vazia")
        return None
    
    elif pilha.proximo == None:
        print("Elemento removido")
        return None
    
    print("Elemento removido")
    pilha.proximo.anterior = None
    pilha = pilha.proximo
    return pilha

def percorrer(pilha):
    if pilha == None:
        print("Pilha vazia")

    aux = pilha
    print("Pilha completa")
    while aux != None:
        print(" - ", aux.dado)
        aux = aux.proximo

def topo(pilha):
    if pilha == None:
        print("Pilha vazia")

    print("Elemento do topo")
    print(" - ", pilha.dado)

def esta_vazia(pilha):
    if pilha == None:
        print("Pilha vazia")
    else:
        print("Pilha não está vazia")

def tamanho(pilha):
    if pilha == None:
        print("Pilha vazia")
    
    tamanho = 0
    aux = pilha
    while aux != None:
        tamanho += 1
        aux = aux.proximo

    print("Tamanho da pilha:", tamanho)

def media(pilha):
    if pilha == None:
        print("Pilha vazia")
    
    media = 0
    aux = pilha
    while aux != None:
        media += aux.dado
        aux = aux.proximo
    
    tamanho = 0
    aux = pilha
    while aux != None:
        tamanho += 1
        aux = aux.proximo

    media = media/tamanho
    print("Média:", media)

def main():
    pilha = None

    for i in range(3):
        if i == 0:
            dado = 123
            pilha = empilhar(pilha, dado)
        elif i == 1:
            dado = 456
            pilha = empilhar(pilha, dado)
        else:
            dado = 789
            pilha = empilhar(pilha, dado)

    percorrer(pilha)
    pilha = desempilhar(pilha)
    percorrer(pilha)

    print("--------------------")
    esta_vazia(pilha)
    dado = 789
    pilha = empilhar(pilha, dado)
    percorrer(pilha)
    topo(pilha)
    pilha = desempilhar(pilha)
    percorrer(pilha)
    topo(pilha)
    pilha = desempilhar(pilha)
    pilha = desempilhar(pilha)
    esta_vazia(pilha)

    print("--------------------")
    for i in range(3):
        if i == 0:
            dado = 123
            pilha = empilhar(pilha, dado)
        elif i == 1:
            dado = 456
            pilha = empilhar(pilha, dado)
        else:
            dado = 789
            pilha = empilhar(pilha, dado)

    percorrer(pilha)
    tamanho(pilha)
    media(pilha)

main()
