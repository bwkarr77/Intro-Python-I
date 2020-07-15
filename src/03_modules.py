"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
# - Run this file in the terminal!! In the terminal, cd into src, then type:
#   - py 03_modules.py something1 something2
#       - 'py' for python, <filename> <input1> <input2>
mySys = sys.argv
print(mySys)
for i in mySys:
    print(i)
    # prints mySys[i]

# Print out the OS platform you're using:
# YOUR CODE HERE
print(sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
print(sys.version_info)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print(os.getcwdb())

# Print out your machine's login name
# YOUR CODE HERE
print(os.getlogin())
