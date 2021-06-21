my_name = "Kara"
print("Hello and welcome " + my_name + "!")

print("Hello world!")


x = 3    # int
y = 6.3  # float
z = kb   # complex


# if statement with indentation
a = 33
b = 603
if b > a:
  print("b is greater than a")


# This is a comment
# written on
# more than just one line
print("Hello, World!")


# Python Lists
# 1 of 4 built-in data types (the others are Tuple, Set, and Dictionary)
my_list = ["apple", "banana", "cherry"]


# The key function for working with files in Python is the open() function.
# To open a file for reading it is enough to specify the name of the file:
f = open("demofile.txt")


# functions
def my_function():
  print("Hello from a function")

my_function()


# arguments
def my_function(fname):
  print(fname + " Seville")

my_function("Alvin")
my_function("Simon")
my_function("Theodore")


# arbitrary keyword arguments
# if you do not know how many keyword arguments that will be passed into your
# function, add two asterisks before the parameter name in the function definition.
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


# default parameter value
# if a function is called without a parameter value, it uses the default value
def my_function(country = "United States"):
  print("I am from " + country)

my_function()


# passing a list as an argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["peach", "blueberry", "cherry"]

my_function(fruits)
