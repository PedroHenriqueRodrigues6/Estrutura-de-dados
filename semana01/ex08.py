class Aluno:
    def __init__(self, nome, lista):
        self.nome = nome
        self.lista = lista

    def calcular_media(self):
        total = 0
        for i in range(len(self.lista)):
            total += self.lista[i]
        
        media = total/len(self.lista)
        print("Média:", media)

        return media

    def verificar_aprovacao(self, media):
        if media >= 7:
            print("Aprovado")
        
        else:
            print("Reprovado")

aluno1 = Aluno("Pedro", [7, 7, 7])
aluno2 = Aluno("Rafael", [5, 7, 2])

media1 = aluno1.calcular_media()
media2 = aluno2.calcular_media()