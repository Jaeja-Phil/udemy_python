my_list = [1,2,3]
my_list2 = [1, 'string', 23.2]
print(len(my_list), len(my_list2))

my_list3 = ['one','two','three']
print(my_list3[1:])
another_list = ['four','five']
new_list = my_list3 + another_list
print(new_list)
new_list[0] = 'ONE ALL CAPS'
print(new_list)
new_list.append('six')
print(new_list)
print(new_list.pop())
print(new_list)
print(new_list.pop(0)) # default index is -1
print(new_list)

new_list = ['a','e','x','b','c']
num_list = [4,1,8,3]
new_list.sort()
print(new_list) # .sort() is in-place
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)