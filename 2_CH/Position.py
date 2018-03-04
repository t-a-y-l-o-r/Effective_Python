'''
Author: Taylor Cochran
Book: Effective Python
Ch1

Goal:
  To learn about variable positional arguments, 
    and how they facilitate noise reduction
'''


# start with a function that stores debug info
def log(message, values):
  if not values:
    print(message)
  else:
    values_str = ", ".join(str(x) for x in values)
    print("%s: %s" % (message, values_str))

# log("My numbers are", [1, 2])
# log("Hi there", [])

# use *arg to remove the need for empty arguments!
def log(message, *values): # values is now optional/ accepts any number of arguments
  if not values:
    print(message)
  else:
    values_str = ", ".join(str(x) for x in values)
    print("%s: %s" % (message, values_str))
# log("My numbers are", 1, 2)
# log("Hi there")


# using * on a list passed as an argument tells python to treat the list items
# as postional arguments
numbers = [7, 33, 99]
log("Farvorite numbers", *numbers)



# use * on argumetns forces the passed object to a tuple
# in the case of a generator this will exahust it, possibly eating all of your memory,
# and time
def my_generator():
  for i in range(10):
    yield i

def my_func(*args):
  print(args)

it = my_generator()
my_func(*it)


# additioanlly it is impossible to append to the accept args without breaking
# any code that calls the function
def log(sequence, message, *values):
  if not values:
    print("%s: %s" % (sequence, message))
  else:
    values_str = ", ".join(str(x) for x in values)
    print("%s: %s: %s" % (sequence, message, values_str))

log(1, "Favorites", 7, 33) # works
log("Favorites", 7, 33) # breaks in an unexpected manner

# to avoid this use keyword arguments to avoid this suple bugg propigation
# will cover in the next script













