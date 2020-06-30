"""
Converting Dictionaries to Lists

Write a function that converts a dictionary into a list, where each element represents a key-value pair.
Examples

to_list({ a: 1, b: 2 }) ➞ [["a", 1], ["b", 2]]

to_list({ shrimp: 15, tots: 12 }) ➞ [["shrimp", 15], ["tots", 12]]

to_list({}) ➞ []

Notes

Return an empty list if the dictionary is empty. Sort the list alphabetically by key.

URL: https://edabit.com/challenge/PgsQAdNvsEAkese8X

"""

def to_list(dct):
    saida = []
    for i, v in sorted((dct).items()):
        saida.append([i, v])
    return saida

print(to_list({'a': 1, 'b': 2}))
print(to_list({'foo': 33, 'bar': 45, 'baz': 67}))
print(to_list({'shrimp': 15, 'tots': 12}))

print(to_list({}))
