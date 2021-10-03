"""

Receber um arquivo texto e mostrar na tela quantos arquivos o mesmo possui

"""

entrada = input("favor digite o nome do arquivo: ")

arquiv = open(entrada, 'r')

dados = arquiv.readlines()

print(f"A quantidade de Linhas é {len(dados)}")

arquiv.close()

