def my_function():
    print("Hello good morning")

my_function()

def my_function(fname):
    print(fname + " Hello")

my_function("monday")
my_function("Tuesday")
my_function("wednesday")


#This function expects 2 arguments, and gets 2 arguments:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


def my_function(*kids):
  print("The youngest child is " + kids[0])

my_function("Emil", "Tobias", "Linus")


#Default Parameter Value

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


def my_function(country = " Nigeria"):
    print("I am form" + country)
my_function()
my_function(" lagos")

 #Passing a List as an Argument

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

