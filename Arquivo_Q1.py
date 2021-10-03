"""

Escreva um programa que:

(a) Criar/abrir um arquivo texto de nome "arq.txt"

(b) Permitir que o usuario grave diversos caracteres, ate que entre com zero

(c) Feche o arquivo

Printar caracter por caracter.

"""

arquivo = open("arq.txt", "w")

entrada = "a"

while entrada != "0":

    entrada = input("Digite a entrada: ")
    arquivo.write(entrada + '\n')


arquivo.close()

arquivo = open("arq.txt", "r")

entrada = 'a'

while entrada != "0":

    entrada = arquivo.read(1)
    print(entrada)

