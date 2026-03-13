class Aluno:
    def __init__(self, nome, frequencia, media_geral):
        self.nome = nome
        self.frequencia = frequencia
        self.media_geral = media_geral

joao = Aluno("João", 76, 7.8)
maria = Aluno("Maria", 80, 8.5)

print("Nome do aluno:", joao.nome, "Frequência:", joao.frequencia, "Média geral:", joao.media_geral)
print("Nome do aluno:", maria.nome, "Frequência:", maria.frequencia, "Média geral:", maria.media_geral)
