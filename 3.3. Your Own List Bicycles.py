Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>  bicycles = ['trek', 'cannondale', 'redline', 'specialized']

  File "<stdin>", line 1
    bicycles = ['trek', 'cannondale', 'redline', 'specialized']
IndentationError: unexpected indent
>>> >>> message = f"My first bicycle was a {bicycles[0].title()}."

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    message = f"My first bicycle was a {bicycles[0].title()}."
                                        ^^^^^^^^
NameError: name 'bicycles' is not defined
>>> >>> print(message)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(message)
          ^^^^^^^
NameError: name 'message' is not defined
>>> print(message)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(message)
          ^^^^^^^
NameError: name 'message' is not defined
>>>  bicycles = ['trek', 'cannondale', 'redline', 'specialized']
  File "<stdin>", line 1
    bicycles = ['trek', 'cannondale', 'redline', 'specialized']
IndentationError: unexpected indent
>>> print(message)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(message)
          ^^^^^^^
NameError: name 'message' is not defined
>>> print(message1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(message1)
          ^^^^^^^^
NameError: name 'message1' is not defined
>>> bicycles = ['trek', 'cannondale', 'redline', 'specialized']

>>> >>> u message = f"My first bicycle was a {bicycles[0].title()}."

  File "<stdin>", line 1
    u message = f"My first bicycle was a {bicycles[0].title()}."
      ^^^^^^^
SyntaxError: invalid syntax
>>> >>> u message = f"My first bicycle was a {bicycles[0].title()}."
  File "<stdin>", line 1
    u message = f"My first bicycle was a {bicycles[0].title()}."
      ^^^^^^^
SyntaxError: invalid syntax
>>> print({bicycles[0])
  File "<stdin>", line 1
    print({bicycles[0])
                      ^
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> print(bicycles[0]
... print(bicycles[1]
  File "<stdin>", line 1
    print(bicycles[0]
          ^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(bicycles[2]
... prin{bicycles[0].title()}."t({bicycles[0].title()}."
  File "<stdin>", line 1
    print(bicycles[2]
          ^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> u message = f"My first bicycle was a {bicycles[0].title()}."
  File "<stdin>", line 1
    u message = f"My first bicycle was a {bicycles[0].title()}."
      ^^^^^^^
SyntaxError: invalid syntax
>>> ng that value. 
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
  File "<stdin>", line 1
    ng that value. 
       ^^^^
SyntaxError: invalid syntax
` message = f"My first bicycle was a {bicycles[0].title()}."
>>> print(message)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(message)
          ^^^^^^^
NameError: name 'message' is not defined
>>> print(bicycles[1])
cannondale
>>> print(bicycles[2])
redline
>>> print(bicycles[3])
specialized
>>> print(bicycles[4])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(bicycles[4])
          ~~~~~~~~^^^
IndexError: list index out of range
>>> print(bicycles[0])
trek
>>> 