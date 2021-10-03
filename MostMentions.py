# PROBLEMA:
# Uma empresa de marketing digital trabalha monitorando avaliações conforme
# um conjunto de palavras-chaves fornecidas pelos seus clientes. Regularmente
# essa empresa reporta aos seus clientes quantas menções foram detectadas para
# cada palavra-chave, destacando a palavra-chave mais mencionada. Dada
# uma lista de postagens em redes sociais e uma lista de palavras-chaves,
# construa uma função que retorna a maior quantidade de vezes que
# uma palavra-chave é mencionada. Considere que uma menção é contabilizada
# quando uma palavra-chave aparece em uma postagem, independente de
# capitalização (maiúscula ou minúscula) e se aparece 1 ou mais vezes
# na mesma postagem.

# INPUT:
# - keywords = list(sr) - lista de palavra-chaves
# - posts = list(str) - lista de postagens em redes sociais;

# CONSTRAINTS:
# 0 < len(keywords) < 10000
# 0 < len(posts) < 10000

# OUTPUT:
# int - maior quantidade de menções de uma mesma palavra-chave

# EXEMPLO:
## INPUT:
## keywords = ['Magazine Luiza', 'Eletroshopping', "Habib's"]
## posts = ['A magazineluiza tá demais nessa black fraude!',
##          'A eletroshopping tá ganhando pra magazine luizAAAAA',
##          'A eletroshop tá se garantindo!',
##          'Habibs, aprenda com a magazine luiza a fazer promocao!']

## OUTPUT:
## 2

def mostMentions(keywords, posts):
    ## SEU CÓDIGO AQUI
    qtd_total = [] #Array da quantidade total de cada palavra chave

    for key in keywords:
        qtd = 0 # Quantidade de cada palavra chave nos posts
        for postagens in posts:

            qtd = qtd + postagens.lower().count(key.lower())

        qtd_total.append(qtd)

    print(max(qtd_total))



keywords = ['Magazine Luiza', 'Eletroshopping', "Habib's"]

posts = ['A magazineluiza tá demais nessa black fraude!',
         'A eletroshopping tá ganhando pra magazine luizAAAAA',
         'A eletroshop tá se garantindo!',
         'Habibs, aprenda com a magazine luiza a fazer promocao!']

mostMentions(keywords, posts)


