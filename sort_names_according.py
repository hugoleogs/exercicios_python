"""
Sort Names According to the Length of Their Last Names
Create a function that takes a list of names in the format "First Name Last Name" (e.g. "John Doe"), and returns a list of these names sorted by the length of their last names. If the length of multiple last names are the same, then proceed to sort alphabetically by last name.

Examples
last_name_lensort([
  "Jennifer Figueroa",
  "Heather Mcgee",
  "Amanda Schwartz",
  "Nicole Yoder",
  "Melissa Hoffman"
]) ➞ ["Heather Mcgee", "Nicole Yoder", "Melissa Hoffman", "Jennifer Figueroa", "Amanda Schwartz"]
Notes
If last names are of the same length, sort alphabetically by last name.

URL: https://edabit.com/challenge/kS8tfJD2ggohQbWx7

"""
# list_name = ["Hitagi Senjougahara","Edward Elric","Light Yagami","Rintaro Okabe","Kurisu Makise"]
list_name = [
    "Jennifer Figueroa",
    "Heather Mcgee",
    "Amanda Schwartz",
    "Nicole Yoder",
    "Melissa Hoffman"
]  # ["Heather Mcgee", "Nicole Yoder", "Melissa Hoffman", "Jennifer Figueroa", "Amanda Schwartz"]


def last_name_lensort(list_names):
    aux = sorted(list_names, key=lambda x: (len(x.split()[1]), x.split()[1]))
    return aux


print(last_name_lensort(list_name))
