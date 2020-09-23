"""
Get Student with Best Test Avg.

Given a dictionary with students and the grades that they made on the tests that they took,
determine which student has the best Test Average. The key will be the student's name and the value will be a list of their grades.
You will only have to return the student's name. You do not need to return their Test Average.

Examples

get_best_student({
  "John": [100, 90, 80],
  "Bob": [100, 70, 80]
}) ➞ "John"

# John's avg = 90
# Bob's avg = 83.33

get_best_student({
  "Susan": [67, 84, 75, 63],
  "Mike": [87, 98, 64, 71],
  "Jim": [90, 58, 73, 86]
}) ➞ "Mike"

Notes

All students in a dictionary will have the same amount of test scores. So no student will have taken more tests than another.

URL: https://edabit.com/challenge/pnd7xPYuvogkNfHg6

"""

def get_best_student(grades):
    return max([(i, sum(b)/len(b)) for i, b in grades.items()], key=lambda x: x[1])[0]

print(get_best_student({
  "John": [100, 90, 80],
  "Bob": [100, 70, 80]
}))

print(get_best_student({
  "Susan": [67, 84, 75, 63],
  "Mike": [87, 98, 64, 71],
  "Jim": [90, 58, 73, 86]
}))