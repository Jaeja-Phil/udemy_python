a = 'hello world'
print(len(a))
print(a[0]) # a[20] will give an index error
print(a[-3])

print(a[2:])
print(a[2:6])
print(a[:6:2])
print(a[::2])
print(a[::-1])
print(a[::-2])

# a[0] = 'p' error! TypeError: 'str' object doesnt support item assignment
# print(a) # still 'hello world'
b = 'p' + a[1:]
print(b)

print(a.upper()) 
print(a.title())
print(a.split()) # default is a space split

# .format()
# f-strings formatted string literals

print('string here {2} then also here {0}'.format('phillip', 'choi', 'aaaa'))
print('the {f} {b} {q}'.format(f = 'fox', b = 'brown', q = 'quick'))

result = 100/777
print(result)
# formatting "{value:width.precision f}"
print('{r:1.3f}'.format(r = result)) 


# f-strings
name = 'Phillip'
age = 3
print(f'hello, my name is {name}')
print(f'{name} is {age} years old')