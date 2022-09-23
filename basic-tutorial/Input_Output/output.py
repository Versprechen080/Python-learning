# end= ” ” statement
# Example: Python print() without new line
print("hello",end=",")
print("welcome to my house")

# flush Argument
import time
count_seconds=3
for i in reversed(range(count_seconds+1)):
    if i>0:
        print(i,end='>>>')
        time.sleep(1)
    else:
        print('Start')
# Now, set the flush argument as true and again see the results.
import time
count_seconds=3
for i in reversed(range(count_seconds+1)):
    if i>0:
        print(i,end='>>>',flush=True)
        time.sleep(1)
    else:
        print('Start')

# Separator
a=21
b=9
c=2022
print(a,b,c,sep='-')

# file Argument
import io
# declare a dummy file 声明一个虚拟文件
dummy_file=io.StringIO()
# add message to the dummy file
print('Hello Geeks!',file=dummy_file)
# get the value from dummy file
print(dummy_file.getvalue())