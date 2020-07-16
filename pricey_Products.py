"""
Pricey Products

You will be given a dictionary with various products and their respective prices. Return a list of the products with a minimum price of 500 in descending order.
Examples

pricey_prod({"Computer" : 600, "TV" : 800, "Radio" : 50}) ➞ ["TV", "Computer"]

pricey_prod({"Bike1" : 510, "Bike2" : 401, "Bike3" : 501}) ➞ ["Bike1", "Bike3"]

pricey_prod({"Loafers" : 50, "Vans" : 10, "Crocs" : 20}) ➞ []

Notes

N/A

URL: https://edabit.com/challenge/SxevRSmRcshgwnAKp
"""

pricey_prod = lambda d: list(
    map(lambda y: y[0], filter(lambda x: x[1] >= 500, sorted(d.items(), key=lambda i: i[1], reverse=True))))

print(pricey_prod({"Computer": 600, "TV": 800, "Radio": 50}))

print(pricey_prod({"Bike1": 510, "Bike2": 401, "Bike3": 501}))

print(pricey_prod({"Loafers": 50, "Vans": 10, "Crocs": 20}))
