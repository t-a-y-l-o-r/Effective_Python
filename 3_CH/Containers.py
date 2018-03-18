'''
Author: Taylor Cochran
Book: Effective Python
Chapter 3: Classes and Inheritance

Goal: Learn to inherit from collection.abs for Custom container types!


Remeber:
  1) 
'''


# lets inherite from Pyton's build in list class
# and see what happens
class FrequencyList(list):
  def __init__(self, members):
    super().__init__(members)

  def frequency(self):
    counts = {}
    for item in self:
      counts.setdefault(item, 0)
      counts[item] += 1
    return counts

# this allows for you to inherit all of list's usefull methods
# as well as allowing for the addition of custom behavior
test = FrequencyList(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'a', 'b', 'c', 'a', 'd'])
# print("Legnth is: ", len(test))
test.pop()
# print("After pop: ", repr(test))
# print("Frequency: ", test.frequency())


# now implementing a custom list like class
# but not inheriting from the list class itself
class BinaryNode(object):
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

# the trick is getting python to allow indexing with this custom class
# the following
bar = [1, 2, 3]
bar[0]
# is interpreted as
bar.__getitem__(0)

# thus a cutom implementaion of __getitem__ might help

class IndexNode(BinaryNode):
  def _search(self, count, index):
    count = 0
    item = None
    dic = {}
    for attr, value in self.__dict__.items():
      if count == index:
        return [value], count
      count += 1
    return item, count


  def __getitem__(self, index):
    found, _ = self._search(0, index)
    if not found:
      raise IndexError('Index out of range')
    return found[0]

# now create tree as usual
tree = IndexNode(
  10, 
  left=IndexNode(
    5,
    left=IndexNode(2),
    right=IndexNode(
      6, right=IndexNode(7))
    ),
  right=IndexNode(
    15, left=IndexNode(11))
  )

print("LRR: ", tree.left.right.right.value)
print("Index 0: ", tree[0])
print("Index 1: ", tree[1])
print("11 in the tree: ", 11 in tree)
print("17 in the tree: ", 17 in tree)
print("Tree is", list(tree))














































