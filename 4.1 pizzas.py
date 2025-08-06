Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']

>>> >>> # Print the names of all the pizzas.
>>> for pizza in favorite_pizzas:
... print("\n")
  File "<stdin>", line 2
    print("\n")
    ^^^^^
IndentationError: expected an indented block after 'for' statement on line 1
>>> for pizza in favorite_pizzas:
... print("\n")
  File "<stdin>", line 2
    print("\n")
    ^^^^^
IndentationError: expected an indented block after 'for' statement on line 1
>>> # Print a sentence about each pizza.
>>> for pizza in favorite_pizzas:
... print("I really love " + pizza + " pizza!")

  File "<stdin>", line 2
    print("I really love " + pizza + " pizza!")
    ^^^^^
IndentationError: expected an indented block after 'for' statement on line 1
>>> >>> print("\nI really love pizza!")

I really love pizza!
>>> favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
>>> 'pepperoni'
'pepperoni'
>>> for favorite_pizzas

  File "<stdin>", line 1
    for favorite_pizzas
                       ^
SyntaxError: invalid syntax
>>> >>> for pizzas
  File "<stdin>", line 1
    for pizzas
              ^
SyntaxError: invalid syntax
>>> favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
>>> favorite_pizzas = ['pepperoni']
>>> favorite_pizzas = ['hawaiian']
>>> 
>>> >>> print(name.rstrip())
>>>   File "<stdin>", line 1
    >>> >>> print(name.rstrip())
    ^^
SyntaxError: invalid syntax
>>> favorite_pizzas = ['veggie']
>>> # Print the names of all the pizzas.
>>> favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
>>> print("\n I really love pizza!")

 I really love pizza!
print("\n I really love pepperoni pizza!")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    t("\n I really love pepperoni pizza!")
    ^
NameError: name 't' is not defined
>>> print("\n I really love pizza!")

 I really love pizza!
>>> print("\n I really love pepperoni pizza!")

 I really love pepperoni pizza!
>>> print("\n I really love hawaiian pizza!")

 I really love hawaiian pizza!
>>> print("\n I really love veggie pizza!")

 I really love veggie pizza!
>>> 