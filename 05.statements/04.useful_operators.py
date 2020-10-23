mylist = [1,2,3]

for num in range(0,10,2):
  print(num)

print(list(range(0,11,2)))

index_count = 0
for letter in 'abcde':
  print('at index {} the letter is {}'.format(index_count, letter))
  index_count += 1

index_count = 0
word = 'abcde'
for letter in word:
  print(word[index_count])
  index_count += 1

for item in enumerate(word):
  print(item)

for index, letter in enumerate(word):
  print(index, letter)

mylist1 = [1,2,3,4,5,6,7,8]
mylist2 = ['a','b','c','d','e']

print('\n\nzip function')
for item in zip(mylist1, mylist2): # change item to a, b, or w.e
  print(item)

print(list(zip(mylist1, mylist2)))

print('x' in [1,2,3])
print('x' in [1,2,'x'])
print('a' in 'a world')
print('mykey' in {'mykey':345})
d = {'mykey':345}
print(345 in d.keys())
print(345 in d.values())

mylist = [1,2,3,2,3]
print(min(mylist))
print(max(mylist))

from random import shuffle
mylist = [1,2,3,4,5]
shuffle(mylist)
print(mylist)

from random import randint
print(randint(0,100))
print(randint(0,100))

result = input('whats ur name')
print(result)