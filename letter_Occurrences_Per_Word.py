"""
Letter Occurrences Per Word

Create a function that takes in a sentence and a character to find. Return a dictionary of each word in the sentence, with the number of the specified character as the value.
Examples

find_occurrences("Hello World", "o") ➞ {
  "hello" : 1,
  "world" : 1
}

find_occurrences("Create a nice JUICY function", "c") ➞  {
  "create" : 1,
  "a" : 0,
  "nice" : 1,
  "juicy" : 1,
  "function" : 1
}

find_occurrences("An APPLE a day keeps an Archeologist AWAY...", "A") ➞ {
  "an" : 1,
  "apple" : 1,
  "a" : 1,
  "day" : 1,
  "keeps" : 0,
  "archeologist" : 1,
  "away..." : 2
}

Notes

    The function shouldn't be case sensitive.
    Words in the dictionary should be in lowercase.
    You may be required to find punctuation.
    Duplicate words should be ignored (see example #3 for the word "an").

URL: https://edabit.com/challenge/gA9dpoanWY6StiKR9
"""


def find_occurrences(txt, ch):
    return {(i.lower()): (i.lower().count(ch.lower())) for i in txt.split()}


#    return txt.split()[0].count(ch)


print(find_occurrences("Hello World", "o"))

print(find_occurrences("Create a nice JUICY function", "c"))

print(find_occurrences("An APPLE a day keeps an Archeologist AWAY...", "A"))
