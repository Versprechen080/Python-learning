# using format() method
print('I love {} for "{}!"'.format('Geeks', 'Geeks'))

# using format() method and referring
# a position of the object
print('{0} and {1}'.format('Geeks', 'Portal'))
print('{1} and {0}'.format('Geeks', 'Portal'))

print(f"I love {'Geeks'} for \"{'Geeks'}!\"")
print(f"{'Geeks'} and {'Portal'}")

print("Second argument: {1:3d}, first one: {0:7.2f}".
      format(47.42, 11))


# Python program to
# show format() is
# used in dictionary
data = dict(fun="GeeksForGeeks", adj="Portal")

# using format() in dictionary
print("I love {fun} computer {adj}".format(**data))

tab = {'geeks': 4127, 'for': 4098, 'geek': 8637678,'another':121212}

# using format() in dictionary
print('Geeks: {0[geeks]:d}; For: {0[for]:d}; '
      'Geeks: {0[geek]:d};Haha: {0[another]:d}'.format(tab))

# Formatting output using the String method
cstr="I love geeksforgeeks"
# Printing the center aligned
# string with fillchr
print("Center aligned string with fillchr: ")
print(cstr.center(40,'#'))

# Printing the left aligned
# string with "-" padding
print ("The left aligned string is : ")
print (cstr.ljust(40, '-'))

# Printing the right aligned string
# with "-" padding
print ("The right aligned string is : ")
print (cstr.rjust(40, '-')) #20 is the smallest value