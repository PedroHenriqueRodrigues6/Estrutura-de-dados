def soma_temperaturas(array, tamanho, indice):
    if indice == tamanho:
        return 0
    else:
        return array[indice] + soma_temperaturas(array, tamanho, indice + 1)


def exibir_caixas(n):
    if n == 1:
        print(1)
    else:
        print(n)
        exibir_caixas(n - 1)


temperaturas = [25, 28, 22, 30, 27]

soma = soma_temperaturas(temperaturas, len(temperaturas), 0)
media = soma / len(temperaturas)

print("Média das temperaturas:", media)

quantidade = int(input("Digite a quantidade de caixas: "))

print("Caixas do topo até a base:")
exibir_caixas(quantidade)