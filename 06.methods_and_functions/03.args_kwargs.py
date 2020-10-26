def myfunc(a,b,c=0,d=0):
  # returns 5% of the sum of a and b
  return sum((a,b)) * 0.05

print(myfunc(40,60))

def myfunc(*args):
  print(args)
  return sum(args) * 0.05

print(myfunc(1,5,3,2,1,100))

def myfunc(**kwargs):
  print(kwargs)
  if 'fruit' in kwargs:
    print('my fruit of choice is {}'.format(kwargs['fruit']))
  else:
    print('cant find the fruit')

myfunc(fruit = 'apple', veggie = 'lettuce')
  
def myfunc1(*args, **kwargs):
  print('id like {} {}'.format(args[0], kwargs['food']))

myfunc1(10,20,30,fruit='orange',food='eggs',animal='dog')
# order of args and kwargs is important!