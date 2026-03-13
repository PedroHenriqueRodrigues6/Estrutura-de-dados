class Produto:
    def __init__(self, nome, preco, quantidade_em_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_em_estoque = quantidade_em_estoque

    def mostrar_estoque(self):
        print(self.nome, "Estoque atual:", self.quantidade_em_estoque)

    def atualizar_estoque(self, quantidade):
        self.quantidade_em_estoque += quantidade


teclado = Produto("Teclado", 50.00, 5)
mouse = Produto("Mouse", 20.00, 3)

teclado.mostrar_estoque()
mouse.mostrar_estoque()

valor_teclado = int(input("Digite o número de teclados: "))
valor_mouse = int(input("Digite o número de mouses: "))

teclado.atualizar_estoque(valor_teclado)
mouse.atualizar_estoque(valor_mouse)

print("Estoque atualizado:")
teclado.mostrar_estoque()
mouse.mostrar_estoque()