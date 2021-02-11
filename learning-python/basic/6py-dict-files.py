"""
Dict Hash Table
"""
# Can build up a dict by starting with the the empty dict {}
# and storing key/value pairs into the dict like this:
# dict[key] = value-for-that-key
print('Dict Hash Table')
new_dict = {}
new_dict['a'] = 'alpha'
new_dict['g'] = 'gamma'
new_dict['o'] = 'omega'

print(new_dict)  # {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

print(new_dict['a'])  # Simple lookup, returns 'alpha'
new_dict['a'] = str(6)  # Put new key/value into dict

print('a' in new_dict)  # True

# print dict['z']  # Throws KeyError
if 'z' in new_dict:
    print(new_dict['z'])  # Avoid KeyError

print(new_dict.get('z'))  # None (instead of KeyError)

"""
By default, iterating over a dict iterates over its keys.
Note that the keys are in a random order
"""
print('\nPrinting Keys')
for key in new_dict:
    print(key)  # prints a g o

# Exactly the same as above
for key in new_dict.keys():
    print(key)

# Get the .keys() list:
print('\nPrinting Keys list')
print(new_dict.keys())  # ['a', 'o', 'g']

# Likewise, there's a .values() list of values
print('\nPrinting Values list')
print(new_dict.values())  # ['alpha', 'omega', 'gamma']

"""
Common case -- loop over the keys in sorted order,
accessing each key/value
"""
print('\nPrinting sorted Key/value')
for key in sorted(new_dict.keys()):
    print(key, new_dict[key])

# .items() is the dict expressed as (key, value) tuples
print('\nPrinting dict as (key, value) tuples')
print(new_dict.items())  # [('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')]

"""
This loop syntax accesses the whole dict by looping over the .items() tuple list, accessing one (key, value)
pair on each iteration.
"""
print('\nPrinting one key/value pair on each iteration.')
for k, v in new_dict.items():
    print(k, '/', v)  # a / alpha    o / omega     g / gamma

"""
Dict Formatting
"""
new_hash = {}
new_hash['word'] = 'garfield'
new_hash['count'] = 42
s = 'I want %(count)d copies of %(word)s' % new_hash  # %d for int, %s for string  # 'I want 42 copies of garfield'
print('\nPrinting dict formatted string')
print(s)

"""
Files
"""
# Echo the contents of a file
f = open('foo.txt', 'rU')
for line in f:  # iterates over the lines of the file
    print(line,)  # trailing , so print does not add an end-of-line char
    # since 'line' already includes the end-of-line.
f.close()

