# Find the indexs of new
li = ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']

# Finds index of only first occurence new
print(li.index('new'))

# Finds index of only first occurence new from 3rd position to end of list
print(li.index('new',3,len(li)))

# Get list of indexes using enumerate, tuples and listcomps
print([(i) for i,j in enumerate(li) if j == 'new'])