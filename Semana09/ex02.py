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

    def inserir_fim(self, dado):

        novo = Node(dado)

        if self.fim is None:
            self.inicio = self.fim = novo
        else:
            novo.anterior = self.fim
            self.fim.proximo = novo
            self.fim = novo

        self.tamanho += 1

    def remover_fim(self):

        if self.fim is None:
            return None

        removido = self.fim.dado

        self.fim = self.fim.anterior

        if self.fim:
            self.fim.proximo = None
        else:
            self.inicio = None

        self.tamanho -= 1

        return removido

    def pagina_atual(self):

        if self.fim:
            return self.fim.dado

        return "Nenhuma página"

    def listar(self):

        aux = self.inicio

        print("\nHistórico:")

        if aux is None:
            print("Vazio")
            return

        while aux:

            print("-", aux.dado)

            aux = aux.proximo

        print("Página atual:", self.pagina_atual())


def main():

    historico = Deque()
    avanco = []

    opcao = 0

    while opcao != 4:

        print("\n1 - Acessar site")
        print("2 - Voltar")
        print("3 - Avançar")
        print("4 - Sair")

        opcao = int(input("Escolha: "))

        if opcao == 1:

            site = input("Digite o site: ")

            historico.inserir_fim(site)

            avanco.clear()

            historico.listar()

        elif opcao == 2:

            if historico.tamanho > 1:

                pagina = historico.remover_fim()

                avanco.append(pagina)

            else:

                print("Não há página anterior")

            historico.listar()

        elif opcao == 3:

            if len(avanco) > 0:

                pagina = avanco.pop()

                historico.inserir_fim(pagina)

            else:

                print("Nenhuma página para avançar")

            historico.listar()

main()