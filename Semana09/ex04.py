class Node:

    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None


class Deque:

    def __init__(self):

        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def inserir_inicio(self, dado):

        novo = Node(dado)

        if self.inicio is None:

            self.inicio = self.fim = novo

        else:

            novo.proximo = self.inicio
            self.inicio.anterior = novo
            self.inicio = novo

        self.tamanho += 1

        print(dado, "entrou como preferencial")

    def inserir_fim(self, dado):

        novo = Node(dado)

        if self.fim is None:

            self.inicio = self.fim = novo

        else:

            novo.anterior = self.fim
            self.fim.proximo = novo
            self.fim = novo

        self.tamanho += 1

        print(dado, "entrou na fila comum")

    def remover_inicio(self):

        if self.inicio is None:

            print("Fila vazia")
            return

        cliente = self.inicio.dado

        self.inicio = self.inicio.proximo

        if self.inicio:

            self.inicio.anterior = None

        else:

            self.fim = None

        self.tamanho -= 1

        print(cliente, "foi atendido")

    def listar(self):

        if self.inicio is None:

            print("Fila vazia")
            return

        aux = self.inicio

        print("\nOrdem atual de atendimento:")

        while aux:

            print("-", aux.dado)

            aux = aux.proximo

        print()


def main():

    fila = Deque()

    opcao = 0

    while opcao != 4:

        print("\n=== BANCO ===")
        print("1 - Cliente comum")
        print("2 - Cliente preferencial")
        print("3 - Atender cliente")
        print("4 - Sair")

        opcao = int(input("Escolha: "))

        if opcao == 1:

            nome = input("Nome do cliente: ")

            fila.inserir_fim(nome)

            fila.listar()

        elif opcao == 2:

            nome = input("Nome do cliente: ")

            fila.inserir_inicio(nome)

            fila.listar()

        elif opcao == 3:

            fila.remover_inicio()

            fila.listar()


main()