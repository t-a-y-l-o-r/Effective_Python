'''
Author: Taylor Cochran
Book: Effective Python
Ch2

Goal:
  To understand why returning generators is preferable
'''

from itertools import islice

# returning lists is easy
# but creates noise, complexity, and breaks down under heavy load
def index_words(text):
  result = []
  if text:
    result.append(0)
  for index, letter in enumerate(text):
    if letter == " ":
      result.append(index + 1)
  return result

address = "Four score and even years ago..."
result = index_words(address)
print(result)


# using a generator will reduce noise and complexity
# additioanlly can easily be converted to a list using the inbult list function
def index_words_iter(text):
  if text:
    yield 0
  for index, letter in enumerate(text):
    if letter == " ":
      yield index + 1

gen = index_words_iter(address)
print(list(gen))



# the following generator reads one line at a time
# while yielding one word at a time
# only keeping one line in memeory at any given moment
def index_file(handle):
  offset = 0
  for line in handle:
    if line:
      yield offset
    for letter in line:
      offset += 1
      if letter == " ":
        yield offset


with open("my_file.txt", "r") as f:
  it = index_file(f)
  results = islice(it, 0, 3)
  print(list(results))





















