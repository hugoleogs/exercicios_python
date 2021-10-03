"""

Receber um arquivo e contar as vogais e consoantes.


"""

entrada = input("Digite o nome do arquivo: ")

arquivo = open(entrada, 'r')

soma = soma2 = 0

for letra in arquivo.read():

    if letra.lower() in ['a', 'e', 'i', 'o', 'u']:

        soma = soma + 1

    elif letra.lower() in ['b','c','d','f','g','h','i','j','l','m','n','p','q','r','s','t','v','x','z']:

        soma2 = soma2 + 1


print(f"As quantidades respectivas de Vogais/Consoantes é {soma}/{soma2}")

arquivo.close()