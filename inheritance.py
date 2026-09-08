class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def display(self):
        print(f'welcome mr.{self.fname} {self.lname}')
class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear=year

    def show(self):
        print(f'hello {self.fname}{self.lname}  passout  year is {self.graduationyear}')

s1=student("kruthik","sen",2025)
s1.display()
s1.show()