'''
Author: Taylor Cochran
Book: Effective Python
Ch1

Goal:
  To learn about try/except/else/finally
'''

# finally
handle = open("my_file.txt", 'ab+') # may throw IOError
try:
  data = handle.read() # may throw UnicodeDecodeException
  print(data.decode('utf-8'))
finally:
  handle.close() # always runs after try


# use try/except/else to denote which exceptions you handle
# also allows for the reduction of code in the try
# imrpoving readability
def load_json_key(data, key):
  try:
    result_dict = json.loads(data) # ValueError
  except ValueError as e:
    raise KeyError from e
  else:
    return result_dict[key] # KeyError


# try/except/else/finally to allow for both complexity and readiabilty
UNDEFINED = object()

def divid_json(path):
  handle = open(path, "rb+") # IO
  try:
    date = handle.read() # UnicodeDecode
    op = json.loads(data) # Value Error
    value = (
      op['numerator']/
      op['denominator']
      )
  except ZeroDivisionError as e:
    return UNDEFINED
  else:
    op['result'] = value
    result = json.dumps(op)
    handle.seek(0)
    handle.write(result) # IO
    return value
  finally:
    handle.close()













