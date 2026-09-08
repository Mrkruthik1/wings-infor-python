#python

print("hello world"); print("well come"); print("this is first python..")

#end=

print("well this is kruthik",end="")
print(" learning new things")           #end= " " =by using this we can write the next print statement in the same line without going to the next line


#maths inside print statement
print(2+3)  #addition
print(2-3)  #subtraction
print(2*3)  #multiplication
print(2/3)  #division


#num+text inside print statement


print("i am kruthik and my age is",20 ) #num+text

print("the sum of 2 and 3 is",2+3)  #addition
print("the difference of 2 and 3 is",5-2)  #subtraction
print("the product of 2 and 3 is",5*5)   #multiplication

#comments start with '#' and are used to explain the code. They are ignored by the interpreter.

name=input("enter your name:")  #input function is used to take input from the user
print("hello",name)  #print function is used to print the output


#hi
#i am kruthik
# this python training
print("hi this is python training in wings")

#multiline string (triple quotes)
"""this is a multiline string
it can span multiple lines
  triple quotes can be used for docstrings and comments"""


"""
count=0
"""
num=10
for i in range(num):
    print(i)  #print numbers from 0 to 9

#variables
"""
a variable is a container that holds a value in it 

"""
x=10
y="hello"
z='K'

print(x,end="")
print(y,end="")
print(z)

#data type

x=int(10)
y=float(5)
z=str("ram")
l=str(44)

print(x)

print(y)

print(z)

print(l)

#variable names
AGE=22
age=33
age=55#more priority
Age=44

print("this is a age ")
print(AGE)
print(age)
print(Age)


x,y,z="kruthik",10,0.5

print(x)
print(y)
print(z)

x=y=z="multi"

print(x)
print(y)
print(z)

fruits=["apple ","banana ","orange"]
x,y,z=fruits
print(x)
print(y)
print(z)



#"+"
print(x+y+z)

print('Hello','World')


#global variables
x="awsome"

def num():
    print("python is "+x)
num()

print("------------")

y="awsome"

def num():
    y="good"
    print("python is "+y)
num()

print("-----------------")

def text():
    global x
    x="good"
    print("python is "+x)
text()
print("so is",x)

print("-------------")
x=5
y="john"
z=0.5
print(type(x))

print(type(y))

print(type(z))

print("--------------")

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

print("-----")

txt="the python is for freee"
if "free" in txt:
    print("yes free is in text")
else:
    print("no free is in text")

print("--------")

k="worlds"
print(k[2:5])

print("-----------")

b = "Hello, World!"
print(b[2:5])

print("------------")

txt="kruthik"
print(txt[:5])
print("------------")

a = " kruthik "
print(a.strip())

k="kruthik"
print(k.split(","))

k="kruhtik"
m=" j"

print(k+m)

print("------------")

print(f"the price is {20} dollars")

print("--------------")

# Create the variable
s="kruthik"
# Print characters from index 2 to 5
print(s[2:5])
# Print in upper case
print(s.upper())
# Create the name variable
carname=" varun"
# Print using an f-string
print(f"the carname is{carname}")

print("------------")

print(10>9)
print("------------")
print(10<9)
print("------------")
print(10==9)
print("------------")

a=10
b=20
if b>a:
    print("b is grater than a")
else:
    print("a is grater than b")

print("------------")

print(bool(0))
print("------------")
print(bool(1))
print("------------")
print(bool(15))
print("------------")
print(bool("kruthik"))
print("------------")


print(bool(["ram","rahul","rambo"]))

print("------------")

def myfun():
    return True
print(myfun())

print("------------")

x=10

print(isinstance(x,int))

print("------------")

numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

print("------------")

num=6

print("holiday" if num>5  else "working day")

print("------------")

num=3

print("fri"if num==5 else "sat" if num==6 else "sun"if num==7 else "working day")

print("------------")
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

print("------------")

x=5

print(1<x<10)
print("------------")


y=6

print(not(y<5 and y<10))

print("------------")

k=6
print(not(k < 5 and k < 10))

print("------------")

v=10
j=10

print(v is j)
print(v is not j)
print("------------")

k=("ram","rahul","rambo")
mylist=list(k)
print(mylist)
print("------------")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print("------------")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
print("------------")
print(thislist[2:])
print("------------")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

print("------------")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[2]="blackcurrent"
print(thislist)

print("------------")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[1:3]=["rawfruit","jackfruit"]
print(thislist)

print("------------")

list=["mango","orange","cherry"]
list.insert(2,"kiwi")
print(list)

print("------------")

l1=["apple"]
l1.append("orange")
print(l1)
l2=["mango","cherry"]
l1.extend(l2)
print(l1)
print("------------")
l1=["apple"]
l2=("mango","orange","cherry")
l1.extend(l2)
print(l1)


print("------------")

l1=["apple","orange","cherry","mango"]
l2=[x for x in l1 if x!="apple"]
print(l2)
l3=[x.upper() for x in l1]
print(l3)
print("------------")

l4=["mango","orange","cherry"]

l5=["hello" for x in l4]
print(l5)
print("------------")

l4=["mango","orange","cherry"]
l5=[x if x!="orange" else "apple" for x in l4]
print(l5)
print("------------")

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

print("------------")
l1=[99,55,66,33,22,11,0]
l1.sort()
print(l1)
print("------------")

l1=[99,55,66,33,22,11,0]
l1.sort(reverse=True)
print(l1)
print("------------")


def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

print("------------")

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
print("------------")

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
print("------------")

tuple=tuple(("mango","apple","pineapple"))
print(tuple)
print("------------")

