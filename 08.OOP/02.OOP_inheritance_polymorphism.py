class Animal():
  def __init__(self):
    print('animal created')

  def who_am_i(self):
    print('i am animal')

  def eat(self):
    print('i am eating')

# myanimal = Animal()

class Dog(Animal):

  def __init__(self):
    Animal.__init__(self)
    print('Dog created')

  # def who_am_i(self):
  #   print('i am a dog') # now this is overwritten

  def eat(self):
    print('dog is eating')

  def bark(self):
    print('woof')

mydog = Dog()
mydog.who_am_i()
mydog.eat()

class Doggo():
  def __init__(self, name):
    self.name = name
  
  def speak(self):
    return self.name + ' says woof!'

class Cat():
  def __init__(self, name):
    self.name = name
  
  def speak(self):
    return self.name + ' says meow!'

mydoggo = Doggo('jjun')
mycat =  Cat('arong')

for pet in [mydoggo, mycat]:
  print(type(pet))
  print(pet.speak())

def pet_speak(pet):
  print(pet.speak())

pet_speak(mydoggo)
pet_speak(mycat)

class Animal2():

  def __init__(self, name):
    self.name = name

  def speak(self):
    raise NotImplementedError('subclass must implement this abstract method')

myanimal = Animal2('fred')
# myanimal.speak() # this causes an error!


class Example():

  def __init__(self, name):
    self.name = name


class Example2(Example):
  def speak(self):
    return self.name + 'ssssss'

example = Example2('haha')
test = example.speak()
print(test)