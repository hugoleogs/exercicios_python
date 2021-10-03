"""

Gerenciamento de agenda de contato.

"""
import ast

print("\n")
print("       Agenda de Contatos      ")
print("\n")


with open('arquivo.txt', '+r') as arquivo:

    base_dados = ast.literal_eval(arquivo.read())

    intencao = ''

    while intencao.lower() != 'sair':

        print("""
        (a) inserir contato \n 
        (b) remover contato \n
        (c) pesquisar um contato pelo nome \n
        (d)  listar todos os contatos \n
        (e)  listar os contatos cujo nome inicia com uma dada letra \n
        (f)  imprimir os aniversariantes do mês \n
        (sair) para sair!
        
        """)

        intencao = input("Digite a sua opção: ")

        if intencao == 'a':

            nome = input("Favor, Digite o nome que você deseja add: ")

            numero = input("Favor, Digite o numero: ")

            data = input("Favor, Digite o data no formato DD/MM/YYYY: ")

            base_dados[nome]=(numero, data)


        elif intencao == 'b':

            nome = input("Favor, Digite o nome que você deseja remover: ")

            retorno = base_dados.pop(nome, 'Usuário não encontrado! ')

            if retorno != 'Usuário não encontrado! ':

                print("Usuário Removido com sucesso!")

            else:

                print(retorno)

        elif intencao == 'c':

            nome = input("Favor, Digite o nome que você deseja pesquisar: ")

            saida = base_dados.get(nome, 'Usuário não encontrado! ')

            print(f'Contato de {nome} \n Numero: {saida[0]} \n data nascimento: {saida[1]}')

        elif intencao == 'd':

            print("\n")

            for contato in base_dados:

                saida = base_dados.get(contato)

                print(f'Contato de {contato} \n Numero: {saida[0]} \n data nascimento: {saida[1]}')

                print("\n")

        elif intencao == 'e':

            letra = input("Favor, Digite a letra que você deseja pesquisar: ")

            print("\n")

            for contato in base_dados:

                if letra in contato[0]:

                    saida = base_dados.get(contato)

                    print(f'Contato de {contato} \n Numero: {saida[0]} \n data nascimento: {saida[1]}')

                    print("\n")

        elif intencao == 'f':

            print("NÃO FIZ, DEU PREGUIÇA")

        elif intencao == 'sair':

            print("Adeus...")

        else:

            print("Favor digite uma das alternativas listadas!")

    arquivo.truncate(0)
    arquivo.seek(0)
    arquivo.write(str(base_dados))

""" 





   else:

       print('Opção Invalida, Digite novamente: ')


"""









