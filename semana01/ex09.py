class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        media = 0
        for i in range(len(self.notas)):
            media += self.notas[i]

        media /= 3
        print("Nome:", self.nome, "\nMédia:", media)


aluno1 = Aluno("João", [5, 4, 6])
aluno2 = Aluno("Roberto", [7, 7, 7])
aluno3 = Aluno("Guilherme", [10, 9, 8])

turma = [aluno1, aluno2, aluno3]

for i in range(len(turma)):
    turma[i].calcular_media()