"""
Poker Full House

Create a function that determines whether or not a player is holding a Full House in their hand. A hand is represented as a list of 5 cards. A full house is defined as a pair of cards and a three-of-a-kind.

To illustrate: ["A", "A", "A", "K", "K"] would be a Full House, since the player holds 3 aces and 2 kings.
Examples

is_full_house(["A", "A", "A", "K", "K"]) ➞ True

is_full_house(["3", "J", "J", "3", "3"]) ➞ True

is_full_house(["10", "J", "10", "10", "10"]) ➞ False

is_full_house(["7", "J", "3", "4", "2"]) ➞ False

Notes

N/A

URL: https://edabit.com/challenge/uugzpwJXKdiESZbjM

"""


def is_full_house(arr):
    saida = []
    for elem in set(arr):
        saida.append(arr.count(elem))
    return set(saida) == set([2, 3])


print(is_full_house(["A", "A", "A", "K", "K"]))

print(is_full_house(["3", "J", "J", "3", "3"]))

print(is_full_house(["10", "J", "10", "10", "10"]))

print(is_full_house(["7", "J", "3", "4", "2"]))
