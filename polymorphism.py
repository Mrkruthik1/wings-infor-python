#polymorphism

class car:
    def __init__(self,model,color):
        self.model=model
        self.color=color
    def move(self):
        print(f'this {self.model} moves fast , that is my fav {self.color} color')
class bike:
    def __init__(self,type,ps):
        self.type=type
        self.ps=ps
    def move(self):
        print(f'my bike is {type} type , it produce above {self.ps} power')
class laptop:
    def __init__(self, brand , chip):
        self.brand=brand
        self.chip=chip
    def move(self):
        print(f'my laptop is {self.brand}, it  has {self.chip} that is more faster that normal laptop ')

c1=car(" bmw "," black ")
b1=bike(" sports "," 166 ")
l1=laptop("apple","mac M4")

for x in (c1,b1,l1):
    x.move()
    