class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def calcular_bonus(self):
        anterior = self.salario

        if self.cargo == "Gerente":
            self.salario *= 0.10
            anterior += self.salario

            return anterior
        
        else:
            self.salario *= 0.05
            anterior += self.salario

            return anterior

funcionario1 = Funcionario("Roger", 100, "Gerente")
funcionario2 = Funcionario("Cleiton", 100, "Vendedor")

print("Salário atualizado com bônus:", funcionario1.calcular_bonus())
print("Salário atualizado com bônus:", funcionario2.calcular_bonus())