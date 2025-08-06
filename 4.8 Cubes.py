Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> cubes = list(range(1, 11))

>>> >>> for cube in cubes:
... print(cube**3)
  File "<stdin>", line 2
    print(cube**3)
    ^^^^^
IndentationError: expected an indented block after 'for' statement on line 1
>>> cubes = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
>>> print(cube)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(cube)
          ^^^^
NameError: name 'cube' is not defined. Did you mean: 'cubes'?
>>> print(cubes)
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
>>> cubes = []
>>> for value in range(1, 11):
... cubes.append(value**3)
  File "<stdin>", line 2
    cubes.append(value**3)
    ^^^^^
IndentationError: expected an indented block after 'for' statement on line 1
>>> cubes = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
>>> print(cube**3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(cube**3)
          ^^^^
NameError: name 'cube' is not defined. Did you mean: 'cubes'?
>>> print(cubes**3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(cubes**3)
          ~~~~~^^~
TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
>>> cube = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
>>> print(cube**3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(cube**3)
          ~~~~^^~
TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
>>> print(cubes**3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(cubes**3)
          ~~~~~^^~
TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
>>> cubes = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
>>> for cube in cubes:
... print(cube)
  File "<stdin>", line 2
    print(cube)
    ^^^^^
IndentationError: expected an indented block after 'for' statement on line 1
>>> cubes = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
>>> for cube in cubes:
... 
  File "<stdin>", line 2
    
    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>> 
>>> cubes = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
>>> 
>>> for cube in cubes:
... print(cube)
  File "<stdin>", line 2
    print(cube)
    ^^^^^
IndentationError: expected an indented block after 'for' statement on line 1
>>> for cube in cubes:
... print(cubes)
  File "<stdin>", line 2
    print(cubes)
    ^^^^^
IndentationError: expected an indented block after 'for' statement on line 1
>>> print(cube)