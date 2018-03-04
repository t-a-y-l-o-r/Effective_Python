'''
Author: Taylor Cochran
Book: Effective Python
Ch2

Goal:
  To learn about closures and variable scope
'''

# sort with a helper passed as an  argument
def sort_priority(values, group):
  def helper(x):
    ''' Sets priority based on group '''
    if x in group:
      return (0, x) 
    return (1, x)
    '''Uses the priority to sort the list'''
  values.sort(key=helper)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)


# now we attempt to integrate a flag to detect whether or not priority 
# items have been seen in the intial list
def sort_priority2(numbers, group):
  found = False # scope = sort_priotity2
  def helper(x):
    if x in group:
      found = True # scope = helper -> not what we want
      return (0, x)
    return (1, x)
  numbers.sort(key=helper)
  return found



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
group = {2, 3, 5, 7}
# but it doesn't work!
found = sort_priority2(numbers, group)
print("Found: ", found)
print(numbers)

 



# now we force scope traversal within the helper func
def sort_priority3(number, group):
  found = False # scope = sort_priority3
  def helper(x):
    nonlocal found # forces scope traversal
    if x in group:
      found = True # scope = sort_priority3
      return (0, x)
    return (1, x)
  numbers.sort(key=helper)
  return found



# in most instances it is safer and easier to read when the 
# effect is achieved with a helper function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

class Sorter(object):
  def __init__(self, group):
    self.group = group
    self.found = False

  def __call__(self, x):
    if x in self.group:
      self.found = True
      return (0, x)
    return (1, x)

sorter = Sorter(group)
numbers.sort(key=sorter)
assert sorter.found is True






























