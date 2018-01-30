<!-- page_number: true -->

# About Python

From Wikipedia:
- Python is a widely used __high-level__, __general-purpose__, __interpreted__, __dynamic programming language__. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. The language provides constructs intended to enable clear programs on both a small and large scale.

- Adapted from [learnxinyminutes.com](https://learnxinyminutes.com/)

---
## You have numbers
```
3  # => 3
```

## Math is what you would expect
```
1 + 1=> 2
8 - 1   # => 7
10 * 2  # => 20
```

## Except division which returns floats, real numbers, by default
```
35 / 5  # => 7.0
```

---
## Result of integer division truncated down both for positive and negative.
```
5 // 3       # => 1
5.0 // 3.0   # => 1.0 # works on floats too
-5 // 3      # => -2
-5.0 // 3.0  # => -2.0
```

## When you use a float, results are floats
```
3 * 2.0  # => 6.0
```

## Modulo operation
```
7 % 3  # => 1
```

---
## Exponentiation (`x**y`, `x` to the `yth` power)
```
2**4  # => 16
```

## Enforce precedence with parentheses
```
(1 + 3) * 2  # => 8
```

---
## Boolean values are primitives (note: the capitalization)
```
True
False
```

## Negate with not
```
not True   # => False
not False  # => True
```

## Boolean Operators, note `and` and `or` are case-sensitive
```
True and False  # => False
False or True   # => True
```

---
## Note using Bool operators with ints
```
0 and 2     # => 0
-5 or 0     # => -5
0 == False  # => True
2 == True   # => False
1 == True   # => True
```

## Equality is `==`
```
1 == 1  # => True
2 == 1  # => False
```

## Inequality is `!=`
```
1 != 1  # => False
2 != 1  # => True
```

---
## More comparisons
```
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True
```

## Comparisons can be chained!
```
1 < 2 < 3  # => True
2 < 3 < 2  # => False
```

---
## (`is` vs. `==`) `is` checks if two variables refer to the same object, but `==` checks if the objects pointed to have the same values.
```
a = [1, 2, 3, 4]  # Point a at a new list, [1, 2, 3, 4]
b = a             # Point b at what a is pointing to
b is a            # => True, a and b refer to the same object
b == a            # => True, a's and b's objects are equal
b = [1, 2, 3, 4]  # Point b at a new list, [1, 2, 3, 4]
b is a            # => False, a and b do not refer to the same object
b == a            # => True, a's and b's objects are equal
```

---
## Strings are created with " or '
```
"This is a string."
'This is also a string.'
```

---
## Strings can be added too!, but try not to do this.
```
"Hello " + "world!"  # => "Hello world!"
```

## Strings can be added without using `+`
```
"Hello " "world!"    # => "Hello world!"
```

## A string can be treated like a list of characters
```
"This is a string"[0]  # => 'T'
```

---
## `.format` can be used to format strings, like this:
```
"{} can be {}".format("Strings", "interpolated")
# => "Strings can be interpolated"
```

## You can repeat the formatting arguments to save some typing.
```
"{0} be nimble, {0} be quick, {0} jump over the {1}" \ 
   .format("Jack", "candle stick")
# => "Jack be nimble, Jack be quick, Jack jump over 
#       the candle stick"
```

---
## You can use keywords if you don't want to count
```
"{name} wants to eat {food}" \
  .format(name="Bob", food="lasagna") 
# => "Bob wants to eat lasagna"
```

### If your Python 3 code also needs to run on Python 2.5 and below, you can also still use the old style of formatting:
```
"%s can be %s the %s way" % \ 
    ("Strings", "interpolated", "old")
# => "Strings can be interpolated the old way"
```

---
## None is an object
```
None  # => None
```

---
### Don't use the equality `==` symbol to compare objects to `None`
### Use `is` instead. This checks for equality of object identity.
```
"etc" is None  # => False
None is None   # => True
```

### `None`, `0`, and empty strings/lists/dicts all evaluate to False.
### All other values are True
```
bool(0)   # => False
bool("")  # => False
bool([])  # => False
bool({})  # => False
```

---
# Stop and Think

You will need to write a format string which prints out the data using the following syntax:

"Hello, __name__ __last_name__. Your current balance is $__balance__".

```
data = ("John", "Doe", 53.44)
format_string = "Hello ...?"
```

---
# 2. Variables and Collections

---
## Python has a print function
```
print("I'm Python. Nice to meet you!")
```

- By default the print function also prints out a newline at the end.
- Use the optional argument end to change the end character.
```
print("Hello, World", end="!")
```

---
## Simple way to get input data from console
```
input_string_var = input("Enter some data: ")
# Returns the data as a string
```
- Note: In earlier versions of Python, `input()` method was named as `raw_input()`

---
## No need to declare variables before assigning to them.
- Convention is to use `lower_case_with_underscores`
```
some_var = 5
some_var
```

---
# Stop and Think
The target of this exercise is to create a string, an integer, and a floating point number. The string should be named mystring and should contain the word "hello". The floating point number should be named myfloat and should contain the number 10, and the integer should be named myint and should contain the number 20.

```
# testing code
if mystring == "hello":
    print "String: %s" % mystring
if isinstance(myfloat, float) and myfloat == 10.0:
    print "Float: %d" % myfloat
if isinstance(myint, int) and myint == 20:
    print "Integer: %d" % myint
```

---
## Accessing a previously unassigned variable is an exception.
```
some_unknown_var  # Raises a NameError
```

---
## if can be used as an expression
```
"yahoo!" if 3 > 2 else 2
```

---
## Lists store sequences
```
li = []
```
## You can start with a prefilled list
```
other_li = [4, 5, 6]
```

## Add stuff to the end of a list with append
```
li.append(1)    # li is now [1]
li.append(2)    # li is now [1, 2]
li.append(4)    # li is now [1, 2, 4]
li.append(3)    # li is now [1, 2, 4, 3]
```

---
## Remove from the end with pop
```
li.pop()        # => 3 and li is now [1, 2, 4]
```
## Let's put it back
```
li.append(3)    # li is now [1, 2, 4, 3] again.
```

---
## Access a list like you would any array
```
li[0]   # => 1
```
## Look at the last element
```
li[-1]  # => 3
```

## Looking out of bounds is an IndexError
```
li[4]  # Raises an IndexError
```

---
## You can look at ranges with slice syntax. (It's a closed/open range for you mathy types.)
```
li[1:3]   # => [2, 4]
```
## Omit the beginning
```
li[2:]    # => [4, 3]
```
## Omit the end
```
li[:3]    # => [1, 2, 4]
```
---
## Select every second entry
```
li[::2]   # =>[1, 4]
```
## Return a reversed copy of the list
```
li[::-1]  # => [3, 4, 2, 1]
```
## Use any combination of these to make advanced slices
```
li[start:end:step]
```

---
## Make a one layer deep copy using slices
```
li2 = li[:] 
# => li2 = [1, 2, 4, 3],
# but (li2 is li) will result in False.
```

## Remove arbitrary elements from a list with `del`
```
del li[2]  # li is now [1, 2, 3]
```

## Remove first occurrence of a value
```
li.remove(2)  # li is now [1, 3]
li.remove(2)  # Raises a ValueError as 2 is not in li
```

---
## Insert an element at a specific index
```
li.insert(1, 2)  # li is now [1, 2, 3] again
```

## Get the index of the first item found matching the argument
```
li.index(2)  # => 1
li.index(4)  # Raises a ValueError as 4 is not in li
```

---
## You can add lists, note: values for li and for other_li are not modified.
```
li + other_li  # => [1, 2, 3, 4, 5, 6]
```

## Concatenate lists with `extend()`
```
li.extend(other_li)  # Now li is [1, 2, 3, 4, 5, 6]
```

## Check for existence in a list with `in`
```
1 in li  # => True
```

## Examine the length with `len()`
```
len(li)  # => 6
```

---
# Stop and Think

In this exercise, you will need to add numbers and strings to the correct lists using the `append` list method. You must add the numbers 1,2, and 3 to the `numbers` list, and the words 'hello' and 'world' to the strings variable.

You will also have to fill in the variable second_name with the second name in the names list, using the brackets operator []. Note that the index is zero-based, so if you want to access the second item in the list, its index will be 1.
```
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]
```

---
## Tuples are like lists but are immutable.
```
tup = (1, 2, 3)
tup[0]      # => 1
tup[0] = 3  # Raises a TypeError
```

----
## Note that a tuple of length one has to have a comma after the last element but tuples of other lengths, even zero, do not.
```
type((1))   # => <class 'int'>
type((1,))  # => <class 'tuple'>
type(())    # => <class 'tuple'>
```

---
## You can do most of the list operations on tuples too
```
len(tup)         # => 3
tup + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)
tup[:2]          # => (1, 2)
2 in tup         # => True
```

---
## You can unpack tuples (or lists) into variables
```
a, b, c = (1, 2, 3) 
# a is now 1, b is now 2 and c is now 3
```
## You can also do extended unpacking
```
a, *b, c = (1, 2, 3, 4)
# a is now 1, b is now [2, 3] and c is now 4
```
## Tuples are created by default if you leave out the parentheses
```
d, e, f = 4, 5, 6
```
## Now look how easy it is to swap two values
```
e, d = d, e  # d is now 5 and e is now 4
```

---
# Dictionaries store mappings
```
empty_dict = {}
```
## Here is a prefilled dictionary
```
filled_dict = {"one": 1, "two": 2, "three": 3}
```

---
## Note keys for dictionaries have to be immutable types. This is to ensure that the key can be converted to a constant hash value for quick look-ups.
- Immutable types include `ints`, `floats`, `strings`, `tuples`.
```
invalid_dict = {[1,2,3]: "123"}
# => Raises a TypeError: unhashable type: 'list'
valid_dict = {(1,2,3):[1,2,3]}
# Values can be of any type, however.
```

---
## Look up values with `[]`
```
filled_dict["one"]  # => 1
```

## Get all keys as an iterable with `keys()`. We need to wrap the call in `list()` to turn it into a list. Dictionary key ordering is not guaranteed.
```
list(filled_dict.keys())  # => ["three", "two", "one"]
```

---
## Get all values as an iterable with `values()`. Once again we need to wrap it in `list()` to get it out of the iterable.
```
list(filled_dict.values())  # => [3, 2, 1]
```

---
## Check for existence of keys in a dictionary with "in"
```
"one" in filled_dict  # => True
1 in filled_dict      # => False
```

## Looking up a non-existing key is a `KeyError`
```
filled_dict["four"]  # KeyError
```

---
## Use `get()` method to avoid the `KeyError`
```
filled_dict.get("one")      # => 1
filled_dict.get("four")     # => None
```

## The get method supports a default argument when the value is missing
```
filled_dict.get("one", 4)   # => 1
filled_dict.get("four", 4)  # => 4
```

---
## `setdefault()` inserts into a dictionary only if the given key isn't present
```
filled_dict.setdefault("five", 5)  # filled_dict["five"] is set to 5
filled_dict.setdefault("five", 6)  # filled_dict["five"] is still 5
```

## Adding to a dictionary
```
filled_dict.update({"four":4}) 
# => {"one": 1, "two": 2, "three": 3, "four": 4}
filled_dict["four"] = 4 # another way to add to dict
```

---
## Remove keys from a dictionary with `del`
```
del filled_dict["one"]  # Removes the key "one" from filled dict
```

## From Python 3.5 you can also use the additional unpacking options
```
{'a': 1, **{'b': 2}}  # => {'a': 1, 'b': 2}
{'a': 1, **{'a': 2}}  # => {'a': 2}
```

---
## Sets store ... well sets
```
empty_set = set()
```
## Initialize a set with a bunch of values. Yeah, it looks a bit like a dict. Sorry.
```
some_set = {1, 1, 2, 2, 3, 4}
# some_set is now {1, 2, 3, 4}
```

## Similar to keys of a dictionary, elements of a set have to be immutable.
```
invalid_set = {[1], 1}
# => Raises a TypeError: unhashable type: 'list'
valid_set = {(1,), 1}
```

---
## Can set new variables to a `set`
```
filled_set = some_set
```

## Add one more item to the `set`
```
filled_set.add(5)  # filled_set is now {1, 2, 3, 4, 5}
```

## Do set intersection with `&`
```
other_set = {3, 4, 5, 6}
filled_set & other_set  # => {3, 4, 5}
```

## Do set union with `|`
```
filled_set | other_set  # => {1, 2, 3, 4, 5, 6}
```

---
## Do set difference with `-`
```
{1, 2, 3, 4} - {2, 3, 5}  # => {1, 4}
```

## Do set symmetric difference with `^`
```
{1, 2, 3, 4} ^ {2, 3, 5}  # => {1, 4, 5}
```

## Check if set on the left is a superset of set on the right
```
{1, 2} >= {1, 2, 3} # => False
```

## Check if set on the left is a subset of set on the right
```
{1, 2} <= {1, 2, 3} # => True
```

---
## Check for existence in a set with in
```
2 in filled_set   # => True
10 in filled_set  # => False
```

---
# Stop and Think

Add "Jake" to the phonebook with the phone number 938273443, and remove "Jill" from the phonebook.
```
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
```
---
# 3. Control Flow and Iterables

---
## Let's just make a variable
```
some_var = 11
```

## Here is an if statement. __Indentation is significant in python!__
```
# prints "some_var is smaller than 10"
if some_var > 10:
    print("some_var is totally bigger than 10.")
elif some_var < 10:    # This elif clause is optional.
    print("some_var is smaller than 10.")
else:                  # This is optional too.
    print("some_var is indeed 10.")
```

---
## For loops iterate over lists
```
for animal in ["dog", "cat", "mouse"]:
    # You can use format to interpolate formatted
    # strings
    print("{} is a mammal".format(animal))
```

---
## `range(number)` returns an iterable of numbers from zero to the given number
```
for i in range(4):
    print(i)
```

---
## `range(lower, upper)` returns an iterable of numbers from the lower number to the upper number
```
for i in range(4, 8):
    print(i)
```

---
## `range(lower, upper, step)` returns an iterable of numbers from the lower number to the upper number, while incrementing by step. If step is not indicated, the default value is 1.
```
for i in range(4, 8, 2):
    print(i)
```

---
## While loops go until a condition is no longer met.
```
x = 0
while x < 4:
    print(x)
    x += 1  # Shorthand for x = x + 1
```

---
## Handle exceptions with a try/except block
```
try:
    # Use "raise" to raise an error
    raise IndexError("This is an index error")
except IndexError as e:
    pass                 # Pass is just a no-op. Usually you would do recovery here.
except (TypeError, NameError):
    pass                 # Multiple exceptions can be handled together, if required.
else:                    # Optional clause to the try/except block. Must follow all except blocks
    print("All good!")   # Runs only if the code in try raises no exceptions
finally:                 #  Execute under all circumstances
    print("We can clean up resources here")
```

---
## Instead of try/finally to cleanup resources you can use a with statement
```
with open("myfile.txt") as f:
    for line in f:
        print(line)
```

---
## Python offers a fundamental abstraction called the Iterable.
- An iterable is an object that can be treated as a sequence.
- The object returned the range function, is an iterable.
```
filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable) 
# => dict_keys(['one', 'two', 'three']).
# This is an object that implements our Iterable interface.
```

---
## We can loop over it.
```
for i in our_iterable:
    print(i)  # Prints one, two, three
```

## However we cannot address elements by index.
```
our_iterable[1]  # Raises a TypeError
```

---
## An iterable is an object that knows how to create an iterator.
```
our_iterator = iter(our_iterable)
```

## Our iterator is an object that can remember the state as we traverse through it.
- We get the next object with `next()`.
```
next(our_iterator)  # => "one"
```

## It maintains state as we iterate.
```
next(our_iterator)  # => "two"
next(our_iterator)  # => "three"
```

---
## After the iterator has returned all of its data, it gives you a StopIterator Exception
```
next(our_iterator)  # Raises StopIteration
```

---
## You can grab all the elements of an iterator by calling list() on it.
```
list(filled_dict.keys())
# => Returns ["one", "two", "three"]
```

---
# Stop and Think
- Change the variables in the first section, so that each if statement resolves as `True`.
```
number = 16
second_number = 0
first_array = [1, 2, 3]
second_array = [1,2]

if number > 15:
    print("1")
if first_array:
    print("2")
if len(second_array) == 2:
    print("3")
if len(first_array) + len(second_array) == 5:
    print("4")
if first_array and first_array[0] == 1:
    print("5")
if not second_number:
    print("6")
```

---
- Loop through and print out all even numbers from the numbers list in the same order they are received. Don't print any numbers that come after 237 in the sequence.
```
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980,
    507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617,
    865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386,
    462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978,
    328, 615, 953, 345, 399, 162, 758, 219, 918, 238, 412,
    566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67,
    104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843,
    831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854,
    685, 93, 857, 440, 380, 126, 721, 328, 753, 470,743, 527
]
```

---
# 4. Functions

---
## Use `def` to create new functions
```
def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y  # Return values with a return statement
```

## Calling functions with parameters
```
print(add(5, 6))
```

---
## Another way to call functions is with keyword arguments
```
add(y=6, x=5) # Keyword arguments can arrive in any order.
```

## You can define functions that take a variable number of positional arguments
```
def varargs(*args):
    return args

varargs(1, 2, 3)  # => (1, 2, 3)
```

---
## You can define functions that take a variable number of keyword arguments, as well
```
def keyword_args(**kwargs):
    return kwargs
```

## Let's call it to see what happens
```
keyword_args(big="foot", loch="ness")
# => {"big": "foot", "loch": "ness"}
```

---
## You can do both at once, if you like
```
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)
```

---
## When calling functions, you can do the opposite of args/kwargs!
- Use `*` to expand tuples and use `**` to expand kwargs.
```
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)      # equivalent to foo(1, 2, 3, 4)
all_the_args(**kwargs)   # equivalent to foo(a=3, b=4)
all_the_args(*args, **kwargs)
# equivalent to foo(1, 2, 3, 4, a=3, b=4)
```

---
## Returning multiple values (with tuple assignments)
```
def swap(x, y):
    return y, x  # parenthesis can be excluded.
x = 1
y = 2
x, y = swap(x, y)     # => x = 2, y = 1
# (x, y) = swap(x,y) 
```

---
## Function Scope
```
x = 5

def set_x(num):
    # Local var x not the same as global variable x
    x = num    # => 43
    print (x)  # => 43

def set_global_x(num):
    global x
    print (x)  # => 5
    x = num    # global var x is now set to 6
    print (x)  # => 6

set_x(43)
set_global_x(6)
```

---
## Python has first class functions
```
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(3)   # => 13
```

---
## There are also anonymous functions
```
(lambda x: x > 2)(3)                  # => True
square = (lambda x, y: x ** 2 + y ** 2)
square(5,2)
```

---
## There are built-in higher order functions
```
list(map(add_10, [1, 2, 3]))          # => [11, 12, 13]
list(map(max, [1, 2, 3], [4, 2, 1]))  # => [4, 2, 3]

list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))  # => [6, 7]
```

---
## We can use list comprehensions for nice maps and filters
- List comprehension stores the output as a list which can itself be a nested list
```
[add_10(i) for i in [1, 2, 3]]         # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6, 7]
```

---
# Stop and Think
In this exercise you'll use an existing function, and while adding your own to create a fully functional program.

- Add a function named `list_benefits()` that returns the following list of strings: "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

- Add a function named `build_sentence(info)` which receives a single argument containing a string and returns a sentence starting with the given string and ending with the string " is a benefit of functions!"

- Run and see all the functions work together!

---
## Modify this function to concatenate to each benefit - " is a benefit of functions!"
```
def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
```

---
## 5. Classes

---
## We use the "class" operator to get a class
```
class Human:

    # A class attribute. It is shared by all instances of
    # this class
    species = "H. sapiens"

    # Basic initializer, this is called when this class
    # is instantiated.
    # Note that the double leading and trailing
    # underscores denote objects or attributes that are
    # used by python but that live in user-controlled
    # namespaces. Methods(or objects or attributes) 
    # like: __init__, __str__, __repr__ etc. are called
    # magic methods (or sometimes called dunder methods)
    # You should not invent such names on your own.
    def __init__(self, name):
        # Assign the argument to the instance's name
        # attribute
        self.name = name

        # Initialize property
        self.age = 0
```

---
```
    # An instance method. All methods take "self" as the first argument
    def say(self, msg):
        return "{name}: {message}".format(name=self.name, message=msg)

    # A class method is shared among all instances
    # They are called with the calling class as the first argument
    @classmethod
    def get_species(cls):
        return cls.species

    # A static method is called without a class or instance reference
    @staticmethod
    def grunt():
        return "*grunt*"

    # A property is just like a getter.
    # It turns the method age() into an read-only attribute
    # of the same name.
    @property
    def age(self):
        return self._age
```

---
```
    age = 0
    # This allows the property to be set
    @age.setter
    def age(self, age):
        if type(age) != type(0):
            raise AgeError
        self._age = age

    # This allows the property to be deleted
    @age.deleter
    def age(self):
        del self._age
        
h = Human()
h.age = []
```

---
## Instantiate a class
```
i = Human("Ian")
print(i.say("hi"))

j = Human("Joel")
print(j.say("hello"))
```

---
## Call our class method
```
i.get_species()
```

## Change the shared attribute
```
Human.species = "H. neanderthalensis"
i.get_species()  # => "H. neanderthalensis"
j.get_species()  # => "H. neanderthalensis"
```

---
## Call the static method
```
Human.grunt()    # => "*grunt*"
```

## Update the property
```
i.age = 42
```

## Get the property
```
i.age # => 42
```

## Delete the property
```
del i.age
i.age  # => raises an AttributeError
```

---
# Stop and Think
We have a class defined for vehicles. Create two new vehicles called car1 and car2. Set car1 to be a red convertible worth \$60,000 with a name of Fer, and car2 to be a blue van named Jump worth \$10,000.
```
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    
    def __init__(self, name, kind, color, value):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value
    
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
```

---
# 6. Modules

---
## You can import modules
```
import math
print(math.sqrt(16))  # => 4.0
```

---
## You can get specific functions from a module
```
from math import ceil, floor
print(ceil(3.7))   # => 4.0
print(floor(3.7))  # => 3.0
```

---
## You can import all functions from a module.
- Warning: this is not recommended
```
from math import *
```

## You can shorten module names
```
import math as m
math.sqrt(16) == m.sqrt(16)  # => True
```

---
## Python modules are just ordinary python files. You can write your own, and import them. The name of the module is the same as the name of the file.

- You can find out which functions and attributes defines a module.
```
import math
dir(math)
```

## If you have a Python script named `math.py` in the same folder as your current script, the file `math.py` will be loaded instead of the built-in Python module. This happens because the local folder has priority over Python's built-in libraries.

---
# Stop and Think

In this exercise, you will need to print an alphabetically sorted list of all functions in the re module, which contain the word match.

---
## 7. Advanced

---
## Generators help you make lazy code
```
def double_numbers(iterable):
    for i in iterable:
        yield i + i
```

---
## A generator creates values on the fly.
- Instead of generating and returning all values at once it creates one in each iteration.  This means values bigger than 15 wont be processed in double_numbers.
- We use a trailing underscore in variable names when we want to use a name that would normally collide with a python keyword
```
range_ = range(1, 900000000)
# will double all numbers until a result >=30 found
for i in double_numbers(range_):
    print(i)
    if i >= 30:
        break
```

---
## Decorators
- In this example `beg` wraps `say`
- Beg will call say. If say_please is True then it will change the returned message
```
from functools import wraps
def beg(target_function):
  @wraps(target_function)
  def wrapper(*args, **kwargs):
    msg, say_please = target_function(*args, **kwargs)
    if say_please:
      return "{} {}".format(msg, "Please!")
    return msg

  return wrapper
@beg
def say(say_please=False):
  msg = "Can you buy me a beer?"
  return msg, say_please

print(say())                #Can you buy me a beer?
print(say(say_please=True)) #Can you buy me a beer? Please!
```

---
# Stop and Think
Write a __generator__ function which returns the Fibonacci series. They are calculated using the following formula: 
- The first two numbers of the series is always equal to 1
- Each consecutive number returned is the sum of the last two numbers.
- Hint: Can you use only two variables in the generator function? Remember that assignments can be done simultaneously.
```
a = 1
b = 2
a, b = b, a
```

---
```
def fib():
  a = 0
  b = 1
  while True:
    pass # this is a null statement which does nothing,
         # useful as a placeholder.
```

## Testing code
```
import types
if type(fib()) == types.GeneratorType:
    print ("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
```
