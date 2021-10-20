"""
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]

"""


def unique_in_order(iterable):
    list_saida = []
    a = ''
    if iterable is list:
        for i in iterable:
            if a != i:
                list_saida.append(i)
                a = i
    else:
        for i in list(iterable):
            if a != i:
                list_saida.append(i)
                a = i
    return list_saida


print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))
