def menu():
    print("1 - Inserir operação na pilha")
    print("2 - Retirar última operação da pilha")
    print("3 - Mostrar última operação inserida na pilha")
    print("4 - Mostrar todas as operações pendentes")
    print("5 - Sair")
    opcao = int(input("Digite a opção:"))
    return opcao

def inserir_operacao(pilha, operacao):
    pilha.append(operacao)
    return pilha

def remover_ultima_operacao(pilha):
    if not pilha:
        print("Pilha vazia")
        return pilha
    
    else:
        removido = pilha.pop()
        print("Removido:", removido)
        return pilha

def mostrar_ultima_operacao(pilha):
    if not pilha:
        print("Pilha vazia")

    else:
        print("Topo da pilha:", pilha[-1])

def mostrar_pilha(pilha):
    if not pilha:
        print("Pilha vazia")

    else:
        print("Operações na pilha (topo primeiro):")
        for op in reversed(pilha):
            print(" -", op)

def main():
    pilha = []
    opcao = 0

    while opcao != 5:
        opcao = menu()

        if opcao == 1:
            operacao = str(input("Digite uma operação:"))
            pilha = inserir_operacao(pilha, operacao)

        elif opcao == 2:
            pilha = remover_ultima_operacao(pilha)

        elif opcao == 3:
            mostrar_ultima_operacao(pilha)

        elif opcao == 4:
            mostrar_pilha(pilha)

        elif opcao == 5:
            return

        else:
            print("Opção inválida")

main()
