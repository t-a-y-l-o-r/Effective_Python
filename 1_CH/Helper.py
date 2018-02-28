'''
Author: Taylor Cochran
Book: Effective Python
Chapter: 1 - Helper Functions

This script is a basic example of a helper function.
The goal is to use a function instead of complex expression
'''

from urllib.parse import parse_qs

# base idea
my_values = parse_qs('red=5&blue=0&green=',
                    keep_blank_values=True)

# okay representation
print(repr(my_values))

# more complex
print('Red:   ', my_values.get('red'))
print('Blue:  ', my_values.get('blue'))
print('Green:  ', my_values.get('green'))

# even more complex
red = my_values.get('red', ['']) or 0
blue = my_values.get('blue', ['']) or 0
green = my_values.get('green', ['']) or 0
print('Red:    %r' % red)
print('Blue:   %r' % blue)
print('Green:   %r' % green)

# even worse yet
red = int(my_values.get('red', [''])[0] or 0)
print('Red:      %r' % red)


# helper function
def get_first_int(values, key, default=0):
  '''
  Takes the past list of values. Looks for the key inside the list.
  Converts the resulting value to an integer
  '''
  found = values.get(key, [''])
  if found[0]:
    found = int(found[0])
  else:
    found = default
  return found

# best yet
red = get_first_int(my_values, 'red')
blue = get_first_int(my_values, 'blue')
green = get_first_int(my_values, 'green')
print('Red:      %r' % red)
print('Blue:     %r' % blue)
print('Green:    %r' % green)

















