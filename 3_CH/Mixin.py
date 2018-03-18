'''
Author: Taylor Cochran
Book: Effective Python
Chapter 3: Classes and Inheritance

Goal: To use multiple class inheritance for mix-in utility classes


Remeber:
  1) Avoid using multi inheritance except when utilizing mixin-classes
  2) Feel free to override method behavior as needed
  3) Compose mixins to create complex behavior from just a few simple classes
'''

import json

# a mix-in that converts python data to a dict for future serlization
# basically adds this method to any class that inherites from todictmix
class ToDictMixin(object):
  def to_dict(self):
    return self._traverse_dict(self.__dict__)
# implimentation utilizes dynamic attribute access
# with hasattr
# dynamic type inspection with ininstance
# and accessing the instance dictionary __dict__
  def _traverse_dict(self, instance_dict):
    output = {}
    for key, value in instance_dict.items():
      output[key] = self._traverse(key, value)
    return output

  def _traverse(self, key, value):
    if isinstance(value, ToDictMixin):
      return value.to_dict()
    elif isinstance(value, dict):
      return self._traverse_dict(value)
    elif isinstance(value, list):
      return [self._traverse(key, i) for i in value]
    elif hasattr(value, "__dict__"):
      return self._traverse_dict(value.__dict__)
    else:
      return value

# makes a dict from a binary tree
class BinaryTree(ToDictMixin):
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

# inheritance from ToDictMixin makes converting any data to a dict extremly easy
tree = BinaryTree(10, 
                  left=BinaryTree(7, right=BinaryTree(9)),
                  right=BinaryTree(13, left=BinaryTree(11))
                  )

print(tree.to_dict())

# the following defenition would cause to_dict to loop forever
class BinaryTreeWithParent(BinaryTree):
  def __init__(self, value, left=None, right=None, parent=None):
    super().__init__(value, left=left, right=right)
    self.parent = parent

# the solution is to override the _traverse defintiion 
# to only filter out results that matter
# returning only the numerical values of the parent rather than
# calling it's to_dict
  def _traverse(self, key, value):
    if (isinstance(value, BinaryTreeWithParent) and key == "parent"):
      return value.value # prevents infinite loop
    else:
      return super()._traverse(key, value)


root = BinaryTreeWithParent(10)
root.left = BinaryTreeWithParent(7, parent=root)
root.left.right = BinaryTreeWithParent(9, parent=root.left)
print("\n", root.to_dict())


# by overrideing _traverse any class that contains a BinaryTreeWithParent
# as an attribute will now automatically be compatible with ToDictMixn inheritance
class NamedSubTree(ToDictMixin):
  def __init__(self, name, tree_with_parent):
    self.name = name
    self.tree_with_parent = tree_with_parent

my_tree = NamedSubTree('foobar', root.left.right)
print("\n", my_tree.to_dict())




# Mixins can also be composed together
# this class implements Json serlization
# and assumes the class provides a to_dict method
class JsonMixin(object):
  @classmethod
  def from_json(cls, data):
    kwargs = json.loads(data)
    return cls(**kwargs) # allows the passage of a dict

  def to_json(self):
    return json.dumps(self.to_dict())

# now itlizing multi-inheritance it is possible to beneifit from the to_dict in 
# ToDictMixin and from Json serilization
class DatacenterRack(ToDictMixin, JsonMixin):
  def __init__(self, switch=None, machines=None):
    self.switch = Switch(**switch)
    self.machines = [Machine(**kwargs) for kwargs in machines]

class Switch(ToDictMixin, JsonMixin):
  def __init__(self, *args, **kwargs):
    pass 

class Machine(ToDictMixin, JsonMixin):
  def __init__(self, *arge, **kwargs):
    pass


serailized = '''{
  "switch": {"ports": 5, "speed": 1e9},
  "machines": [
              {"cores": 8, "ram": 32e9, "disk": 5e12},
              {"cores": 4, "ram": 16e9, "disk": 1e12},
              {"cores": 2, "ram": 4e9, "disk": 500e9}
              ]
}'''

deserialized = DatacenterRack.from_json(serailized)
rountrip = deserialized.to_json()
# print("\n", deserialized)
# print("\n", json.loads(serailized))
# print("\n", json.loads(DatacenterRack.from_json(serailized).to_json()))
# print("\n", json.loads(rountrip))
# assert json.loads(serailized) == json.loads(rountrip)



































