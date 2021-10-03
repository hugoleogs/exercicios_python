"""
Exercícios de Python - Seção 16

Questão 01

Class Pessoa

"""


class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def set_nome(self, nome):
        self.__nome = nome

    def set_idade(self, idade):
        self.__idade = idade

    def set_altura(self, altura):
        self.__altura = altura

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_altura(self):
        return self.__altura

    def print_tela(self):
        print(f"{self.get_nome()} tem {self.get_idade()} anos de idade com uma altura {self.get_altura()}")


class Agenda:

    def __init__(self):
        self.__lista_usuario = []

    def armazena_pessoa(self, nome, idade, altura):

        self.__lista_usuario.append(Pessoa(nome, idade, altura))

    def remover_pessoa(self, nome):
        for i in range(len(self.__lista_usuario)):
            if self.__lista_usuario[i].get_nome() == nome:
                del (self.__lista_usuario[i])
                print("Usuário removido com sucesso!")

    def buscar_pessoa(self, nome):
        for i in range(len(self.__lista_usuario)):
            if self.__lista_usuario[i].get_nome() == nome:
                print(f" Contato salvo na posição {i}")
                print("\n")

    def imprimir_agenda(self):
        for i in range(len(self.__lista_usuario)):
            print(self.__lista_usuario[i].get_nome())
            print(self.__lista_usuario[i].get_idade())
            print(self.__lista_usuario[i].get_altura())
            print("\n")

    def imprimir_pessoa(self, posicao):
                print(f" Contato salvo na posição {posicao}")
                print(self.__lista_usuario[posicao].get_nome())
                print(self.__lista_usuario[posicao].get_idade())
                print(self.__lista_usuario[posicao].get_altura())
                print("\n")


minha_agenda = Agenda()
entrada = ''

nome = input("Davor digite seu nome: ")
idade = int(input("Favor digite sua idade: "))
altura = float(input("Favor digite sua altura: "))

user1 = Pessoa(nome, idade, altura)

while entrada != 'sair':

    print("Digite sua intenção: ")

    print("1 - Alterar nome  \n"
          "2 - Alterar idade \n"
          "3 - Alterar altura \n"
          "4 - imprimir Pessoa \n"
          "5 - Salvar Contatos"
          "6 - Remover Contatos"
          "7 - Buscar Contatos"
          "8 - Imprimir Agenda"
          "9 - Imprimir Pessoa"
          "sair - Para sair do programa ")

    entrada = input()

    if entrada == '1':

        entrada2 = input("Digite o nome para alterar: ")

        user1.set_nome(entrada2)

    elif entrada == '2':

        entrada2 = input("Digite a idade para alterar: ")

        user1.set_idade(entrada2)

    elif entrada == '3':

        entrada2 = input("Digite a altura para alterar: ")

        user1.set_altura(entrada2)

    elif entrada == '4':

        user1.print_tela()

    elif entrada == '5':

        minha_agenda.armazena_pessoa(input("Favor digite o nome do contato: "), int(input("Favor digite a idade do contato: ")), float(input("Favor digite a altura do contato: ")))

    elif entrada == '6':

        minha_agenda.remover_pessoa(input("Favor digite o nome do contato que será removido: "))

    elif entrada == '7':

        minha_agenda.buscar_pessoa(input("Favor digite o nome do contato que vc deseja buscar: "))

    elif entrada == '8':

        minha_agenda.imprimir_agenda()

    elif entrada == '9':

        minha_agenda.buscar_pessoa(int(input("Favor digite a posição que esse contato encontra-se: ")))

    else:
        print("Opção Invalida! Favor Digite uma Opção: ")
