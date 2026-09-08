thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

print("--------------------------------")

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)