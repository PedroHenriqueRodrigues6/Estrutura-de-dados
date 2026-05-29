def contagem_regressiva(n):
    if n <= 1:
        print(1)
    else:
        print(n)
        contagem_regressiva(n - 1)


def pares(n):
    if n < 0:
        return
    else:
        pares(n - 1)
        if n % 2 == 0:
            print(n)


def soma_impares(n):
    if n <= 0:
        return 0
    else:
        if n % 2 != 0:
            return n + soma_impares(n - 1)
        else:
            return soma_impares(n - 1)


n = int(input("Digite um número: "))

print("\nContagem regressiva:")
contagem_regressiva(n)

print("\nNúmeros pares entre 0 e", n, ":")
pares(n)

print("\nSoma dos números ímpares de 1 até", n, ":")
print(soma_impares(n))
