x = lambda a : a + 10

print(x(5))

print("--------------------------------")

x = lambda a, b : a * b
print(x(5, 6))

print("--------------------------------")

def myfunc(n):
  print(n)
  return lambda a : a * n


mydoubler = myfunc(2)

print(mydoubler(11))


