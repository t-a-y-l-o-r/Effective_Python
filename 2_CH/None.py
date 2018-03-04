'''
Author: Taylor Cochran
Book: Effective Python
Ch2

Goal:
  To learn why preferring exceptions to returning None is better
'''

# temptation
def divide(a, b):
  try:
    return a / b
  except ZeroDivisionError:
    return None
x, y = 1, 2

result = divide(x, y)
if result is None: # breaks down when result is 0
  print("Invalid input")

x, y = 0, 5
result = divide(x, y)
if not result: # doesn't work with 0/y
  print("Invalid input")

# returning None is error prone

# solution 1: return a tuple
# success/failure, result
# this can lead to users ignoring the other result
def divide(a, b):
  try:
    return True, a / b
  except ZeroDivisionError:
    return False, None

# improper use of above
_, result = divide(x, y)
if not result:
  print("Invalid input!") # wrong


# The 2nd and best way is to simply raise an exception
def divide(a, b):
  try:
    return a / b
  except ZeroDivisionError as e:
    raise ValueError("Invalid inputs!") from e

# this allows for clear usage


x, y = 5, 2
try:
  result = divide(x, y)
except ValueError:
  print("Invalid input!")
else:
  print("Result is %.1f" % result)











