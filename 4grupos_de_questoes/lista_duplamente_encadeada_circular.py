class NoDuploCircular:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None

class ListaDuplamenteEncadeadaCircular:
    def __init__(self):
        self.inicio = None

    def adicionar_inicio(self, dado):
        novo = NoDuploCircular(dado)

        if self.inicio is None:
            novo.proximo = novo
            novo.anterior = novo
            self.inicio = novo
        else:
            ultimo = self.inicio.anterior

            novo.proximo = self.inicio
            novo.anterior = ultimo

            ultimo.proximo = novo
            self.inicio.anterior = novo

            self.inicio = novo

    def adicionar_final(self, dado):
        novo = NoDuploCircular(dado)

        if self.inicio is None:
            novo.proximo = novo
            novo.anterior = novo
            self.inicio = novo
        else:
            ultimo = self.inicio.anterior

            novo.proximo = self.inicio
            novo.anterior = ultimo

            ultimo.proximo = novo
            self.inicio.anterior = novo

    def percorrer_frente(self, quantidade):
        if self.inicio is None:
            return

        atual = self.inicio
        for _ in range(quantidade):
            print(atual.dado, end=" -> ")
            atual = atual.proximo
        print("...")

    def percorrer_tras(self, quantidade):
        if self.inicio is None:
            return

        atual = self.inicio.anterior
        for _ in range(quantidade):
            print(atual.dado, end=" -> ")
            atual = atual.anterior
        print("...")

    def remover(self, dado):
        if self.inicio is None:
            return

        atual = self.inicio

        while True:
            if atual.dado == dado:
                if atual.proximo == atual:
                    self.inicio = None
                else:
                    atual.anterior.proximo = atual.proximo
                    atual.proximo.anterior = atual.anterior

                    if atual == self.inicio:
                        self.inicio = atual.proximo
                return

            atual = atual.proximo
            if atual == self.inicio:
                break

lista = ListaDuplamenteEncadeadaCircular()

lista.adicionar_inicio(10)
lista.adicionar_inicio(5)
lista.adicionar_final(20)
lista.adicionar_final(30)

print("Frente:")
lista.percorrer_frente(8)

print("Trás:")
lista.percorrer_tras(8)

print("Removendo 5...")
lista.remover(5)

print("Frente após remoção:")
lista.percorrer_frente(8)

print("Trás após remoção:")
lista.percorrer_tras(8)