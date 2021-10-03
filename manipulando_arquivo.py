"""
Esse modulo será dividido em três partes.

leitura, escrita e outros

(Exemplo1)
arquivo = open('text1')
print(arquivo.read())

(Exemplo2)
arquivo = open('text1')
print(arquivo.read())
print('\n')
arquivo.seek(28)
print(arquivo.read())

(Exemplo3)
arquivo = open('text1')
print(arquivo.readline(), end='')
print(arquivo.readline(), end='')
print(arquivo.readline(), end='')

(Exemplo4)
#Verifica quantas linhas o arquivo tem!
arquivo = open('text1')
tex = arquivo.readlines()
print(len(tex))

(Exemplo5)
#iterando sobre as linhas
arquivo = open('text1')
tex = arquivo.readlines()
for i in tex:
    print(i, end='')

(Exemplo6)
arquivo = open('text1')

tex = arquivo.readlines()

for i in tex:

    print(i, end='')

print(arquivo.closed)#verifica se o arquivo foi fechado!

arquivo.close()

print(arquivo.closed)#verifica se o arquivo foi fechado!


(Exemplo7)
arquivo = open('text1')

tex = arquivo.read(35) #limita a leitura em 35 caracteres

print(tex)


arquivo = open('text1', 'w')

arquivo.write('Deus te amo e preciso de ti mais...\n')
arquivo.write('eu nao sou nada sem ti\n')
arquivo.write('Deus me ajuda \n')

arquivo.close()


"""
