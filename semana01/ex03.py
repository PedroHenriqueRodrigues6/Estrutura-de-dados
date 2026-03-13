class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        preco_total = self.preco * self.quantidade

        return preco_total

banana = Produto("banana", 10.99, 5)

print("Produto:", banana.nome, "Preço:", banana.preco, "Quantidade:", banana.quantidade)
print("Preço total:", banana.calcular_total())