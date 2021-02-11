"""
Python has a built-in string class named "str" with many handy features (there is an older module named "string"
which you should not use). String literals can be enclosed by either double or single quotes, although single quotes
are more commonly used.

Python strings are "immutable" which means they cannot be changed after they are created
"""

s = 'hi'
print(s[1])  # i
print(len(s))  # 2
print(s + ' there')  # hi there

pi = 3.14
# text = 'The value of pi is ' + pi      # NO, does not work
text = 'The value of pi is ' + str(pi)  # yes

raw = r'this\t\n and that'
print(raw)  # prints - this\t\n and that

multi = """It was the best of times.
It was the worst of times."""
print(multi)  # prints below multi line
# It was the best of times.
# It was the worst of times.

# % operator
text = "%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down." % (3, 'huff', 'puff', 'house')
print(text)

speed = 80
if speed >= 80:
    print('License and registration please')
    mood = input('Please enter your mood: ')
    if mood == 'terrible' or speed >= 100:
        print('You have the right to remain silent.')
    elif mood == 'bad' or speed >= 90:
        print("I'm going to have to write you a ticket.")
    else:
        print("Let's try to keep it under 80 ok?")
