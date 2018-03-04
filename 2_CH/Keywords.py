'''
Author: Taylor Cochran
Book: Effective Python
Ch1

Goal:
  To learn keyword arguments and optional behavior
'''

# postional arguments are pretty standard across most languages
def remainder(num, divis):
  return num % divis

assert remainder(20, 7) == 6


# all positional arguments duel as keyword arguments by default
# make sure to pass all postional arguments before keywords!
remainder(20, 7)
remainder(20, divis=7)
remainder(num=20, divis=7)
remainder(divis=7, num=20)
# remainder(divis=7, 20) # breaks
# remainder(20, num=7) # each value can only be supplied once


# keyword allow for alternative behavior, less code, and clarity to newcomers

# determines flow_rate

def flow_rate(weight_diff, time_diff):
  return weight_diff / time_diff

weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
# print("%.3f kg per second" % flow)


# now implements the ability to extrapolate this data to larger time periods
def flow_rate(weight_diff, time_diff, period):
  return (weight_diff / time_diff) * period


weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff, 1)
# print("%.3f kg per second" % flow)


# providing a default value redueces noise for the user
def flow_rate(weight_diff, time_diff, period=1):
  return (weight_diff / time_diff) * period


weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
# print("%.3f kg per second" % flow)
flow = flow_rate(weight_diff, time_diff, 3600)
# print("%.3f kg per hour" % flow)



# extending the definition of a function is easy with keyward arguments
def flow_rate(weight_diff, time_diff,
              period=1, units_per_kg=1):
  return ((weight_diff * units_per_kg) / time_diff) * period


weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print("%.3f kg per second" % flow)
flow = flow_rate(weight_diff, time_diff, 3600)
print("%.3f kg per hour" % flow)
flow = flow_rate(weight_diff, time_diff, 3600, 1000)
print("%.3f grams per hour" % flow)








































