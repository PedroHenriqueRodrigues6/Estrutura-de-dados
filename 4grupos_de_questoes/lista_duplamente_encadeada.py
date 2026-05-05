class NoDuplo:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None

    def adicionar_inicio(self, dado):
        novo = NoDuplo(dado)

        if self.inicio is not None:
            self.inicio.anterior = novo
            novo.proximo = self.inicio

        self.inicio = novo

    def percorrer_frente(self):
        atual = self.inicio
        while atual:
            print(atual.dado, end=" <-> ")
            atual = atual.proximo
        print("None")

    def percorrer_tras(self):
        atual = self.inicio

        while atual and atual.proximo:
            atual = atual.proximo

        while atual:
            print(atual.dado, end=" <-> ")
            atual = atual.anterior
        print("None")

lista = ListaDuplamenteEncadeada()

lista.adicionar_inicio(10)
lista.adicionar_inicio(5)
lista.adicionar_inicio(1)

print("Percorrendo para frente:")
lista.percorrer_frente()

print("Percorrendo para trás:")
lista.percorrer_tras()