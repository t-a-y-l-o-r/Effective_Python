'''
Author: Taylor Cochran
Book: Effective Python
Ch: 2

goal: Learn about using None and Docstrings to specify dynamic default arguments
'''
import datetime
import time
import json

# let's log some data
# using a variable time stamp 
# this fails because default arguments are only defined once
def log(message, when=datetime.datetime.now()):
  print("%s: %s" % (when, message))

# log("Hi there")
# time.sleep(1)
# log("Hi again!")


# convention is to default to none
# then document the default behavior 
# the function body is run each time it is called, allowing for two time stamps!
def log(message, when=None):
  '''Log a message with a timestamp.

    Args:
        message: Message to print.
        when: datetime of when the message occured.
            Defaults to the present time.
  '''
  when = datetime.datetime.now() if when is None else when
  print("%s: %s" % (when, message))

log("Hi there!")
time.sleep(1)
log("Hi again!")


# none is especially prudent for mutable arguments
# this results in a single dictionary refrence
# pointed to by multiple variables
def decode(data, default={}):
  ''' Decodes the json data passed.

  Args:
      data: The data to be decoded
      default: a dictonary returned if the data can't be decoded,
        blank by default
  '''
  try:
    return json.loads(data)
  except:
    return default

# foo = decode('bad data')
# foo['stuff'] = 5
# bar = decode('also data')
# bar['meep'] = 1
# print("Foo:", foo)
# print("Bar:", bar)


# the fix, again, is to use None as the default value
def decode(data, default=None):
  '''Load JSON data from a string.

  Args:
      data: JSON data to decode
      default: Value to return if decoding fails.
        Defaults to an empty dictionary.
  '''
  if default is None:
    default = {}
  try:
    return json.loads(data)
  except ValueError:
    return default


foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also data')
bar['meeep'] = 1
print('Foo:', foo)
print('Bar:', bar)






























