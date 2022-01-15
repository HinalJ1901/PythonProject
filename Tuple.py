# hinal kanani
# Id No : 20CE039
# Aim : Tuple

# a. Write a Python program to create a tuple with different data types.

print("----------Tuple Que:a----------")
tuple1 = ("Hinal", False, 3.2, 1)
print("tuple =",tuple1)

# b. Write a Python program to create a tuple with numbers and print one item.

print("----------Tuple Que:b----------")
#Create a tuple with numbers
tuple2 = (8, 10, 15, 20, 25,39)
print(" tuple with one item =",tuple2[0])

#Create a tuple of one item
tuple3 = (8,)
print(" tuple with one item=",tuple3)



# c. Write a Python program to add an item in a tuple.

print("----------Tuple Que:c----------")
#create a tuple
tuple4 = (4, 6, 2, 8, 3, 1) 
print("tuple=",tuple4)
print("tuples are immutable, so you can not add new elements")

#using merge of tuples with the + operator you can add an element and it will create a new tuple
tuple4 = tuple4 + (9,)
print("Afert adding an element, tuple = ",tuple4)

#adding items in a specific index
tuple4 = tuple4[:5] + (15, 20, 25) + tuple4[:5]
print("After adding items in a specific index ,tuple = ",tuple4)

# d. Write a Python program to convert a tuple to a string.
print("----------Tuple Que:d----------")

tuple5 = ('h','e','l','l','o')

# Use str.join() to convert tuple to string.
str = ''.join(tuple5)
print(type(tuple5))
print ("After converting tuple to string = ",str)
print(type(str))

# Use for loop to convert tuple to string.
str2 = ''
for item in tuple5:
    str2 = str2 + item
print(type(tuple5))
print ("After converting tuple to string = ",str2)
print(type(str2))

# e. Write a Python program to find the length of a tuple.
print("----------Tuple Que:e----------")

tuple6 = (20,32,14,25,45,56)
print(tuple6)
#use the len() function to known the length of tuple
print("length of tuple=",len(tuple6))