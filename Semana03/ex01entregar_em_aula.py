class No:
    def __init__(self, identificador, nome, nota_final):
        self.identificador = identificador
        self.nome = nome
        self.nota_final = nota_final
        self.proximo = None
        self.anterior = None

def inserir_nome(lista, identificador, nome, nota_final):
    novo = No(identificador, nome, nota_final)

    if lista == None:
        lista = novo
        return lista
    
    lista.anterior = novo
    novo.proximo = lista
    lista = novo
    return lista

def listar_alunos(lista):
    aux = lista

    if aux == None:
        print("Nenhum aluno cadastrado")

    while aux != None:
        print("Identificador(ID) do aluno:", aux.identificador,
              "\nNome do aluno:", aux.nome,
              "\nNota final do aluno:", aux.nota_final)
        aux = aux.proximo

def remover_aluno(lista, nome):
    aux = lista

    while aux is not None:

        if aux.nome == nome:
            if aux.proximo == aux.anterior == None:
                return None
            
            elif aux.anterior == None:
                lista = aux.proximo
                lista.anterior = None
                return lista
            
            elif aux.proximo == None:
                aux.anterior.proximo = None
                return lista

            else:
                aux.anterior.proximo = aux.proximo
                aux.proximo.anterior = aux.anterior
                return lista

        else:
            aux = aux.proximo
    
    print("Aluno não encontrado")
    return lista

def mostrar_situacao(lista):
    aux = lista

    if aux == None:
        print("Nenhum aluno cadastrado")
        
    while aux is not None:
        if aux.nota_final >= 7:
            print(aux.nome, "- Aprovado")

        elif aux.nota_final >= 4 and aux.nota_final <= 6.9:
            print(aux.nome, "- Exame")
        
        else:
            print(aux.nome, "- Reprovado")

        aux = aux.proximo

def menu():
    print("1 - Inserir aluno")
    print("2 - Listar alunos")
    print("3 - Remover aluno")
    print("4 - Mostrar situação dos alunos")
    print("5 - Sair")
    opc = int(input("Digite a opção:"))
    return opc

def main():
    lista = None
    opc = 0

    while opc != 5:
        opc = menu()
        
        if opc == 1:
            identificador = int(input("Digite o identificador(ID) do aluno:"))
            nome = str(input("Digite o nome do aluno:"))
            nota_final = float(input("Digite a nota final do aluno:"))
            lista = inserir_nome(lista, identificador, nome, nota_final)

        elif opc == 2:
            listar_alunos(lista)

        elif opc == 3:
            nome = str(input("Digite o nome do aluno:"))
            lista = remover_aluno(lista, nome)

        elif opc == 4:
            mostrar_situacao(lista)

main()
