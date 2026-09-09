f=open("kruthik__1.txt","x")

import os 

if os.path.exists("kruthik__.txt"):
    os.remove("kruthik__.txt")
    print(" deleted")
else:
    print("file does not exist")


