'''
Author: Taylor Cochran
Book: Effective Python
Ch1

Goal:
  To learn about zipping iterators
'''

# create a list from another list using list comprehension
names = ['Johnathan', 'Noah', 'Billy']
letters = [len(n) for n in names]


# to iterate over each list in parallel, iterate over the length of the names source lst
longest_name = None
max_letters = 0

for i in range(len(names)):
  count = letters[i]
  if count > max_letters:
    longest_name = names[i]
    max_letters = count


# using enumerate helps a litte
for i, name in enumerate(names):
  count = letters[i]
  if count > max_letters:
    longest_name = names[i]
    max_letters = count


# zip is the best approach
for name, count in zip(names, letters):
  if count > max_letters:
    longest_name = name
    max_letters = count

# zip should only be used on lists of the same size
# use zip_longest from itertools if you are not sure of their equality