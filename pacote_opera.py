"""
Pacote para importar operações basicas.

"""

def soma(ent1, ent2):
    return ent1+ent2


def somalist(ent):
    return sum(ent)


def listTostring(ent):
    return ''.join(ent)


def printsobrenome(ent):
    saida = ''
    for x in ent:
        saida = saida + ' ' + x.split()[-1]
    return saida

def pares(ent):

    return [numero for numero in ent if numero % 2 == 0]


def impares(ent):

    return [numero for numero in ent if numero % 2 != 0]


pi = 3.1415