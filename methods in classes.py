class calculator :
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)

c=calculator()
c.add(10,40)
c.sub(40,10)

print("--------------------------------")

class birthday:
    def __init__(self,day,month,year,name):
        self.day=day
        self.month=month
        self.year=year
        self.name=name
    def happybirthday(self):
        print(f'happy birthday to you {self.name}, on {self.day}/{self.month}/{self.year}  ')

b=birthday(14,21,2002,"kruthik")
b.happybirthday()



print("----------------------------------")









