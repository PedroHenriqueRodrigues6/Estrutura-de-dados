from collections import deque

def adicionar_inicio(fila):
    nome = input("Nome do viajante: ")
    fila.appendleft(nome)

def adicionar_final(fila):
    nome = input("Nome do viajante: ")
    fila.append(nome)

def enviar_inicio(fila):
    if len(fila) == 0:
        print("A fila está vazia.")
    else:
        print(f"Viajante enviado para a missão: {fila.popleft()}")

def enviar_final(fila):
    if len(fila) == 0:
        print("A fila está vazia.")
    else:
        print(f"Viajante enviado para a missão: {fila.pop()}")

def apresentar_fila(fila):
    if len(fila) == 0:
        print("A fila está vazia.")
    else:
        print("Fila de viajantes:")
        for viajante in fila:
            print(viajante)

fila = deque()

while True:
    print("\n1 - Adicionar viajante no início da fila")
    print("2 - Adicionar viajante no final da fila")
    print("3 - Enviar viajante do início para a missão")
    print("4 - Enviar viajante do final para a missão")
    print("5 - Apresentar fila de viajantes")
    print("6 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        adicionar_inicio(fila)
    elif opcao == 2:
        adicionar_final(fila)
    elif opcao == 3:
        enviar_inicio(fila)
    elif opcao == 4:
        enviar_final(fila)
    elif opcao == 5:
        apresentar_fila(fila)
    elif opcao == 6:
        print("Encerrando...")
        break
    else:
        print("Opção inválida.")
