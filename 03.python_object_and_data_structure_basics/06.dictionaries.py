# dictionaries are unordered mappings for storing objects
# lists are ORDERED sequence

my_dict = {'key1':'value1','key2':'value2'}
print(my_dict['key1'])

prices_lookup = {'apple':2.99,'oranges':1.99,'milk':5.80}
print(prices_lookup['apple'])

d = {'k1':123,'k2':[0,1,2],'k3':{'insideKey':100}}
print(d['k2'])
print(d['k3']['insideKey'])
d['k4'] = 300
print(d)

print(d.values())
print(d.keys())
print(d.items())