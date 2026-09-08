#encapsulations

class bank:
    def __init__(self,name,accountpass):
       self.name=name
       self.__accountpass=accountpass

b=bank("kruthik",1234)
print(b.name)
print(b.__accountpass) # this is private " double underscore (__variable)"
