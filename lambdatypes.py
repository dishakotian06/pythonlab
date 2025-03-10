#lambda function

square = lambda x:x ** 2
print(square(5))

#lambda with multiple arguments

add = lambda a,b : a + b
print(add(8,5))

#lambda inside map()

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x:x ** 2, numbers))
print (squared)

# lambda inside filter()

numbers = [9, 2, 10, 4, 7]
evens = list(filter(lambda x:x % 2 == 0, numbers))
print(evens)

#lambda inside sorted()

names = ["Disha","Malishka","Inchara","Keerthana","Manasvi"]
sorted_names = sorted(names, key = lambda x:len(x))
print(sorted_names)
