# x = y = z = 0
# print(x)
# print(y)
# print(z)
# coord = [0, 0, 0]
# x, y, z = coord
# print(x)
# print(y)
# print(z)

# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)


# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)

# x = 210
# y = 3
# print(x * y)
# z = "sad"
# print(y, z)


# global and local
# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)

# //////////////////////////
# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)

# //////////////////////////
# import random

# print(random.randrange(1, 10))


# //////////////////////////
# a = "Hello, World!"
# print(len(a))

# //////////////////////////
# a = "Hi everybody, I am Mxo"
# print("am" in a)

# //////////////////////////
# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")

# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")

# # sliceing
# print(txt[1:8])
# print(txt[:8])
# print(txt[4:])

# b = " Hello, World! "
# print(b[-5:-2])
# print(b.upper())
# print(b.upper())
# print(b.strip())

# a = "Hello, World!"
# print(a.replace("H", "J"))
# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']


# combine strings and numbers
# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))

# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))


# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))

# txt = "banana"

# x = txt.center(10, "O")

# print(x)

# ///////////////////////
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]

# print(newlist)
# ///////////////////////
# copy list
# 1
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)
# 2
# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

# join lists
# 1
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

# 2
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)
# print(list1)

# 3
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)

# Change Tuple Values

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)

# Add tuple to a tuple.
# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)


# ############################################################################
# ############################################################################
# ############################################################################
# ####################################FAST####################################
# ############################################################################
# ############################################################################
# ############################################################################

# num = int(input("enter number: "))
# print(num + 2)



# x = int(input("Grade: "))

# print("A") if 90 < x <= 100 else print('B') if 80 < x <= 90 \
#     else print('C') if 70 < x <=80 else print('D') if 60 < x <= 70 else print('F')

# age = int(input('Enetr your age: '))
# print('Invalid age!!!') if age < 0 else print('child') if age <= 14 else print('young') if age <= 24 else print('adult') if age <= 64 else print('senior')

# nahanj tari
year = int(input('Enetr year: '))
print('Leap year') if year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0) else print('not leap year')
