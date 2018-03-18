'''
Author: Taylor Cochran
Book: Effective Python
Chapter 3: Classes and Inheritance

Goal: To learn WHY you shuold prefer public attributes over private ones


Remeber:
  1) Private attributes aren't really a thing in Python
  2) Plan for subclasses to utilize your attributes!
  3) Document protected fields and methods with interal use or okay to motify
  4) Only use private when dealing with possible naming conflicts down the line!
'''

# in python there are only two types of access for atttributes:
# public var
# public __var

class MyObject(object):
  def __init__(self):
    self.public_field = 5
    self.__private_field = 10

  def get_private_field(self):
    return self.__private_field

  @classmethod
  def get_private_field_of_instance(cls, instance):
    ''' Class methods also have access to private fields, due to their scope'''
    return instance.__private_field

ob = MyObject()
assert ob.get_private_field() == 10
assert ob.public_field == 5
assert MyObject.get_private_field_of_instance(ob) == 10



# children can't access a Parents private fields!
class Parent(object):
  def __init__(self):
    self.__private_field = 71

class Child(Parent):
  def get_private_field(self):
    self.__private_field


'''
When an attribute is called Python resolves it's name as follows:
object = MyObject()
var_call = object.var
resolved_name = objectvar

In the instance of a child calling a parent's attribute:
the child has not attribute called child__private_field. Thus the call fails!
'''


test = Child()
# test.get_private_field() # fails!
print(test.__dict__)
# shows the private attribute's resolved name is '_Parent__private_field'

'''
Python's philosphy is very simple:
"We are all consenting adults here"
Meaning Python's creators belive that the pros for openness outway the pros for closedness

This is especailly aparent when you consider the level of control you have over a class
 with the following methods:
  __getattr__
  __getattribute__
  __setattr__

Generally a 'protected' field or method is preceded by an '_' 
  and should be treated with care
'''

# python is not java!
class MyClass(object):
  def __init__(self, value):
    self.__value = value

  def get_value(self):
    return self.__value



# coding in the above manner makes inheritance cumberson
# it also introduces the lack of addaptability should a method sig change
# in the parent class
class MyIntegerChild(MyClass):
  def get_value(self):
    return int(self._MyClass__value) # gross!

foo = MyIntegerChild(5)
assert foo.get_value() == 5


# altering MyClass's parent structure destroys MyIntegerChild's attribute call!
class MyRoot(object):
  def __init__(self, value):
    self.__value = value

class MyClass(MyRoot):
  def __init__(self, value):
    super().__init__(value)

class MyIntegerChild(MyClass):
  def get_value(self):
    return int(self._MyClass__value)

foo = MyIntegerChild(5)
print(foo.__dict__) # _My_Root__value!
# assert foo.get_value() == 5 # no longer works!




# it is better to use protected attributes and document which ones are for internal API
# usage and which are safe to manipulate
# allowing for more flexible implemntation down the line
class MyClass(object):
  def __init__(self, value):
    ''' Stores the passed value to a protected attribute.
    The attribute should be considered immutable. 
    It is primarily for internal usage!
    '''
    self._value = value

# protected attributes should only ever be used when naming conflicts might arrise
class ApiClass(object):
  def __init__(self):
    self.__value = 5

  def get(self):
    return self.__value

class Child(ApiClass):
  def __init__(self):
    super().__init__()
    self._value = "Hello World!" # this works just fine!

a = Child()
print(a.get(), " and ", a._value, " are different!")
































