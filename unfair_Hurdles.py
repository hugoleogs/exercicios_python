"""
Unfair Hurdles

Unfair hurdles are hurdles which are either too high, or way too close together.

Create a function which takes in a list of strings, representing hurdles, and return whether they are unfair. For the purposes of this challenge, unfair hurdles are:

    At least 4 characters tall.
    Strictly less than 4 spaces apart.

Examples

# Hurdle are good distance apart but are way too tall.

is_unfair_hurdle([
  "#    #    #    #",
  "#    #    #    #",
  "#    #    #    #",
  "#    #    #    #"
]) ➞ True


# Hurdles are a fine height but are way too close together.

is_unfair_hurdle([
  "#  #  #  #",
  "#  #  #  #",
  "#  #  #  #"
]) ➞ True


# These hurdles are mighty splendid.

is_unfair_hurdle([
  "#      #      #      #",
  "#      #      #      #"
]) ➞ False

Notes

    Hurdles will be represented with a hashtag "#".
    There will be the same spacing between hurdles.

URL: https://edabit.com/challenge/dqJYvDRTyXzQPGimc

"""

def is_unfair_hurdle(hurdles):
    if (len(hurdles) >= 4):
        saida = True
    elif (len(hurdles[0].split('#')[1]) < 4):
        saida = True
    else:
        saida = False
    return saida

print(is_unfair_hurdle([
  "#    #    #    #",
  "#    #    #    #",
  "#    #    #    #",
  "#    #    #    #"
]))

print(is_unfair_hurdle([
  "#  #  #  #",
  "#  #  #  #",
  "#  #  #  #"
]))

print(is_unfair_hurdle([
  "#      #      #      #",
  "#      #      #      #"
]))
