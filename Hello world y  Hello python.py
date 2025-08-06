Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello Python interpreter!")
Hello Python interpreter!
>>> Type "help"
  File "<stdin>", line 1
    Type "help"
         ^^^^^^
SyntaxError: invalid syntax
>>> Type "help", "copyright", "credits", or "license" for more information.
  File "<stdin>", line 1
    Type "help", "copyright", "credits", or "license" for more information.
         ^^^^^^
SyntaxError: invalid syntax
Type "help"
  File "<stdin>", line 1
    "help"
IndentationError: unexpected indent
>>> >>> print("Hello Python interpreter!")
  File "<stdin>", line 1
    >>> print("Hello Python interpreter!")
    ^^
SyntaxError: invalid syntax
>>>  print("Hello Python interpreter!")
  File "<stdin>", line 1
    print("Hello Python interpreter!")
IndentationError: unexpected indent
>>> print("Hello Python interpreter!")
Hello Python interpreter!
>>> Type "help", "copyright", "credits" or "license" for more information.
  File "<stdin>", line 1
    Type "help", "copyright", "credits" or "license" for more information.
         ^^^^^^
SyntaxError: invalid syntax
>>> Type "help","copyright","credits" or "license" for more information.
  File "<stdin>", line 1
    Type "help","copyright","credits" or "license" for more information.
         ^^^^^^
SyntaxError: invalid syntax
>>> Type "help", "copyright", "credits" or "license" for more information.
  File "<stdin>", line 1
    Type "help", "copyright", "credits" or "license" for more information.
         ^^^^^^
SyntaxError: invalid syntax
>>> Type "help", "copyright", "credits" or "license"
  File "<stdin>", line 1
    Type "help", "copyright", "credits" or "license"
         ^^^^^^
SyntaxError: invalid syntax
>>> Type "help", "copyright", "credits" or "license" for more information.
  File "<stdin>", line 1
    Type "help", "copyright", "credits" or "license" for more information.
         ^^^^^^
SyntaxError: invalid syntax
>>> print("Hello Python world!")
Hello Python world!
>>> message = "Hello Python world!"
>>>message = "Hello Python world!"
print(message)
