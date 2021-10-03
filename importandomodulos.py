"""
Codigo para aprendizado de importação de codigos python

"""
"""
import pacote_opera as pacote

print(f"A soma eh {pacote.soma(3, pacote.pi)}")

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"a soma da lista eh {pacote.somalist(list1)}")

string = ['h', 'u', 'g', 'o']

print("transformando lista em string: {}".format(pacote.listTostring(string)))

print("impar: {} e os pares: {}".format(pacote.impares(list1), pacote.pares(list1)))

stringnomes = ["hugo leonardo gomes da silva", "sheyla leal de souza melo", "jesse pereira da silva", "Erica maria pereira da silva melo"]

print("os sobrenomes sao: {}".format(pacote.printsobrenome(stringnomes)))

"""

"""

from pacote_opera import *

print(f"A soma eh {soma(3, pi)}")

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"a soma da lista eh {somalist(list1)}")

string = ['h', 'u', 'g', 'o']

print("transformando lista em string: {}".format(listTostring(string)))

print("impar: {} e os pares: {}".format(impares(list1), pares(list1)))

stringnomes = ["hugo leonardo gomes da silva", "sheyla leal de souza melo", "jesse pereira da silva", "Erica maria pereira da silva melo"]

print("os sobrenomes sao: {}".format(printsobrenome(stringnomes)))

"""

