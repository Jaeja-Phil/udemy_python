# x = 25

# def printer():
#   x = 50
#   return x

# print(printer())

# LEGB rule
# L: local?
# E: enclosing function local
# G; global?
# B: built in

name = 'this is a global string'

def greet():
  name = 'sammy' # comment and uncomment this 

  def hello():
    print('hello ' + name)

  hello()

greet()



x = 50
def func():
  global x # jump to global x
  print(f'x is {x}')

  x = 'new val'
  print(f'i just locally changed x to {x}')
  return x

func()
print(x)