"""
A list is positive dominant if it contains strictly more unique positive values than unique negative values.

Write a function that returns true if a list is positive dominant.
Examples

[1, 1, 1, 1, -3, -4] ➞ false
# there is only 1 unique positive value (1)
# there are 2 unique negative values (-3, -4)

[5, 99, 832, -3, -4] ➞ true

[5, 0] ➞ true

[0, -4, -1] ➞ false

print(is_positive_dominant([5, 4, 3, 0, 0, -1, -1, -2, -2]), True)

print(is_positive_dominant([52, 52, 52, -3, 2, 2, 2, -4]), False)

print(is_positive_dominant([3, 3, 3, 3, -1, -1, -1]), False)

print(is_positive_dominant([1, 0, 0, -1]), False)

Notes

0 neither counts as a positive nor a negative value.

"""
#Uma segunda forma
#def is_positive_dominant(lst):
#  return sum(1 if i>0 else -1 if i<0 else 0 for i in set(lst))>0

def is_positive_dominant(lst):
    return (len(list(filter(lambda x: x > 0, set(lst)))) > len(list(filter(lambda x: x < 0, set(lst)))))


print(is_positive_dominant([1, 1, 1, 1, -3, -4]))

print(is_positive_dominant([5, 99, 832, -3, -4]))

print(is_positive_dominant([5, 0]))

print(is_positive_dominant([0, -4, -1]))

print(is_positive_dominant([5, 4, 3, 0, 0, -1, -1, -2, -2]))

print(is_positive_dominant([52, 52, 52, -3, 2, 2, 2, -4]))

print(is_positive_dominant([3, 3, 3, 3, -1, -1, -1]))

print(is_positive_dominant([1, 0, 0, -1]))
