"""
receber um arquivo texto, criar um segundo arquivo e trancrever o texto, modificando as vogais


"""
entrada = input("Digite o nome do arquivo de entrada: ")

with open(entrada, 'r') as arquivo:

    with open(entrada+'2', 'w') as arquivo2:

        text = arquivo.read()

        for letra in text:

            if letra.lower() in ['a', 'e', 'i', 'o', 'u']:

                arquivo2.write('*')

            else:

                arquivo2.write(letra)


