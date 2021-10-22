"""
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

Requirements:

    There must be a function for each number from 0 ("zero") to 9 ("nine")
    There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
    Each calculation consist of exactly one operation and two numbers
    The most outer function represents the left operand, the most inner function represents the right operand
    Division should be integer division. For example, this should return 2, not 2.666666...:

eight(divided_by(three()))

URL: https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python
"""


def zero(a = -1):  # your code here
    if a == -1:
        return 0
    else:
        return int(eval(f'0{a}'))


def one(a = -1):  # your code here
    if a == -1:
        return 1
    else:
        return int(eval(f'1{a}'))


def two(a = -1):  # your code here
    if a == -1:
        return 2
    else:
        return int(eval(f'2{a}'))


def three(a = -1):  # your code here
    if a == -1:
        return 3
    else:
        return int(eval(f'3{a}'))


def four(a = -1):  # your code here
    if a == -1:
        return 4
    else:
        return int(eval(f'4{a}'))


def five(a = -1):  # your code here
    if a == -1:
        return 5
    else:
        return int(eval(f'5{a}'))


def six(a = -1):  # your code here
    if a == -1:
        return 6
    else:
        return int(eval(f'6{a}'))


def seven(a = -1):  # your code here
    if a == -1:
        return 7
    else:
        return int(eval(f'7{a}'))


def eight(a = -1):  # your code here
    if a == -1:
        return 8
    else:
        return int(eval(f'8{a}'))


def nine(a = -1):  # your code here
    if a == -1:
        return 9
    else:
        return int(eval(f'9{a}'))


def plus(a):  # your code here
    return f'+{a}'


def minus(a):  # your code here
    return f'-{a}'


def times(a):  # your code here
    return f'*{a}'


def divided_by(a):  # your code here
    return f'/{a}'


print(seven(times(five())))  # must return 35
print(four(plus(nine())))  # must return 13
print(eight(minus(three())))  # must return 5
print(six(divided_by(two())))  # must return 3
print(eight(divided_by(three()))) # must return 2
