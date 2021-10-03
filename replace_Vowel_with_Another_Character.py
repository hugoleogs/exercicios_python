"""
Replace Vowel with Another Character

Create a function that takes a string and replaces the vowels with another character.

    a = 1
    e = 2
    i = 3
    o = 4
    u = 5

Examples

replaceVowel("karachi") ➞ "k1r1ch3"

replaceVowel("chembur") ➞ "ch2mb5r"

replaceVowel("khandbari") ➞ "kh1ndb1ri"

Notes

The input will always be in lowercase.
"""

def replaceVowel(word):
    vet_teste = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
    for letra in vet_teste.keys():
        word = word.replace(letra, str(vet_teste[letra]))
    return word


print(replaceVowel("karachi"))

print(replaceVowel("chembur"))

print(replaceVowel("khandbari"))