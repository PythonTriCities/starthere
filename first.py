#!/usr/bin/env python3

# Any line that begins with a # is a comment.

# Use a Python built in function to do something:
# https://docs.python.org/3/library/functions.html
# We will use input() and print()
# and a variable named, name.

name = input('Please type in a name: ')
print('Hello, ' + name)
print('Hello, {}'.format(name))
print('Hello, %s' % name)
