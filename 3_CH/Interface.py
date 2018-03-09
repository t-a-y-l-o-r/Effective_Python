'''
Author: Taylor Cochran
Book: Effective Python
Chapter 3

Goal: Learn to accept functions for simple interfaces instead of classes
'''
from collections import defaultdict

# some api's allow "hook" functions to be passed as arguments
# in the case of the sort function it allows you to determine 
# how the sort is indexed
# this list is sorted by name length

names = ["Taylor", "Kyra", "Noah", "Cochran", "Teshima", "Miller"]
names.sort(key=lambda x: -len(x)) # -len() for largest to smallest
# print(names)

# most languages use abstract classes for hooks
# however has 'class-first' functions
# and as such they can be passed around just like variables
def log_message():
  print("Default created!")
  return 0

my_dict = {"green" : 12,
           "blue": 3}
increments = [
  ("red", 5),
  ("blue", 17),
  ("orange", 9),
]

# result = defaultdict(log_message, my_dict)
# print("Before:", dict(result))
# for key, value in increments:
#   result[key] += value
# print("After: ", dict(result))


# using hooks allows for the seperation of stateful behaviour and side effects
# counts to number of keys that were created/ missing
# this allows for additional functionality later on, due to stateful closures

def increment_with_report(current, increments):
  added_count = 0

  def missing():
    nonlocal added_count # STATEFUL CLOSURE
    added_count += 1
    return 0

  result = defaultdict(missing, current)
  for key, value in increments:
    result[key] += value

  return result, added_count

# result, count = increment_with_report(my_dict, increments)
# print("Added: %s \nDict: %s" % (str(count), str(dict(result))))


# the main downside to stateful behavoir inside of a hook
# is the reduced redability
# instead try encapsualting the state in a class

class CountMissing(object):
  def __init__(self):
    self.added = 0

  def missing(self):
    self.added += 1
    return self.added

# normally defaultdict would have to be modified to account for 
# countmissing's interface
# however this is not an issue with first-class functions, in python

counter = CountMissing()
result = defaultdict(counter.missing, my_dict) # Method reference

for key, value in increments:
  result[key] += value
assert counter.added == 2


# to clarify what exactly CountMissing is meant to do
# override __call__


my_dict = {"green" : 12,
           "blue": 3}
increments = [
  ("red", 5),
  ("blue", 17),
  ("orange", 9),
]

class BetterCountMissing(object):
  def __init__(self):
    self.added = 0

  def __call__(self):
    self.added += 1
    return 0

count = BetterCountMissing()
count()
assert callable(count)

# removed the need to call a function/instance vairable
count = BetterCountMissing() # make sure it hasn't been called before!
result = defaultdict(count, my_dict)
for key, value in increments:
  result[key] += value
assert count.added == 2













































