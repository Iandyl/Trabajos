Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> #4.6 Odd numbers

>>> >>> even_numbers = list(range(2,21,2))
>>> for number in even_numbers:
... #print each number
... print(number)
  File "<stdin>", line 3
    print(number)
    ^^^^^
IndentationError: expected an indented block after 'for' statement on line 1
>>> odd_numbers = list(range(1, 20, 2))
>>> for number in odd_numbers:
...  print(number)
... 
1
3
5
7
9
11
13
15
17
19
>>> 
>>> 
>>> 