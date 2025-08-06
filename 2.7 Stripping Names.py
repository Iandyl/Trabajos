Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> name = "\tRocko Pablo\n"
>>> print(name)
	Rocko Pablo

>>> print("\nUsing lstrip():")


Using lstrip():
>>> >>> print(name.lstrip())

Rocko Pablo

>>> >>> print("\nUsing rstrip():")


Using rstrip():
>>> >>> 
>>> >>> print(name.rstrip())
>>>   File "<stdin>", line 1
    >>> >>> print(name.rstrip())
    ^^
SyntaxError: invalid syntax
>>> print("\nUsing rstrip():")

Using rstrip():
>>> print(name.rstrip())

	Rocko Pablo
>>> >>> print("\nUsing strip():")

Using strip():
>>> print(name.strip())
Rocko Pablo
>>> 