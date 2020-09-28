"""
The Frugal Gentleman

Atticus has been invited to a dinner party, and he decides to purchase a bottle of wine. However, he has little knowledge of how to choose a good bottle. Being a very frugal gentleman (yet disliking looking like a cheapskate), he decides to use a very simple rule. In any selection of two or more wines, he will always buy the second-cheapest.

Given a list of wine dictionaries, write a function that returns the name of the wine he will buy for the party. If given an empty list, return None. If given a list of only one, Atticus will buy that wine.
Examples

chosen_wine([
  { "name": "Wine A", "price": 8.99 },
  { "name": "Wine 32", "price": 13.99 },
  { "name": "Wine 9", "price": 10.99 }
]) ➞ "Wine 9"

chosen_wine([{ "name": "Wine A", "price": 8.99 }]) ➞ "Wine A"

chosen_wine([]) ➞ None

Notes

All wines will be different prices, so there is no confusion in the ordering.

URL: https://edabit.com/challenge/RWLWKmGcbp6drWgKB

"""
#list(filter(lambda x: x["price"] == , wines))
# min(map(lambda y: y["price"], wines))
#list(filter(lambda x: x["price"] > 10.99, wines))
# wines[0]["name"] if len(wines) == 0

def chosen_wine(wines):
    return list(filter(lambda a: a["price"] == min(map(lambda z: z["price"], filter(lambda x: x["price"] > min(map(lambda y: y["price"], wines)), wines))), wines))[0]["name"] if len(wines) >= 2 else None if len(wines) == 0 else wines[0]["name"]

print(chosen_wine([
  {"name": "Wine A", "price": 8.99},
  {"name": "Wine 32", "price": 13.99},
  {"name": "Wine 9", "price": 10.99}
]))

print(chosen_wine([{"name": "Wine A", "price": 8.99}]))

print(chosen_wine([{"name": "Wine C", "price": 9.99}, {"name": "Wine D", "price": 10.99}]))

print(chosen_wine([]))