"""
Sorting
The easiest way to sort is with the sorted(list) function, which takes a list and returns a new list with those
elements in sorted order. The original list is not changed.
"""
numbers_to_sort = [5, 1, 4, 3]
print("Sorted List:")
print(sorted(numbers_to_sort))  # [1, 3, 4, 5]
print("Original List:")
print(numbers_to_sort)  # [5, 1, 4, 3]

strs_to_sort = ['aa', 'BB', 'zz', 'CC']
print(sorted(strs_to_sort))  # ['BB', 'CC', 'aa', 'zz'] (case sensitive)
print(sorted(strs_to_sort, reverse=True))  # ['zz', 'aa', 'CC', 'BB']

"""
Custom Sorting With key= 
For more complex custom sorting, sorted() takes an optional "key=" specifying a "key" 
function that transforms each element before comparison. The key function takes in 1 value and returns 1 value, 
and the returned "proxy" value is used for the comparisons within the sort. 
"""
print('\nCustom Sorting With key=')
key_len_sorting_list = ['ccc', 'aaaa', 'd', 'bb']
print('Sorting With key=len(str)')
print(sorted(key_len_sorting_list, key=len))  # ['d', 'bb', 'ccc', 'aaaa']

key_lower_sorting_list = ['aa', 'BB', 'zz', 'CC']
# "key" argument specifying str.lower function to use for sorting
print('Sorting With key=str.lower)')
print(sorted(key_lower_sorting_list, key=str.lower))  # ['aa', 'BB', 'CC', 'zz']

"""
You can also pass in your own function as the key, like this:
"""
# Say we have a list of strings we want to sort by the last letter of the string.
custom_sorting_list = ['xc', 'zb', 'yd', 'wa']


# Write a little function that takes a string, and returns its last letter.
# This will be the key function (takes in 1 value, returns 1 value).
def my_sort_function(s):
    return s[-1]


# Now pass key=MyFn to sorted() to sort by the last letter:
print(sorted(custom_sorting_list, key=my_sort_function))  # ['wa', 'zb', 'xc', 'yd']

"""
sort() method
As an alternative to sorted(), the sort() method on a list sorts that list into ascending order, e.g. list.sort(). 
The sort() method changes the underlying list and returns None, so use it like this:
"""
# alist.sort()  # correct
# sorted_list = alist.sort()  # incorrect, sort() returns None

"""
Tuples
A tuple is a fixed size grouping of elements, such as an (x, y) co-ordinate. Tuples are like lists, except they are 
immutable and do not change size (tuples are not strictly immutable since one of the contained elements could be 
mutable). Tuples play a sort of "struct" role in Python -- a convenient way to pass around a little logical, fixed size 
bundle of values. A function that needs to return multiple values can just return a tuple of the values. For example, 
if I wanted to have a list of 3-d coordinates, the natural python representation would be a list of tuples, where each 
tuple is size 3 holding one (x, y, z) group.

To create a tuple, just list the values within parenthesis separated by commas. The "empty" tuple is just an empty pair
of parenthesis. Accessing the elements in a tuple is just like a list -- len(), [ ], for, in, etc. all work the same.
"""
print('\nTuples')
tuple_example = (1, 2, 'hi')
print(len(tuple_example))  # 3
print(tuple_example[2])  # hi
# tuple_example[2] = 'bye'  # NO, tuples cannot be changed
tuple_example = (1, 2, 'bye')  # this works

"""
List Comprehensions
A list comprehension is a compact way to write an expression that expands to a whole list. Suppose we have a list nums 
[1, 2, 3, 4], here is the list comprehension to compute a list of their squares [1, 4, 9, 16]:
"""
print('\nList Comprehensions')

comp_nums_list = [1, 2, 3, 4]
squares = [n * n for n in comp_nums_list]  # [1, 4, 9, 16]
print('Original List')
print(comp_nums_list)
print('Comprehensions List')
print(squares)


comp_strs_list = ['hello', 'and', 'goodbye']
shouting = [s.upper() + ' !!!' for s in comp_strs_list]  # ['HELLO!!!', 'AND!!!', 'GOODBYE!!!']
print('\nOriginal List')
print(comp_strs_list)
print('Comprehensions List')
print(shouting)

"""
You can add an if test to the right of the for-loop to narrow the result. The if test is evaluated for each element, 
including only the elements where the test is true.
"""
comp_nums_if_list = [2, 8, 1, 6]  # Select values <= 2
small = [n for n in comp_nums_if_list if n <= 2]  # [2, 1]
print('\nOriginal List')
print(comp_nums_if_list)
print('Comprehensions List')
print(small)

comp_fruits_if_list = ['apple', 'cherry', 'banana', 'lemon']  # Select fruits containing 'a', change to upper case
afruits = [s.upper() for s in comp_fruits_if_list if 'a' in s]  # ['APPLE', 'BANANA']
print('\nOriginal List')
print(comp_fruits_if_list)
print('Comprehensions List')
print(afruits)


