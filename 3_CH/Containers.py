'''
Author: Taylor Cochran
Book: Effective Python
Chapter 3: Classes and Inheritance

Goal: Learn to inherit from collection.abc for Custom container types!


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

# this allows for you to inherit all of list's useful methods
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
    ''' this could be worked on, but isn't really the main point'''
    item = None
    for attr, value in self.__dict__.items():
      # print("Attr: ", attr, " value: ", value)
      if isinstance(value, int):
        count += 1
        item = value
      if isinstance(value, IndexNode):
        # print('recurring ', count)
        item, count = value._search(count, index)
      if count == index:
        # print(count)
        return (value, count)
    # print(item, count)
    return (item, count)

  def __getitem__(self, index):
    found, _ = self._search(0, index)
    if not found:
      raise IndexError('Index out of range')
    return found

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

# print("LRR: ", tree.left.right.right.value)
# print("Index 0: ", tree[0])
# print("Index 1: ", tree[1])
# print("11 in the tree: ", 11 in tree)
# print("17 in the tree: ", 17 in tree)
# print("Tree is", list(tree))

'''
The main problem is that every behavior default to list would need to be implented 
manually.

No bueno!
'''

class SequenceNode(IndexNode):
  def __len__(self):
    _, count = self._search(0, None)
    return count
tree = SequenceNode(
  10, 
  left=SequenceNode(
    5,
    left=SequenceNode(2),
    right=SequenceNode(
      6, right=SequenceNode(7))
    ),
  right=SequenceNode(
    15, left=SequenceNode(11))
  )
# print(len(tree))
# print(tree[1])
# print(isinstance(tree[1], IndexNode))
i = 0
while i < 7:
  print(tree._search(0, i))
  i += 1













































