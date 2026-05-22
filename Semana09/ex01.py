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
        print(dado, "adicionado como URGENTE")

    def inserir_fim(self, dado):
        novo = Node(dado)

        if self.fim is None:
            self.inicio = self.fim = novo
        else:
            novo.anterior = self.fim
            self.fim.proximo = novo
            self.fim = novo

        self.tamanho += 1
        print(dado, "adicionado na fila")

    def remover_inicio(self):

        if self.inicio is None:
            print("Nenhum documento para imprimir")
            return

        documento = self.inicio.dado

        self.inicio = self.inicio.proximo

        if self.inicio:
            self.inicio.anterior = None
        else:
            self.fim = None

        self.tamanho -= 1

        print("Documento impresso:", documento)

    def listar_frente(self):

        if self.inicio is None:
            print("Fila vazia")
            return

        aux = self.inicio

        print("Fila atual:")

        while aux is not None:
            print("-", aux.dado)
            aux = aux.proximo

        print()

def main():

    impressora = Deque()
    opcao = 0

    while opcao != 4:

        print("\n1 - Novo documento")
        print("2 - Documento urgente")
        print("3 - Processar impressão")
        print("4 - Sair")

        opcao = int(input("Escolha: "))

        if opcao == 1:

            doc = input("Nome do documento: ")
            impressora.inserir_fim(doc)
            impressora.listar_frente()

        elif opcao == 2:

            doc = input("Nome do documento urgente: ")
            impressora.inserir_inicio(doc)
            impressora.listar_frente()

        elif opcao == 3:

            impressora.remover_inicio()
            impressora.listar_frente()

main()
