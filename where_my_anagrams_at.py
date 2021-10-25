"""
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false

Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

Note for Go
For Go: Empty string slice is expected when there are no anagrams found.
"""


def compara_palavra(palavra1, palavra2):
    for i in palavra2:
        if palavra1.count(i) == palavra2.count(i) and len(palavra1) == len(palavra2):
            saida = True
        else:
            saida = False
            break
    return saida


def anagrams(word, words):
    saida = filter(lambda x: compara_palavra(x, word), words)
    return list(saida)


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))  # ['aabb', 'bbaa']

print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))  # ['carer', 'racer']

print(anagrams('laser', ['lazing', 'lazy', 'lacer']))  # []

print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])) #['carer', 'racer']
