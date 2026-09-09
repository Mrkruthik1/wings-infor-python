num=15 #prime is divisible my 1 and itself

count=0

for i in range(1,num+1):
    if num%i==0:
        count+=1
print(count)

if count==2:
    print("prime")
else:
    print("not a prime")




