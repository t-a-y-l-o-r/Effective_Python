'''
Author: Taylor Cochran
Book: Effective Python
Ch1

Goal:
  To learn about generator expressions
'''


# use a list comprehension for small data sets!
value = [len(x) for x in open('my_file.txt')]
print(value)

# for larger data sets utilize a generator 
# to save memory
# by using () instead of []
gen = (len(x) for x in open('my_file.txt'))
print(gen)

# for x in gen:
#   print("%d, " % x, end='')
# print()


# it is possibile to string generators together
roots = ((x, x**0.5) for x in gen)
print(next(roots))