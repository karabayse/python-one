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


# the pass statement
# put in the pass statement to avoid getting an error for empty function definitions
def myfunction():
  pass


# recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


# lambda function
# small anonymous function
x = lambda a : a + 10
print(x(5))


# arrays
colors = ["red", "yellow", "blue"]
colors.append("green")
colors.pop("red")


# classes
class MyClass:
  x = 5


# init function
class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Dog("Kernel", 3)

print(p1.name)
print(p1.age)


# iterators
mytuple = ("strawberry", "blueberry", "blackberry")
myit = iter(mytuple)
