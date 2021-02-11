#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys # this is the regular importing stype
# from sys import argv  # another style to import with short names


# Define a main() function that prints a little greeting.
def main() -> object:
    # Get the name from the command line, using 'World' as a fallback.
    if len(sys.argv) >= 2:
        name = sys.argv[1]
    else:
        name = 'World'
    print('Hello', name)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
