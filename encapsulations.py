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

print("------------------------------------")

class Student:
  def __init__(self, name):
    self.name = name
    self.__grade = 0

  def set_grade(self, grade):
    if 0 <= grade <= 100:
      self.__grade = grade
    else:
      print("Grade must be between 0 and 100")

  def get_grade(self):
    return self.__grade

  def get_status(self):
    if self.__grade >= 60:
      return "Passed"
    else:
      return "Failed"

student = Student("Emil")
student.set_grade(85)
print(student.get_grade())
print(student.get_status())

print("--------------------------------------")
    
class Person:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary # Protected property

p1 = Person("Linus", 50000)
print(p1.name)
print(p1._salary)

