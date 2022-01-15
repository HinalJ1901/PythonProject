
# hinal kanani
# Id No : 20CE039
# Aim : Set

# a. Write a Python program to add member(s) in a set and clear a set.

print("----------Set Que:a ----------")

Set1 = {'Green', 'Red', 'Blue'}
print("set1 =",Set1)
Set1.add('Yellow')
print("After adding element Set1 =",Set1)
Set1.clear()
print("After using clear funtion Set1 =",Set1)
 

#b. Write a Python program to remove an item from a set if it is present in the set.

print("----------Set Que:b ----------")

Set2 = {'Python', 'Java', 'English'}
lang = input("Enter the language you want to remove from the set =")
print("you remove the language = ",lang)
# remove English from the set
if lang in Set2:
    Set2.remove(lang)
    print("After removing" ,lang," language set =",Set2)
else:
    print("This language is allready not in Set.")


#c. Write a Python program to create an intersection, Union, difference of sets.

print("----------Set Que:c ----------")
# sets are define
A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}
print("set A =",A)
print("set B =",B)  

# union
print("Union :", A | B)
print('A Union B using funtion =', A.union(B))
  
# intersection
print("Intersection :", A & B)
print('A intersection B using funtion=', A.intersection(B))
  
# difference
print("A Difference B :", A - B)
print("B Difference A :", B - A)

# Equivalent to A-B
print('A Difference B using funtion =', A.difference(B))

# Equivalent to B-A
print('B Difference A using funtion =', B.difference(A))

#d.Write a Python program to find maximum and the minimum value in a set.

print("----------Set Que:d ----------")

Set3 = {8, 10, 3, 15, 2, 39}

print("Original set elements:",Set3)
print("Maximum value of the set:",max(Set3))
print("Minimum value of the set:",min(Set3))


#e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
print("----------Set Que:e ----------")

print("-----For list-----")
List = [2, 1, 2, 2, 1, 3]
counter = 0
num = List[0]
for i in List:
    # The count() method returns the number of occurrences of a number in the given List.
    curr_frequency = List.count(i)
    if (curr_frequency > counter):
         counter = curr_frequency
         num = i

print("List = ",List)
print("the most common elements is : ",num)
print("Frequency of most repeted number is: ", counter)

print("-----For Tuple-----")
tuple=(1,2,4,5,6,6,3,6,8,3,6)
L=list(tuple)
counter1 = 0
num1 = L[0]
for i in L:
# The count() method returns the number of occurrences of a number in the given Tuple.
    curr_frequency = L.count(i)
    if(curr_frequency> counter1):
        counter1 = curr_frequency
        num1 = i
print("the most common elements is: ",num1)
print("Frequency of most repeted number is: ",counter1)

print("-----For dictionary-----")
dic={1:'hinal',2:'harmi',3:'sharad',4:'hinal',5:'jay',6:'sharad',7:'jay',8:'hinal',9:'bhavdeep'}
# values() method returns list of all values which are in dictionary 
value=dic.values()
# convert values in list to count frequncy
l1=list(value)
counter1 = 0
name= list(l1[0])
for i in l1:
    curr_frequency = l1.count(i)
    if(curr_frequency> counter1):
        counter1 = curr_frequency
        name = i
print("the most common elements is: ",name)
print("Frequency of most repeted number is: ",counter1)

