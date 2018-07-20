"""This is my file

This is the first python file I have written.
"""
"""
print('Hello World')

if 1 ==2:
    print('wut')
else:
    print('ha')
x = 1
while x < 5:
    print(x)
    print('HA')
    #x +=1
    #add one to x
    #other ways to increment x

"""
"""
for val in range (15, 100):
    print('{val} is divisible by 2: {dunno}'.format(
    val=val, dunno = val%2 == 0))

for thing in range(5):
    print(thing)
for thing in "hello":
    print(thing)

myList = [1,2,3,4,5]

for bOOm in myList:
    print(bOOm)

for val in range (15, 100):
    print('{val} is divisible by 2: {dunno}'.format(
    val=val, dunno = val%2 == 0))
"""
def myFunction() :
    for val in range(1, 16):
        three = val%5==0
        two = val%3==0
        if(three == True and two == True):
            print("fizzbuzz")
        elif(three == True):
            print("fizz")
        elif(two == True):
            print("buzz")
        else:
            print(val)
myFunction()
def fizz(val):
    print("{f}{b}".format(
    f = "Fizz" if val % 3 == 0, else "",
    b = "buzz" if val % 5 == 0, else ""))
"""

Function: Tests and prints values within a certain range.
Args:
    val: the value which is being tests
    f: tests if the value is divisible by 3
    b: tests if the value is divisible by 5
"""
fizz(val)
def print_person(first, middle_name =None, last_name):
    middle_name = middle_name or ''
    print('{f}{m}{l}'.format(f=first, m=middle_name,l=last_name))
print_person('Sally', 'Sue')
""" Prints person Name
pep 8 and pep 257
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""




myDic = {'a': 1, 'b': 2, 'c': 3, 'd': 5}
for key,value in myDic.items():
    if key == 'a':
        print(key) + str(value)















#wow
