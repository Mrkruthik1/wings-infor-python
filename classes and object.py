class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f'hello my name is {self.name} and my age is {self.age}')

p1=person("kruthik",24)
print(p1.name)
print(p1.age)
p1.greet()


print("--------------------------------")

class k:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=k("kruthik",24)
print(p1.name)
print(p1.age)

print("--------------------------------")


class dog :
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print(f'My name is {self.name} and my age is {self.age} ... Woof!')
d=dog("husky",2)
d.bark()
print("--------------------------------")


class names:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print(f'well my name is {self.name} & i am {self.age} year"s old')
p1=names("kruthik",24)
p2=names("varun",23)
p1.print()
p2.print()

print("--------------------------------")


# Create the Car class

class car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model    
        self.year=year
    def display(self):
        print(f'this ia my car brand{self.brand} & model is {self.model} & year is {self.year}')

# Create an object
c1=car(" tata","punch",2026)

c2=car(" hyundai","creta",2024)

del c2

# Call the show method
c1.display()
# c2.display()  this is error because it was deleted 













