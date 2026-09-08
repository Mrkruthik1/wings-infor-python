
class myplaylist:
    def __init__(self,name):
        self.name=name
        self.songs=[]

    def addsong(self,song):
        self.songs.append(song)
        print(f'song {song} added to playlist')

    def removesong(self,song):
        for song in self.songs:
            self.songs.remove(song)
            print(f'remove this {song}')

    def display(self):
        print(f'here is your {self.name} playlist')
        i=1
        for song in self.songs:
            print(f'{i}.{song}')
            i+=1

play=myplaylist("Favorites")
play.addsong("bahubali")
play.display()
print("----------------")
play.addsong("billa")
play.display()
print("----------------")
play.removesong("bahubali")
play.display()
print("----------------")
play.addsong("ram")
play.display()
print("----------------")




class person:
    def __init__(self,name):
        self.name=name


    def greet(self):
        print("hello")

    def respect(self):
        print(f'mr.{self.name}')

p=person("kruthik")

del person.greet
#p.greet    #error

p.respect()


class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print(self.l*self.b)

r1=rectangle(2,10)
r1.area()

