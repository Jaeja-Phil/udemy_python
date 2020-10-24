s = 'print only the words that start with s in this sentence'
for word in s.split():
  if word[0].lower() == 's':
    print(word)

for num in range(0,11):
  if not num % 2:
    print(num)

words = [x for x in range(1,51) if x % 3 == 0]
print(words)

s = 'print every word in this sentence that has an even number of letters'

for word in s.split():
  if len(word) % 2 == 0:
    print(word)

st = 'create a list of first letters of every word in this string'
mylist = [word[0] for word in st.split()]
print(mylist)
