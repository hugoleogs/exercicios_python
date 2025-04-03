"""
List of Multiples

Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num up to length.
Examples

list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]

list_of_multiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

list_of_multiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]

Notes

Notice that num is also included in the returned list.

URL: https://edabit.com/challenge/BuwHwPvt92yw574zB

"""

def list_of_multiples(a, b):
    return [a*x for x in range(1, b+1)]

print(f'a lista de saida eh {list_of_multiples(7, 5)}')

print(f'a lista de saida eh {list_of_multiples(12, 10)}')

print(f'a lista de saida eh {list_of_multiples(17, 6)}')