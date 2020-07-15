# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(x):
    check = x%2
    if check == 0:
        return "Even!"
    else:
        return "Odd"

# Read a number from the keyboard
# num = input("Enter a number: ")
# num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
for i in range(5):
    num = input("Enter a number: ")
    num = int(num)
    val = is_even(num)
    print(val)

