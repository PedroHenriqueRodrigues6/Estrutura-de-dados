class Livro:
    def __init__(self, titulo, autor, numero_de_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_de_paginas = numero_de_paginas

    def verificar_tamanho_livro(self):
        if self.numero_de_paginas <= 100:
            print("Livro curto")
        
        else:
            print("Livro longo")

livro1 = Livro("Livro 1", "Fulano", 60)
livro2 = Livro("Livro 2", "Ciclano", 120)

livro1.verificar_tamanho_livro()
livro2.verificar_tamanho_livro()