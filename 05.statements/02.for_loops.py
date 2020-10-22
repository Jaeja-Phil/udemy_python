# my_iterable = [1,2,3]
# for item_name in my_iterable:
#   print(item_name)

mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylist:
  if num % 2 == 0:
    print(num)
  else:
    print(f'odd num: {num}')


list_sum = 0

for num in mylist:
  list_sum += num

print(list_sum)

tup = (1,2,3)

for item in tup:
  print(item)

mylist = [(1,2),(3,4),(5,6)]

for item in mylist:
  print(item)

for first,second in mylist:
  print(first, second)

d = {'k1':1,'k2':2,'k3':3}

for item in d.items():
  print(item) # item is tuple ('k1', 1), ....

for key, value in d.items():
  print(key, value)
