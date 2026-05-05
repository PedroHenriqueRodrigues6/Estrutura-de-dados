class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def adicionar_inicio(self, dado):
        novo = No(dado)
        novo.proximo = self.inicio
        self.inicio = novo

    def adicionar_final(self, dado):
        novo = No(dado)

        if self.inicio is None:
            self.inicio = novo
            return

        atual = self.inicio
        while atual.proximo:
            atual = atual.proximo

        atual.proximo = novo

    def percorrer(self):
        atual = self.inicio
        while atual:
            print(atual.dado, end=" -> ")
            atual = atual.proximo
        print("None")

    def media(self):
        soma = 0
        quantidade = 0
        atual = self.inicio

        while atual:
            soma += atual.dado
            quantidade += 1
            atual = atual.proximo

        if quantidade == 0:
            return 0

        return soma / quantidade

lista = ListaEncadeada()

lista.adicionar_inicio(10)
lista.adicionar_inicio(5)
lista.adicionar_final(20)
lista.adicionar_final(15)

lista.percorrer()

print("Média:", lista.media())