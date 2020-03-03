"""

Write a function that finds the sum of the first n natural numbers. Make your function recursive.
Examples

sum_numbers(5) ➞ 15
// 1 + 2 + 3 + 4 + 5 = 15

sum_numbers(1) ➞ 1

sum_numbers(12) ➞ 78

"""

def sum_numbers(n):
    soma = 0
    if n == 1:
        return 1
    else:
        soma = n + sum_numbers(n-1)

    return soma





print(sum_numbers(1))

print(sum_numbers(5))

print(sum_numbers(12))