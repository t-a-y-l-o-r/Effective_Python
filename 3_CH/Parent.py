'''
Author: Taylor Cochran
Book: Effective Python
Chapter 3

Goal: To learn WHY you should initilize parent classes with super
'''

# tradiationally paren classes are called using their __init__ method
# this is terrible for larger class trees
# especially when a class inherits from multiple parents
# can result in unintended behaviour
class BaseClass(object):
  def __init__(self, value):
    self.value = value

class SubClass(BaseClass):
  def __init__(self):
    BaseClass.__init__(self, 5)


# EXAMPLES OF POOR BEHAVIOUR
class TimesTwo(object):
  def __init__(self):
    self.value *= 2

class PlusFive(object):
  def __init__(self):
    self.value += 5

class OneWay(BaseClass, TimesTwo, PlusFive):
  def __init__(self, value):
    BaseClass.__init__(self, value)
    TimesTwo.__init__(self)
    PlusFive.__init__(self)

foo = OneWay(5)
print("First attempt: (5 * 2) + 5 = ", foo.value)


class OtherWay(BaseClass, PlusFive, TimesTwo):
  ''' init order does not match argument order'''
  def __init__(self, value):
    BaseClass.__init__(self, value)
    # PlusFive.__init__(self) # flipping the order messes with the calulation
    TimesTwo.__init__(self)
    PlusFive.__init__(self)

bar = OtherWay(5)
print("Second attempt: (5 * 2) + 5 = ", bar.value)

# another problem comes from "diamond inheritance"
# when a class derives from two parents with the same parent
#           root
#            / \
#         sub1 sub2
#            \ /
#           final
# resulting in the same __init__ being run multiple times :(((
# meaning the value for self.value is resest to 5 during the second call
# ruining the calculation!
class TimesFive(BaseClass):
  def __init__(self, value):
    BaseClass.__init__(self, value)
    self.value *= 5

class PlusTwo(BaseClass):
  def __init__(self, value):
    BaseClass.__init__(self, value)
    self.value += 2

class ThisWay(TimesFive, PlusTwo):
  def __init__(self, value):
    TimesFive.__init__(self, value) # calls Base once
    PlusTwo.__init__(self, value) # calls Base a second time

foo = ThisWay(5)
print("This is all wrong: ", foo.value)



# pyton2.2 solved this with the MRO 
# MRO runs the superclasses intilizers depth first, left to right (first to last)
# and only runs a parent once!
# Python3 style is best!

class Explicit(BaseClass):
  def __init__(self, value):
    super(__class__, self).__init__(value * 2)

class Implicit(BaseClass):
  def __init__(self, value):
    super().__init__(value * 2)

assert Explicit(10).value == Implicit(10).value






































