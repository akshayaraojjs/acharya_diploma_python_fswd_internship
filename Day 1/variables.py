# Int
num = 15
print(num)
print(type(num))

# Float
pi = 3.142
print(pi)
print(type(pi))

# String
name = "Akshay Rao"
print(name)
print(type(name))

# String
initial = 'J'
print(initial)
print(type(initial))

# Int, float, String & Bool are the primitive datatypes

# Bool
isDeveloper = True
print(isDeveloper)
print(type(isDeveloper))

# List
# List items are Ordered, Chanagable/Mutable & can allow duplicate values
fruits = ["apple", "banana", "cherry", "dragon fruit", 'apple']

print(fruits)
print(type(fruits))

# We can access the list item using its index number
print(fruits[4])

# len() method is used to get the count of list items
print("Number of items in fruits list:", len(fruits))

# append() method is used to add a new item at the end of the list
fruits.append("strawberry")
print("After appending: ", fruits)
fruits.append("jackfruit")
print("After appending: ", fruits)

# insert method is used to add a new item at the specified index position
# insert method expects 2 arguements: "index" & the new "item"
fruits.insert(1, "chickoo")
print("After inserting: ", fruits)

fruits.insert(5, "custard apple")
print("After inserting: ", fruits)

fruits.insert(2, "mango")
print("After inserting: ", fruits)

# remove() method is used to remove the list item
fruits.remove("apple")
print("After removing: ", fruits)
fruits.remove("cherry")
print("After removing: ", fruits)
# If the item is missing, it is going to throw the error 
# fruits.remove("pappaya")
# print("After removing: ", fruits)

# pop() method is used to remove the item using its index number
# We can use it in 2 ways: without argument it will remove the last item, with arguement it will remove the specified item
fruits.pop()
print("After popping: ", fruits)
fruits.pop(2)
print("After popping: ", fruits)

# del keyword: It is dangerous as it is going to remove the variable itself, if we try to access the deleted variable we will get an error
# del fruits

# Positive index:
print("3rd Fruit:", fruits[2])

# Negative index will refer the list from reversed order, last item will start from -1 index
print("Last 3rd Fruit:", fruits[-3])

# Accessing the items through the range:

# Slicing: [start:end] 
# start is inclusive & end is exclusive
print(fruits[1:4])

# Slicing: [start:]
print(fruits[2:])

# Slicing: [:end]
print(fruits[:5])

# Negative slicing [-2:-5]
print(fruits[-3:-1])
# clear() method is used to remove all the items from the list which will make it empty
fruits.clear()
print(fruits)

random_numbers = [2, 5, 9, 15, 16, 2, 5, 7, 2, 5, 2]

numbers = [3, 7, 9, 17]

# random_numbers.append(numbers)
# If we try to append the list with another list, it will store the new list as a single index, so we need to use the extend() method

# extend() method is used to merge two lists
random_numbers.extend(numbers)

print(random_numbers)

numbers_copy = []
print("Before copying", numbers_copy)

# copy() method is used to clone or copy the existing list
numbers_copy = random_numbers.copy()
print("After copying", numbers_copy)

print("2 is duplicated for ", random_numbers.count(2), " times")

# index() method is used to find the position of the given item
print(random_numbers.index(7))

# reverse method is used to change the order of the list
random_numbers.reverse()

print(random_numbers)

# sort() method is used to sort the list items in Ascending(Ascending) or Descending Order
# Ascending order
random_numbers.sort()
print("Ascending Order",random_numbers)
random_numbers.sort(reverse=True)
print("Descending Order",random_numbers)