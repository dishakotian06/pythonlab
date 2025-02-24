n = int(input("Enter the number of the terms:"))
a, b = 0,1
print("Fibonacci Series:", end=" ")
for i in range(n):
  print(a, end=" ")
  a, b = b, a+b