'''
Author: Taylor Cochran
Book: Effective Python
Chapter 3

Goal: To utilize @classmethod polymorphism to construct classes generically
'''
import os
from threading import Thread

# a class representing input data
class InputData(object):
  def read(self):
    raise NotImplementedError

# this is an implementation of InputData
class PathInputData(InputData):
  def __init__(self, path):
    super().__init__()
    self.path = path

  def read(self):
    return open(self.path).read()

# consider an interface class for a map reduce worker
class Worker(object):
  def __init__(self, input_data):
    self.input_data = input_data
    self.result = None

  def map(self):
    raise NotImplementedError

  def reduce(self, other):
    raise NotImplementedError

# implements the Worker interface :)
# tracks the number of newline chars
class LineCountWorker(Worker):
  def map(self):
    ''' Counts the number of newlines in the passed data list'''
    data = self.input_data.read()
    self.result = data.count("\n")

  def reduce(self, other):
    ''' Consolidatos the count from all of the workers
    into one result
    '''
    self.result += other.result


# how dow we connect all of these constructs?
# a helper function seems obvious
def generate_inputs(data_dir):
  ''' Yields a list of data files to be worked'''
  for name in os.listdi(data_dir):
    yield PathInputData(os.path.join(data_dir, name))


def create_workers(input_list):
  ''' Implements a list of worker bots for each data file'''
  workers = []
  for input_data in input_list:
    workers.append(LineCountWorker(input_data))
  return workers

# but how do we connect each interworking part?
# right now: manually :(


def generate_inputs(data_dir):
  ''' Crawls a directory for data files. 
  Generates a PathInputData instance for each file found
  '''
  for name in os.listdir(data_dir):
    yield PathInputData(os.path.join(data_dir, name))


def create_workers(input_list):
  ''' Creates a list of workers for each data input.'''
  workers = []
  for input_data in input_list:
    workers.append(LineCountWorker(input_data))
  return workers


def execute(workers):
  ''' Fanns out the work by threading multiple 
  workers across the data all at once.
  '''
  threads = [Thread(target=w.map) for w in workers]
  for thread in threads: thread.start()
  for thread in threads: thread.join()

  first, rest = workers[0], workers[1:]
  for worker in rest:
    first.reduce(worker)
  return first.result


def mapreduce(data_dir):
  ''' Strings everything together'''
  inputs = generate_inputs(data_dir)
  workers = create_workers(inputs)
  return execute(workers)



# the final result is extremely clunky :(((
file_list = ["1_temp.txt", "2_temp.txt", "3_tempt.txt"]
temp_dir="/Users/taylorcochran/Documents/TempData"
def write_test_files(file_list, temp_dir):
  temp_dir = os.path.abspath(temp_dir)
  if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)
    for temp in file_list:
      temp_file = os.path.join(temp_dir, temp)
      with open(temp_file, "w+") as handle:
        handle.write("\n\n\n\n\n\n")
write_test_files(file_list, temp_dir)

result = mapreduce(temp_dir)

# print("There are %s lines in the dir!" % int(result))




# Would have to rewrite to implement in a different environment!
# Most languages fix this issue with polymorphism and constructors
# however python only allows for 1 __init__
# instead use @classmethod, allowing for generic implementations!

class GenericInputData(object):
  def read(self):
    raise NotImplementedError

  @classmethod
  def generate_inputs(cls, config):
    raise NotImplementedError


class PathInputData(GenericInputData):
  def __init__(self, path):
    self.path = path

  def read(self):
    ''' Ouputs the contents of a file '''
    return open(self.path).read()

  @classmethod
  def generate_inputs(cls, config):
    ''' Generates a list data file paths '''
    data_dir = config["data_dir"]
    for name in os.listdir(data_dir):
      yield cls(os.path.join(data_dir, name))


class GenericWorker(object):
  def __init__(self, input_data):
    self.result = None
    self.input_data = input_data

  def map(self):
    raise NotImplementedError

  def reduce(self):
    raise NotImplementedError

  @classmethod
  def create_workers(cls, input_class, config):
    ''' Returns a list of generic worker bots '''
    workers = []
    for input_data in input_class.generate_inputs(config): # allows for generic workers
      workers.append(cls(input_data)) # circumvents the __init__
    return workers


class LineCountWorker(GenericWorker):
  def map(self):
    ''' Counts the number of newlines in the passed data list'''
    data = self.input_data.read()
    self.result = data.count("\n")

  def reduce(self, other):
    ''' Consolidatos the count from all of the workers
    into one result
    '''
    self.result += other.result


def map_reduce(worker_class, input_class, config):
  ''' Runs the bots across the passed dir, 
  counts the number of new lines in the dir's files
  '''
  workers = worker_class.create_workers(input_class, config)
  return execute(workers)


config = {'data_dir': temp_dir}
result = map_reduce(LineCountWorker, PathInputData, config)

print("%s new lines found!" % result)














