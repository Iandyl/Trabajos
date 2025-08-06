Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> # Invite some people to dinner.
>>> guests = ['guido van rossum', 'jack turner', 'lynn hill']
>>> name = guests[0].title()

>>> >>> print(f"{name}, please come to dinner.")

Guido Van Rossum, please come to dinner.
>>> >>> name = guests[1].title()
>>> print(f"{name}, please come to dinner.")
Jack Turner, please come to dinner.
>>> name = guests[2].title()
>>> print(f"{name}, please come to dinner.")
Lynn Hill, please come to dinner.
>>> name = guests[1].title()
>>> print(f"\nSorry, {name} can't make it to dinner.")


Sorry, Jack Turner can't make it to dinner.
>>> >>> name = guests[0].title()
>>> print(f"\nSorry, {name} can't make it to dinner.")

Sorry, Guido Van Rossum can't make it to dinner.
>>> name = guests[2].title()
>>> print(f"\nSorry, {name} can't make it to dinner.")

Sorry, Lynn Hill can't make it to dinner.
>>> name = guests[3].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[3].title()
           ~~~~~~^^^
IndexError: list index out of range
>>> name = guests[3].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[3].title()
           ~~~~~~^^^
IndexError: list index out of range
>>> 