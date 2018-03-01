'''
Author: Taylor Cochran
Book: Effective Python
Ch1

Goal:
  To learn about enumerate
'''
import random
# use range for sets of integers
random_bits = 0
for i in range(64):
  if random.randint(0, 1):
    random_bits |= 1 << i

# data structures can be iterated over directly
flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for flavor in flavor_list:
  # print("%s is delicious!" % flavor)
  break

# it is possible to use range to find the postion of each item
for i in range(len(flavor_list)):
  flavor = flavor_list[i]
  # print("%d: %s" % (i + 1, flavor))
  break

# prefer to use enumerate to create a lazy generator
for i, flavor in enumerate(flavor_list):
  # print("%d: %s" % (i+1, flavor))
  break

# it is possible to specifiy where enumerate should start counting
for i, flavor in enumerate(flavor_list, 1):
  print("%d: %s" % (i, flavor))