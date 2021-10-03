"""

Receber um arquivo texto e verificar quantas ocorrencias de cada caracter


"""

entrada = input("Digite o nome do arquivo de entrada: ")

with open(entrada, 'r') as arquivo:

    text = arquivo.read()

    base = set(text)
    base.discard(' ')
    base.discard('\n')

    for letra in base:

        print(f" A letra {letra} tem {text.count(letra)} ocorrencias")

