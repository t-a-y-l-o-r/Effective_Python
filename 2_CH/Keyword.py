'''
Author: Taylor Cochran
Book: Effective Python
Ch: 2

goal: Enforce clarity with Keyword-only arguments
'''



# division that ignores errors
# requires the user to remember the position of each argument
# possibly resulting in sublte bugs down the line
def safe_division(number, divisior, ignore_overflow, ignore_zero_division):
  try:
    return number / divisior
  except OverflowError:
    if ignore_overflow:
      return 0
    else:
      raise
  except ZeroDivisionError:
    if ignore_zero_division:
      return float("inf")
    else:
      raise


# result = safe_division(1.0, 10**500, True, False)
# print(result)
# result = safe_division(1.0, 0, False, True)
# print(result)

# instead FORCE keyword arguments to be passed, resulting in clear intention
def safe_division(number, divisior, *,
                 ignore_overflow=False, ignore_zero_division=False):
'''Divides the two numbers passed.

Args:
    number: The numerator
    divisor: The divisor
    ingore_overflow: returns 0 if True, raises OverflowError otherwise.
      Defaults to False.
    ignore_zero_division: returns inf if True, raises ZeroDivisionError otherwise.
      Defaults to False.
'''
try:
  return number / divisior
except OverflowError:
  if ignore_overflow:
    return 0
  else:
    raise
except ZeroDivisionError:
  if ignore_zero_division:
    return float("inf")
  else:
    raise
















