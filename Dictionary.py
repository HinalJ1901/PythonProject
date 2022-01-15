# hinal kanani
# Id No : 20CE039
# Aim : Dictionary


# a. Write a Python script to check whether a given key already exists in a dictionary.
print("----------Dictionary Que:a----------")
Dic = {'Hinal': 18,'Jay': 19, 'Harmi': 20,'meet': 21,'sharad': 17}
name = input("Enter the name :")
print('you enter this name:',name)
if name in Dic:
    print('Key is present in the dictionary')
else:
    print('Key is not present in the dictionary')


# b. Write a Python script to merge two Python dictionaries.
print("----------Dictionary Que:b----------")
Dic1 = {'a': 100,'b': 200}
Dic2 = {'c': 300,'d' :400}
Dic3 = Dic1.copy()
Dic3.update(Dic2)
print("Aftre updating Dic5=",Dic3)

# Using funtion
combined_Dic = {**Dic1,**Dic2}
print("Aftre updating Dic5=",combined_Dic)

# c. Write a Python program to sum all the items in a dictionary.
print("----------Dictionary Que:c----------")
Dic4 = {'a': 100, 'b':200, 'c':300}
sum1 =0
for i in Dic4.values():
    sum1 = sum1 + i
print("sum = ",sum1)

# Using Sum funtion
print("Sum =",sum(Dic4.values()))

# d. Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
print("----------Dictionary Que:d----------")
Dic5= {0:10, 1:20}
print("Befor updatind Dic5 =",Dic5)
Dic5[2]=30
print("Aftre updating Dic5=",Dic5)

# Using update funtion
Dic5.update({2:30})
print("Aftre updating Dic5=",Dic5)

# e. Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60
print("----------Dictionary Que:e----------")
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
print("dic1 =",dic1)
print("dic2 =",dic2)
print("dic3 =",dic3)
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print("After concatenate=",dic4)

dic5 ={**dic1,**dic2,**dic3}
print("After concatenate=",dic4)