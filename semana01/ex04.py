class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

pedro = Contato("Pedro", 111111111, "pedro@email.com")
joao = Contato("João", 222222222, "joao@email.com")
paulo = Contato("Paulo", 333333333, "paulo@email.com")

agenda = [pedro, joao, paulo]

for i in range(3):
    print("Nome:", agenda[i].nome, "Telefone:", agenda[i].telefone, "E-mail:", agenda[i].email)