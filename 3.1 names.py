Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print(names[0])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(names[0])
          ^^^^^
NameError: name 'names' is not defined
>>> names = ['ron', 'tyler', 'dani']
>>> print(names[0])
ron
>>> print(names[1])
tyler
>>> print(names[2])
dani
>>> print(names[3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(names[3])
          ~~~~~^^^
IndexError: list index out of range
>>> names = ['Rocko', 'Betsy', 'Pako']
>>> print(names[1])
Betsy
>>> print(names[2])
Pako
>>> print(names[3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(names[3])
          ~~~~~^^^
IndexError: list index out of range
>>> print(names[1])
Betsy
>>> print(names[2])
Pako
>>> print(names[3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(names[3])
          ~~~~~^^^
IndexError: list index out of range
>>> print(names[0])
Rocko
>>> print(names[1])
Betsy
>>> print(names[2])
Pako
>>> print(names[1])