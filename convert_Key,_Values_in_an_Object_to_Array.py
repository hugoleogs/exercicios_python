"""
Convert Key, Values in a Dictionary to List

Write a function that converts a dictionary into a list of keys-values tuples.
Examples

dict_to_list({
  "D": 1,
  "B": 2,
  "C": 3
}) ➞ [("B", 2), ("C", 3), ("D", 1)]

dict_to_list({
  "likes": 2,
  "dislikes": 3,
  "followers": 10
}) ➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]

Notes

Return the elements in the list in alphabetical order.

URL: https://edabit.com/challenge/cMyMt377ReBsoTHnz

"""

dict_to_list = lambda d: sorted([(k, v) for k, v in d.items()])

print(f'A Lista desejada eh: {dict_to_list({"likes": 2, "dislikes": 3, "followers": 10})}')


print(f'A Lista desejada eh: {dict_to_list({"D": 1, "B": 2, "C": 3})}')