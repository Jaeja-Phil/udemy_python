mylist = [1,2,3]
# mylist. ~~~ (some method)

class SampleClassName():
  pass

my_sample = SampleClassName()
print(type(my_sample))

class Dog():
  # class object attribute
  # same for any instance of a class
  species = 'mammal'

  def __init__(self, mybreed, name):
    # attributes
    # we take in the argument
    # assign it using self.attribute_name
    self.breed = mybreed
    self.name = name

  def bark(self, number):
    print('woof! my name is {} and the number is {}'.format(self.name, number))

dog1 = Dog('maltese', 'sammy')
print(dog1.species)
print(dog1.breed)
print(dog1.name)
dog1.bark(5)

class Circle():
  pi = 3.14

  def __init__(self, radius=1):
    self.radius = radius

  def get_circumference(self):
    return self.radius * self.pi * 2

my_circle = Circle()

print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumference())