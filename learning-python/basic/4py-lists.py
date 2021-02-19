print('\nLists')
colors = ['red', 'blue', 'green']
print(colors[0])  # red
print(colors[2])  # green
print(len(colors))  # 3


# FOR and IN
# If you know what sort of thing is in the list, use a variable name in the loop that captures that information such
# as "num", or "name", or "url". Since Python code does not have other syntax to remind you of types, your variable
# names are a key way for you to keep straight what is going on.

print('\nFOR and IN')
squares = [1, 4, 9, 16]
sum_of_squares = 0
for num in squares:
    sum_of_squares += num
print(sum_of_squares)  # 30


# The *in* construct on its own is an easy way to test if an element appears in a list (or other collection) --
# value in collection -- tests if the value is in the collection, returning True/False.

names_list = ['larry', 'curly', 'moe']
if 'curly' in names_list:
    print('yay !!!')


# Range

print('\nRange')
# print the numbers from 0 through 4
for i in range(5):
    print(i)


# List Methods

print('\nList Methods')
new_list = ['larry', 'curly', 'moe']
new_list.append('shemp')  # append elem at end
new_list.insert(0, 'xxx')  # insert elem at index 0
new_list.extend(['yyy', 'zzz'])  # add list of elems at end
print(new_list)  # ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print(new_list.index('curly'))  # 2

new_list.remove('curly')  # search and remove that element
new_list.pop(1)  # removes and returns 'larry'
print(new_list)  # ['xxx', 'moe', 'shemp', 'yyy', 'zzz']


# Common error: note that the above methods do not *return* the modified list, they just modify the original list.

noreturn_list = [1, 2, 3]
# print(list.append(4))  # NO, does not work, append() returns None
# Correct pattern:
noreturn_list.append(4)
print(noreturn_list)  # [1, 2, 3, 4]


# List Slices
# Slices work on lists just as with strings, and can also be used to change sub-parts of the list.

print('\nList Slices')
slice_list = ['a', 'b', 'c', 'd']
print(slice_list[1:-1])  # ['b', 'c']
slice_list[0:2] = 'z'  # replace ['a', 'b'] with ['z']
print(slice_list)  # ['z', 'c', 'd']

