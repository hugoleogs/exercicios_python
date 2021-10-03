"""Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".

    If the number is a multiple of 3 the output should be "Fizz".
    If the number given is a multiple of 5, the output should be "Buzz".
    If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
    If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.

Examples

fizz_buzz(3) ➞ "Fizz"

fizz_buzz(5) ➞ "Buzz"

fizz_buzz(15) ➞ "FizzBuzz"

fizz_buzz(4) ➞ "4"

Notes

    Try to be precise with how you spell things and where you put the capital letters.
    If you get stuck on a challenge, find help in the Resources tab.
    If you're really stuck, unlock solutions in the Solutions tab.
"""

def fizz_buzz(num):
    if num % 3 == 0 and num % 5 != 0:
        return"Fizz"
    elif num % 5 == 0 and num % 3 != 0:
        return"Buzz"
    elif num % 3 == 0 and num % 5 == 0:
        return"FizzBuzz"
    else:
        return str(num)




fizz_buzz(3)
fizz_buzz(5)
fizz_buzz(15)
fizz_buzz(10)
fizz_buzz(98)
