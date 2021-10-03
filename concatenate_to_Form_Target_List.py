"""
Concatenate to Form Target List

Create a function that returns True if smaller lists can concatenate to form the target list and False otherwise.
Examples

canConcatenate([[1, 2, 3, 4], [5, 6], [7]], [1, 2, 3, 4, 5, 6, 7]) ➞ True

canConcatenate([[2, 1, 3], [5, 4, 7, 6]], [7, 6, 5, 4, 3, 2, 1]) ➞ True

canConcatenate([[2, 1, 3], [5, 4, 7, 6, 7]], [1, 2, 3, 4, 5, 6, 7]) ➞ False
# Duplicate 7s not found in target list.

canConcatenate([[2, 1, 3], [5, 4, 7]], [1, 2, 3, 4, 5, 6, 7]) ➞ False
# Missing 6 from target list.

Notes

    Lists do not have to be sorted (see example #2).
    Lists should concatenate to create the final list exactly (see examples #3 and #4).

URL: https://edabit.com/challenge/23htQEtZobC8cfwcm

"""


def canConcatenate(arr, arr2):
    saida = []
    for i in arr:
        saida.extend(i)
    saida.sort()
    arr2.sort()
    return saida == arr2


print(canConcatenate([[1, 2, 3, 4], [5, 6], [7]], [1, 2, 3, 4, 5, 6, 7]))
print(canConcatenate([[2, 1, 3], [5, 4, 7, 6]], [7, 6, 5, 4, 3, 2, 1]))
print(canConcatenate([[2, 1, 3], [5, 4, 7, 6, 7]], [1, 2, 3, 4, 5, 6, 7]))
print(canConcatenate([[2, 1, 3], [5, 4, 7]], [1, 2, 3, 4, 5, 6, 7]))
