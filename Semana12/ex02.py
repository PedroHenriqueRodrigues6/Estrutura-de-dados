def contagem_regressiva(numero):
    print(numero)

    if numero == 0:
        print("Viagem no tempo iniciada!")
    else:
        contagem_regressiva(numero - 1)

n = int(input("Digite um número inteiro positivo: "))
contagem_regressiva(n)