import random

class Guerreiros:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None
        self.anterior = None

def adicionar_guerreiro(lista, nome):
    novo = Guerreiros(nome)

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

def simular_rodadas(lista, quantidade):
    aux = lista
    restantes = quantidade

    while aux.proximo != aux:
        passos = random.randint(1, restantes)

        for i in range(passos):
            aux = aux.proximo

        print(aux.nome, "foi eliminado!")

        aux.anterior.proximo = aux.proximo
        aux.proximo.anterior = aux.anterior

        if aux == lista:
            lista = aux.proximo

        aux = aux.proximo
        restantes -= 1
        
    print("Sobrevivente:", aux.nome)
    return aux
            
def main():
    lista = None

    quantidade = int(input("Digite a quantidade de guerreiros: "))
    
    for i in range(quantidade):
        nome = str(input("Digite o nome do guerreiro:"))
        lista = adicionar_guerreiro(lista, nome)

    simular_rodadas(lista, quantidade)

main()