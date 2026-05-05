class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        print("Área:", self.largura * self.altura)

    def perimetro(self):
        print("Perímetro:", 2 * (self.largura + self.altura))

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar(self):
        print("Carro ligado!")

    def desligar(self):
        print("Carro desligado!")

p1 = Pessoa("Pedro", 20)
p2 = Pessoa("Maria", 25)

p1.apresentar()
p2.apresentar()

r = Retangulo(5, 3)
r.area()
r.perimetro()

c = Carro("Toyota", "Corolla", 2022)
c.ligar()
c.desligar()
