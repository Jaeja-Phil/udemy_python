def name_of_function(name):
  """
  docstring explaining function.
  """
  print(f'hello {name}')

name_of_function('phil')

def add_func(n1, n2):
  return n1 + n2

result = add_func(10,15)
print(result)

def say_hello(dudu='some default name'):
  print(f'hello {dudu}')

say_hello('jose')
# have to pass in the argument
# or have a default value
say_hello()

def even_check(num):
  return num % 2 == 0

print(even_check(20))

def check_even_list(num_list):
  for number in num_list:
    if number % 2 == 0:
      return True
  return False

print(check_even_list([1,3,5,7,9]))
print(check_even_list([1,3,5,7,10]))

stock_prices = [('APPL',200),('GOOG',400),('MSFT',100)]
for item in stock_prices:
  print(item)
for ticker,price in stock_prices:
  print(ticker)
  print(price)

work_hours = [('abby',100),('billy',400),('cassie',800)]

def employee_check(work_hours):
  current_max = 0
  employee_of_month = ''

  for employee,hours in work_hours:
    if hours > current_max:
      current_max = hours
      employee_of_month = employee

  return (employee_of_month, current_max)

print(employee_check(work_hours))
name, hours = employee_check(work_hours)

print(name, hours)


example = [1,2,3,4,5,6,7]

from random import shuffle

shuffle(example)
print(example)

def shuffle_list(mylist):
  shuffle(mylist)
  return mylist

result = shuffle_list(example)
print(result)