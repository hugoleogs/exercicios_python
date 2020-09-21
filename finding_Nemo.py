"""
Finding Nemo

You're given a string of words. You need to find the word "Nemo", and return a string like this: "I found Nemo at [the order of the word you find nemo]!".

If you can't find Nemo, return "I can't find Nemo :(".
Examples

findNemo("I am finding Nemo !") ➞ "I found Nemo at 4!"

findNemo("Nemo is me") ➞ "I found Nemo at 1!"

findNemo("I Nemo am") ➞ "I found Nemo at 2!"

Notes

    ! , ? . are always separated from the last word.
    Nemo will always look like Nemo, and not NeMo or other capital variations.
    Nemo's, or anything that says Nemo with something behind it, doesn't count as Finding Nemo.
    If there are multiple Nemo's in the sentence, only return for the first one.

URL: https://edabit.com/challenge/c23dFfNiKbnguSQtq

"""


def find_nemo(entrada):
    return 'I found Nemo at {}!'.format(entrada.split().index("Nemo")+1) if ("Nemo" in entrada.split()) else "I can't find Nemo :("



print(find_nemo("I am finding Nemo !"))

print(find_nemo("Nemo is me"))

print(find_nemo("I Nemo am"))

print(find_nemo("I hugo am"))

print(find_nemo("Nemo is a clown fish, he has white and orange stripes. Nemo , come back!")) #I found Nemo at 1!

print(find_nemo("Is it Nemos, Nemona, Nemoor or Garfield?")) #I can't find Nemo :(

