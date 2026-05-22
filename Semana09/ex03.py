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

        print("Chamado urgente adicionado.")

    def inserir_fim(self, dado):

        novo = Node(dado)

        if self.fim is None:

            self.inicio = self.fim = novo

        else:

            novo.anterior = self.fim
            self.fim.proximo = novo
            self.fim = novo

        self.tamanho += 1

        print("Chamado comum adicionado.")

    def remover_inicio(self):

        if self.inicio is None:

            print("Fila vazia.")
            return

        chamado = self.inicio.dado

        self.inicio = self.inicio.proximo

        if self.inicio:

            self.inicio.anterior = None

        else:

            self.fim = None

        self.tamanho -= 1

        print("Chamado atendido:", chamado)

    def remover_fim(self):

        if self.fim is None:

            print("Fila vazia.")
            return

        chamado = self.fim.dado

        self.fim = self.fim.anterior

        if self.fim:

            self.fim.proximo = None

        else:

            self.inicio = None

        self.tamanho -= 1

        print("Chamado atendido:", chamado)

    def listar(self):

        if self.inicio is None:

            print("Nenhum chamado na fila.")
            return

        aux = self.inicio

        print("\nFila de chamados:")

        while aux:

            print("-", aux.dado)

            aux = aux.proximo

        print()


def main():

    fila = Deque()

    opcao = 0

    while opcao != 6:

        print("\n=== SISTEMA DE CHAMADOS TI ===")
        print("1 - Adicionar chamado comum")
        print("2 - Adicionar chamado urgente")
        print("3 - Atender primeiro chamado")
        print("4 - Atender último chamado")
        print("5 - Listar chamados")
        print("6 - Sair")

        opcao = int(input("Escolha: "))

        if opcao == 1:

            chamado = input("Descrição do chamado: ")

            fila.inserir_fim(chamado)

        elif opcao == 2:

            chamado = input("Descrição do chamado urgente: ")

            fila.inserir_inicio(chamado)

        elif opcao == 3:

            fila.remover_inicio()

        elif opcao == 4:

            fila.remover_fim()

        elif opcao == 5:

            fila.listar()

    print("Sistema encerrado.")


main()