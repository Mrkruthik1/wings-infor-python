price = 49
txt = "The price is {} dollars"
print(txt.format(price))

print("--------------------------------")

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

print("--------------------------------")

age = 24
name = "kruthik"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))


"""
print("--------------------------------")
print("input")
print("--------------------------------")
name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your favorite animal:")
fav2 = input("What is your favorite color:")
fav3 = input("What is your favorite number:")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")
"""

print("--------------------------------") 

y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x);
    y = False
  except:
    print("Wrong input, please try again.")

print("Thank you!")