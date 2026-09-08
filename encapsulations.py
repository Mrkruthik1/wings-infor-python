#encapsulations

class bank:
    def __init__(self,name,accountpass):
       self.name=name
       self.__accountpass=accountpass
    def get__accountpass(self):
        return self.__accountpass

b=bank("kruthik",1234)
print(b.name)
"""print(b.__accountpass)   this is private " double underscore (__variable)"   """

print("-------------------------------")
class bank:
    def __init__(self,name,accountpass):
       self.name=name
       self.__accountpass=accountpass
    def get__accountpass(self):
        return self.__accountpass
b=bank("k",101)
print(b.get__accountpass()) 


print("-------------------------------")

class account:
    def __init__(self, name, password):
        self.name = name
        self.__password = password

    def get__password(self):
        return self.__password

    def set__password(self, password):
        if password > 0:
            self.__password = password
        else:
            print("pass should be positive")


a = account("modi", -1)

print(a.get__password())   # -1

a.set__password(1)

print(a.get__password())   # 1

