# n=141
# nk=str(n)
# print(nk[::-1])


# s=int(input("enter numbers :"))
# s=str(s)
# if s==s[::-1]:
#     print("palandrom")
# else:
#     print("not a palandrom")


# print("-------------------------")


s="iaia"
rev=""
s=str(s)

for i in s:
    rev=i+rev
if s==rev:
    print("palandrom")
else:
    print("not a palandrom")

