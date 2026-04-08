class Pacientes:
    def __init__(self, nome, idade, prioridade):
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade
        self.proximo = None
        self.anterior = None

def menu():
    print("1 - Inserir paciente na fila")
    print("2 - Remover paciente da fila")
    print("3 - Mostrar pacientes")
    print("4 - Simular atendimento")
    print("5 - Sair")
    opcao = int(input("Digite uma opção:"))
    return opcao

def inserir_paciente(lista, nome, idade, prioridade):
    novo = Pacientes(nome, idade, prioridade)

    if lista is None:
        novo.proximo = novo
        novo.anterior = novo
        lista = novo
        return lista

    lista.anterior.proximo = novo
    novo.anterior = lista.anterior
    lista.anterior = novo 
    novo.proximo = lista
    lista = novo
    return lista

def remover_paciente(lista, nome):
    aux = lista

    if lista is None:
        print("Nenhum paciente na fila")
        return None

    while True:

        if aux.nome == nome:
            if aux == aux.proximo == aux.anterior: 
                return None
            
            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

            if aux == lista:
                lista = lista.proximo
            return lista

        aux = aux.proximo
        if aux == lista:
            print("Paciente não encontrado")
            return lista

def mostrar_pacientes(lista):
    if lista is None:
        print("Nenhum paciente na fila")
        return

    aux = lista

    while True:
        print("Nome:", aux.nome)
        print("Idade:", aux.idade)
        print("Prioridade:", aux.prioridade)
        print("-------------------")
        aux = aux.proximo

        if aux == lista:
            break

def simular_atendimento(lista):
    if lista is None:
        print("Nenhum paciente na fila")
        return

    while lista is not None:
        prioridade_encontrada = None
        aux = lista

        while True:
            if aux.prioridade == "Emergência":
                prioridade_encontrada = aux
                break
            aux = aux.proximo
            if aux == lista:
                break
        
        if prioridade_encontrada is None:
            aux = lista
            while True:
                if aux.prioridade == "Urgente":
                    prioridade_encontrada = aux
                    break
                aux = aux.proximo
                if aux == lista:
                    break

        if prioridade_encontrada is None:
            prioridade_encontrada = lista

        print("Atendendo:", prioridade_encontrada.nome, "-", "Prioridade:", prioridade_encontrada.prioridade)

        lista = remover_paciente(lista, prioridade_encontrada.nome)

    print("Todos os pacientes foram atendidos!")
    return None

def main():
    lista = None
    opcao = 0

    while opcao != 5:
        opcao = menu()

        if opcao == 1:
            nome = str(input("Digite o nome do paciente:"))
            idade = int(input("Digite a idade do paciente:"))

            opc = 0
            print("1 - Emergência")
            print("2 - Urgente")
            print("3 - Normal")
            while opc == 0 or opc < 0 or opc > 3:
                opc = int(input("Escolha a prioridade:"))

            if opc == 1:
                prioridade = "Emergência"
            elif opc == 2:
                prioridade = "Urgente"
            else:
                prioridade = "Normal"
            
            lista = inserir_paciente(lista, nome, idade, prioridade)

        elif opcao == 2:
            nome = str(input("Digite o nome do paciente:"))
            lista = remover_paciente(lista, nome)

        elif opcao == 3:
            mostrar_pacientes(lista)

        elif opcao == 4:
            simular_atendimento(lista)

        elif opcao == 5:
            return

        else:
            print("Opção inválida")

main()