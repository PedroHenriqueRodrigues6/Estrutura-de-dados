class No:
    def __init__(self, id, musica, artista, duracao):
        self.id = id
        self.musica = musica
        self.artista = artista
        self.duracao = duracao
        self.proximo = None
        self.anterior = None

def adicionar_musica(lista, id, musica, artista, duracao):
    novo = No(id, musica, artista, duracao)

    if lista == None:
        lista = novo
        return lista
    
    lista.anterior = novo
    novo.proximo = lista
    lista = novo
    return lista

def listar_musicas(lista):
    aux = lista

    if aux == None:
        print("Playlist vazia")
        return

    while aux != None:
        print("------------------------------------",
              "\nID", aux.id,
              "\nNome:", aux.musica,
              "\nArtista:", aux.artista,
              "\nDuração (em minutos):", aux.duracao,
              "\n------------------------------------")
        aux = aux.proximo

def remover_musica(lista, musica):
    aux = lista

    while aux is not None:

        if aux.musica == musica:
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
    
    print("Música não encontrada")
    return lista

def buscar_musica(lista, opc2, aux2):
    aux = lista

    if aux == None:
        print("Playlist vazia")
        return

    if opc2 == 1:
        while aux is not None:
            if aux2 == aux.musica:
                print("------------------------------",
                      "\nID:", aux.id,
                      "\nNome:",aux.musica,
                      "\nArtista:", aux.artista,
                      "\nDuração:", aux.duracao,
                      "\n------------------------------")
                return
            aux = aux.proximo

    elif opc2 == 2:
        while aux is not None:
            if aux2 == aux.artista:
                print("------------------------------",
                      "\nID:", aux.id,
                      "\nNome:",aux.musica,
                      "\nArtista:", aux.artista,
                      "\nDuração:", aux.duracao,
                      "\n------------------------------")
                return
            aux = aux.proximo

    if opc2 == 1:
        print("Música não encontrada")
    
    elif opc2 == 2:
        print("Artista não encontrado")

def mostrar_duracao(lista):
    aux = lista
    duracao_total = 0

    if aux == None:
        print("Playlist vazia")
        
    while aux is not None:
        duracao_total += aux.duracao
        aux = aux.proximo

    print("Duração total da playlist:", duracao_total)

def alterar_musica(lista):
    aux = lista
    opc = 0

    if aux == None:
        print("Playlist vazia")
        return
    else:
        print("Música atual:", aux.musica)

    print("1 - Avançar para a próxima música")
    print("2 - Voltar para a música anterior")
    print("3 - Pausar a música")
    opc = int(input("Digite uma opção:"))

    while opc != 3:
        if opc == 1:
            if aux.proximo is not None:
                aux = aux.proximo
                print("-------\n",
                      aux.musica,
                      "\n-------")  
            else:
                print("Última música da playlist")

        elif opc == 2:
            if aux.anterior is not None:
                aux = aux.anterior
                print("-------\n",
                      aux.musica,
                      "\n-------")
            else:
                print("Primeira música da playlist")

        elif opc == 3:
            print("Música pausada")

        else:
            print("Opção inválida")
        
        opc = int(input("Digite uma opção:"))

def menu():
    print("1 - Adicionar música na playlist")
    print("2 - Listar todas as músicas")
    print("3 - Remover música")
    print("4 - Buscar música")
    print("5 - Mostrar a duração total da playlist")
    print("6 - Avançar para a próxima música / Voltar para a música anterior")
    print("7 - Sair")
    opc = int(input("Digite uma opção:"))
    return opc

def menu2():
    print("1 - Buscar por nome da música")
    print("2 - Buscar por nome do artista")
    opc2 = int(input("Digite uma opção:"))
    return opc2

def main():
    lista = None
    opc = 0
    opc2 = 0

    while opc != 7:
        opc = menu()
        
        if opc == 1:
            id = int(input("Digite o ID da música:"))
            musica = str(input("Digite o nome da música:"))
            artista = str(input("Digite o nome do artista:"))
            duracao = int(input("Digite a duração da música (em minutos):"))
            lista = adicionar_musica(lista, id, musica, artista, duracao)

        elif opc == 2:
            listar_musicas(lista)

        elif opc == 3:
            musica = str(input("Digite o nome da música:"))
            lista = remover_musica(lista, musica)

        elif opc == 4:
            opc2 = menu2()
            if opc2 == 1:
                aux2 = str(input("Digite o nome da música:"))
                buscar_musica(lista, opc2, aux2)

            elif opc2 == 2:
                aux2 = str(input("Digite o nome do artista:"))
                buscar_musica(lista, opc2, aux2)

            else:
                print("Opção inválida")

        elif opc == 5:
            mostrar_duracao(lista)

        elif opc == 6:
            alterar_musica(lista)

        elif opc == 7:
            break

        else:
            print("Opção inválida")

main()