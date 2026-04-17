class No:
    def __init__(self, jogador):
        self.jogador = jogador
        self.anterior = None
        self.proximo = None

def menu():
    print("1 - Adicionar jogador ao final da fila")
    print("2 - Remover jogador da fila")
    print("3 - Simular uma rodada")
    print("4 - Simular N rodadas")
    print("5 - Mostrar fila")
    print("6 - Mostrar próximo a jogar")
    print("7 - Limpar fila")
    print("8 - Sair")
    opcao = int(input("Digite a opção:"))
    return opcao

def adicionar_jogador(fila, fim_fila, jogador):
    novo = No(jogador)

    if fim_fila == None and fila == None:
        fim_fila = fila = novo
        return fila, fim_fila
    
    fim_fila.proximo = novo
    novo.anterior = fim_fila
    fim_fila = novo
    return fila, fim_fila

def remover_jogador(fila, fim_fila, jogador):
    if fila is None:
        print("Fila vazia")
        return None, None
    
    aux = fila
    while aux is not None:
        if aux.jogador == jogador:
            if aux.anterior is None:
                fila = aux.proximo
                if fila:
                    fila.anterior = None
                else:
                    fim_fila = None

            elif aux.proximo is None:
                fim_fila = aux.anterior
                fim_fila.proximo = None

            else:
                aux.anterior.proximo = aux.proximo
                aux.proximo.anterior = aux.anterior

            return fila, fim_fila

        aux = aux.proximo

    print("Jogador não encontrado")
    return fila, fim_fila

def simular_rodada(fila, fim_fila):
    if fila is None:
        print("Fila vazia")
        return fila, fim_fila

    primeiro = fila

    print("Jogador da rodada:", primeiro.jogador)

    if fila == fim_fila:
        return fila, fim_fila

    fila = fila.proximo
    fila.anterior = None

    fim_fila.proximo = primeiro
    primeiro.anterior = fim_fila
    primeiro.proximo = None
    fim_fila = primeiro

    return fila, fim_fila

def mostrar_fila(fila):
    if fila == None:
        print("Fila vazia")
        return

    aux = fila
    while aux != None:
        print(" - ", aux.jogador)
        aux = aux.proximo

def mostrar_proximo_a_jogar(fila):
    if fila == None:
        print("Fila vazia")
        return
    
    print(" - ", fila.jogador)

def limpar_fila(fila, fim_fila):
    if fila is None:
        print("Fila vazia")
        return None, None
    
    return None, None

def main():
    opcao = 0
    fila = fim_fila = None

    while opcao != 8:
        opcao = menu()

        if opcao == 1:
            jogador = str(input("Digite o nome do jogador que deseja adicionar na fila:"))
            fila, fim_fila = adicionar_jogador(fila, fim_fila, jogador)

        elif opcao == 2:
            jogador = str(input("Digite o nome do jogador que deseja remover da fila:"))
            fila, fim_fila = remover_jogador(fila, fim_fila, jogador)

        elif opcao == 3:
            fila, fim_fila = simular_rodada(fila, fim_fila)

        elif opcao == 4:
            rodadas = int(input("Digite o número de rodadas: "))
            for i in range(rodadas):
                print("Rodada", i+1)
                fila, fim_fila = simular_rodada(fila, fim_fila)
                mostrar_fila(fila)

        elif opcao == 5:
            mostrar_fila(fila)

        elif opcao == 6:
            mostrar_proximo_a_jogar(fila)

        elif opcao == 7:
            fila, fim_fila = limpar_fila(fila, fim_fila)
        
        elif opcao == 8:
            return

        else:
            print("Opção inválida")

main()