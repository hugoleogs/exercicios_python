"""
A group of friends have decided to start a secret society. The name will be the first letter of each of their names, sorted in alphabetical order.

Create a function that takes in a list of names and returns the name of the secret society.
Examples

society_name(["Adam", "Sarah", "Malcolm"]) ➞ "AMS"

society_name(["Harry", "Newt", "Luna", "Cho"]) ➞ "CHLN"

society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]) ➞ "CJMPRR"
"""

def society_name(friends):
    friends = sorted(friends)
    saida = []
    for letra in friends:
        saida.append(letra[0])
    return (''.join(saida))






society_name(["Adam", "Sarah", "Malcolm"])

#society_name(["Harry", "Newt", "Luna", "Cho"])

#society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"])