'''
Author: Taylor Cochran
Book: Effective Python
Ch2

Goal:
  To understand what it means to be "defenseive when iterating" over args
'''

# a 'normalizer' function
#  sums the total, then divids the each city's amount by the total
# getting a percentage of participation

def normalize(numbers):
  total = sum(numbers)
  result = []
  for value in numbers:
    percent = 100 * value / total
    result.append(percent)
  return result

visits = [15, 35, 80]
percentages = normalize(visits)
# print(percentages)

# now we convert the data into a generator to allow for large data sets

def read_visits(data_path):
  with open(data_path) as f:
    for line in f:
      yield int(line)

# unfortunetly this returns an incorrect result
it = read_visits("my_numbers.txt")
percentages = normalize(it)
# print(percentages)

it = read_visits("my_numbers.txt")
# print(list(it)) # exausts the results
# print(list(it)) # has nothing to return


# keep a copy of the generator has a list
# this runs into problems with large data sets
def normalize_copy(numbers):
  numbers = list(numbers) # list copy
  total = sum(numbers)
  result = []
  for value in numbers:
    percent = 100 * value / total
    result.append(percent)
  return result


# the solution is to accpet a function that returns an iterator 
def normalize_func(get_iter):
  total = sum(get_iter()) # exaushts the first iter
  result = []
  for value in get_iter(): # gets a new one
    percent = 100 * value / total
    result.append(percent)
  return result

# pass in a lamda function to call a new instance of the generator each time
path = 'my_numbers.txt'
percentages = normalize_func(lambda: read_visits(path))
# print(percentages)




# lambda is considered noisy
# instead utalize the __iter__ protacal in a container class

class ReadVisits(object):
  def __init__(self, data_path):
    self.data_path = data_path

  def __iter__(self): # allows for the creation of multiple iter objects
    with open(self.data_path) as handle:
      for line in handle:
        yield int(line)


visits = ReadVisits(path)
percentages = normalize(visits)
# print(percentages)



# now we can test for iters 
# ensuring only container objects are passed 
def noramalize_defensive(numbers):
  if iter(numbers) is iter(numbers): # An iterator -- bad!
    raise TypeError("Must supply a container object!")
  total = sum(numbers)
  result = []
  for value in numbers:
    percent = 100 * value / total
    result.append(percent)
  return result

it = iter(visits)
noramalize_defensive(it)

























