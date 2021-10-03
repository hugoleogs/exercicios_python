"""
Utilizando bloco with para ler e escrever

(Exemplo1)
with open('text1') as arquiv:
    print(arquiv.read())

(Exemplo2)
with open('text1') as arquiv:

    arquivo = arquiv.readlines()
    for i in arquivo:
        print(i)

(Exemplo3)
with open('text1', 'w') as arqui:
    arqui.write('Eu sou de jesus...\n')
    arqui.write("Eu amo jesus.\n")
    arqui.write("eu amo meu espirito santo!")

"""
with open('text1', 'w') as arquivo:
    entrada =''
    while entrada != 'sair':
        entrada = input('Digitem um item da feira que falta: ')
        if entrada != 'sair':
            arquivo.write(f'{entrada} \n')
print("fim lista de feira")