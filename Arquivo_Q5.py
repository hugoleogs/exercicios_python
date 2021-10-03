"""

Receber um arquivo e um caracter em seguida contar a quantidade de ocorrencia.


"""

entrada = input("Digite o nome do arquivo: ")
caracter = input("Digite o caracter que vc deseja pesquisar: ")

with open(entrada, 'r') as arquivo:

    string_arq = arquivo.read().lower()

    qtd = string_arq.count(caracter.lower())

    print(f"A quantidade de ocorrencia do caracter solicitado é {qtd}")