# Generally, users use a split() method to split a Python string but one can use it in taking multiple inputs.
x, y = input("Enter two values:").split()
print("Number of boys:", x)
print("Number of girls:", y)
print()  # 空行

a, b = input("Enter two values again: ").split()
print("First number is {} and second number is {}".format(a, b))
print()

# taking multiple inputs at a time
# and type casting using list() function
x = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ", x)

# Using List comprehension:
x,y=[int(x) for x in input("Enter 2 values: ").split()]
print("First Number is ",x)
print("Second Number is ",y)
print("First Number is {} adn second number is {}".format(x,y))
print()

# taking multiple inputs at a time separated by comma
x = [int(x) for x in input("Enter multiple value: ").split(",")]
print("Number of list is: ", x)