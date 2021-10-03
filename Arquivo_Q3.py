"""

Receber um arquivo texto e mostrar quantas são vogais

"""

entrada = input("Favor digite o arquivo Texto: ")

arquiv = open(entrada, 'r')

text = arquiv.read()

soma = 0

for letra in text:

    for vog in ['a', 'e', 'i', 'o', 'u']:

        if letra == vog:

            soma = soma + 1

print(f"O arquivo possuí {soma} vogais ")

arquiv.close()