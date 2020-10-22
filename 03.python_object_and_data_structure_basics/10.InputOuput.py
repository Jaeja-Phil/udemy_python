# myfile = open('some/file/path', 'r')
# myfile.write('something!!!')

with open('./03.python_object_and_data_structure_basics/assets/writefile.txt', 'w') as f:
  f.write('hellooooooo')
# or f.read() on 'r' mode

# options 'r', 'w' --> write only, overites or creates new file 'a', 
# 'r+' --> reading writing 'w+' --> writing and reading (overite existing files or create a new file)