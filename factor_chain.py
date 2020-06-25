"""
Factor Chain

A factor chain is a list where each previous element is a factor of the next consecutive element. The following is a factor chain:

[3, 6, 12, 36]

# 3 is a factor of 6
# 6 is a factor of 12
# 12 is a factor of 36

Create a function that determines whether or not a list is a factor chain.
Examples

factor_chain([1, 2, 4, 8, 16, 32]) ➞ True

factor_chain([1, 1, 1, 1, 1, 1]) ➞ True

factor_chain([2, 4, 6, 7, 12]) ➞ False

factor_chain([10, 1]) ➞ False

Notes

N/A

"""


def factor_chain(lst):
    saida = True
    for i in range(1, len(lst)):
        if (lst[i]%lst[i-1]):
            saida = False
            break
    return saida



print(factor_chain([1, 2, 4, 8, 16, 32]))

print(factor_chain([1, 1, 1, 1, 1, 1]))

print(factor_chain([2, 4, 6, 7, 12]))

print(factor_chain([10, 1]))