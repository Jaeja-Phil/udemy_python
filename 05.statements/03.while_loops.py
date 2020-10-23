# while some_condition:
#   do something

x = 0

while x < 5:
  print(f'the current value of x is {x}')
  x += 1
else:
  print('x is not less than 5')

y = [1,2,3]
for item in y:
  # comment
  pass # need this to not have EOF

mystring = 'phil'
for letter in mystring:
  if letter == 'i':
    continue
  print(letter)

for letter in mystring:
  if letter == 'i':
    break
  print(letter)

  