#
# Example file for variables


# Declare a variable and initialize it
f = 0
print(f)

# # re-declaring the variable works
f = "abc"
print(f)
"0"
# # ERROR: variables of different types cannot be combined
print("percy " + str(23))

# Global vs. local variables in functions


def someFunction():
    global f
    f = "okkk"
    print(f)


someFunction()
print(f)

del f
print(f)
