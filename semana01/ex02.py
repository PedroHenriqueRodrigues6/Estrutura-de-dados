class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

banana = Produto("banana", 10.99, 5)
abacate = Produto("abacate", 15.99, 3)

print("Produto:", banana.nome, "Preço:", banana.preco, "Quantidade:", banana.quantidade)
print("Produto:", abacate.nome, "Preço:", abacate.preco, "Quantidade:", abacate.quantidade)