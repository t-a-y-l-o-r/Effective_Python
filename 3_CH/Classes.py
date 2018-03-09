'''
Author: Taylor Cochran
Book: Effective Python
Chapter: 3

Goal: To learn to use helper classes for bookkeeping
'''

# it is easy to use a dict for storing data, like grades
class GradeBook(object):
  def __init__(self):
    self._grades = {}

  def add_student(self, name):
    '''Adds a new student to the dict'''
    self._grades[name] = []

  def add_grade(self, name, grade):
    '''Adds the grade to the list of grades for this student '''
    self._grades[name].append(grade)

  def average_grade(self, name):
    ''' Finds the mean for students total grade thus far'''
    grades = self._grades[name]
    return sum(grades) / len(grades)


# however dictionaries can be overextended
# resulting in 'brittle' code
class BySubjectGradebook(object):
  def __init__(self):
    self._grades = {}

  def add_student(self, name):
    self._grades[name] = []

  def add_grade(self, name, subject, grade):
    '''Adds the grade to the subject, 
        creates the subject dict if it doesn't exist
    '''
    by_subject = self._grades[name]
    grade_list = by_subject.setdefault(subject, [])
    grade_list.append(grade)

  def average_grade(self, name):
    ''' Finds the average across all subjects '''
    by_subject = self._grades[name]
    total, count = 0, 0
    for grades in by_subject.values():
      total += sum(grades)
      count += len(grades)
    return total / count

# yet the problem becomes worse when more funtionality is added 
# when subjects/ assigmnets are given weight values
# the resulting code is extremely messy
# resutling in nested loops and cluttered code for the reader 
# and the user -> too many postional args!
class BySubjectGradebook(object):
  def __init__(self):
    self._grades = {}

  def add_student(self, name):
    self._grades[name] = []

  def add_grade(self, name, subject, grade, weight):
    '''Adds the grade to the subject, 
        creates the subject dict if it doesn't exist
    '''
    by_subject = self._grades[name]
    grade_list = by_subject.setdefault(subject, [])
    grade_list.append((grade, weight))

  def average_grade(self, name):
    ''' Finds the average across all subjects '''
    by_subject = self._grades[name]
    total, count = 0, 0
    for grades in by_subject.values():
      subject_tot, subject_cnt = 0, 0
      for score, weight in grades:
        pass
    return total / count





# tuples might be a good way to store the grades
grades = []
# score and weight
grades.append((94, 0.45))
total = sum(score * weight for score, weight in grades)
total_weight = sum(weight for _, weight in grades)
average_grade = total / total_weight

# however they prevent additional functionality to be added


grades = []
grades.append((94, 0.45, "Great Job!"))


# use named tuples for small data structures
# allowing for clear, easy storage
# as well as simplifying any future migration
import collections
Grade = collections.namedtuple("Grade", ("score", "weight"))

# next make a class for each subject
class Subject(object):
  def __init__(self):
    self._grades = []

  def add_grade(self, score, weight):
    self._grades.append(Grade(score, weight))

  def average(self):
    total, total_weight = 0, 0
    for grade in self._grades:
      total += grade.score * grade.weight
      total_weight += grade.weight
    return total / total_weight


# then a student class
class Student(object):
  def __init__(self):
    self._subjects = {}

  def subject(self, name):
    ''' Add/returns the subject '''
    if name not in self._subjects:
      self._subjects[name] = Subject()
    return self._subjects[name]

  def average_grade(self):
    total, count = 0, 0
    for subject in self._subjects.values():
      total += subject.average()
      count += 1
    return total / count

# then the grade book
class Gradebook(object):
  def __init__(self):
    self._students = {}

  def student(self, name):
    if name not in self._students:
      self._students[name] = Student()
    return self._students[name]


book = Gradebook()
albert = book.student("Albert")
math = albert.subject("Math")
math.add_grade(80, 1)
print(albert.average_grade())


















