"""
Vamos brincar com dicionarios e arquivos...

Criar uma lista de feira e depois um menu para editar a lista

"""
import os.path

print(" Seja bem vindo! Programa que ajuda a criar e editar sua lista de compras!")
entrada = ''
dici = {}
if os.path.exists('banco'):
    with open('banco') as ler:
        dici = dict(ler.read())

while entrada != '5':

    print("1 - Adicionar  2 - Apagar Item  3 - Qtd Item  4 - Imprimir  5 - Sair")

    entrada = input("Digite a sua opção: ")

    if(entrada != 'Sair'):

        if entrada == '1':

            adicionar = input("Digite o Item: ")
            qtd = input("Digite a quantidade do Item: ")

            dici[adicionar]=qtd

        elif entrada == '2':

            entrada = input("Digite o Item q Deseja remover: ")
            del dici[entrada]

        elif entrada == '3':

            entrada = input("Digite o Item que deseja apagar: ")
            print(f'A Quantidade desse produto eh: {dici[entrada]}')

        elif entrada == '4':

            print(dici)

        elif entrada == '5':

            with open('banco', 'w') as escrev:

                escrev.write(str(dici))
            print("Lista Finalizada com sucesso!")

        else:

            print("Opção Invalida! Escolha uma opção do Menu!")


