Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 3.7: Shrinking Guest List
  File "<stdin>", line 1
    3.7: Shrinking Guest List
    ^^^
SyntaxError: illegal target for annotation
>>> 3.7 Shrinking Guest List
  File "<stdin>", line 1
    3.7 Shrinking Guest List
        ^^^^^^^^^
SyntaxError: invalid syntax
>>> #3.7 Shrinking Guest List
>>> # Invite some people to dinner.

>>> >>> guests = ['guido van rossum', 'jack turner', 'lynn hill']
>>> name = guests[0].title()
>>> print(f"{name}, please come to dinner.")
Guido Van Rossum, please come to dinner.
>>> name = guests[1].title()
>>> print(f"{name}, please come to dinner.")
Jack Turner, please come to dinner.
>>> name = guests[2].title()
>>> print(f"{name}, please come to dinner.")
Lynn Hill, please come to dinner.
>>> name = guests[0].title()
>>> print(f"\nSorry, {name} can't make it to dinner.")


Sorry, Guido Van Rossum can't make it to dinner.
>>> >>> name = guests[1].title()
>>> print(f"\nSorry, {name} can't make it to dinner.")

Sorry, Jack Turner can't make it to dinner.
>>> name = guests[2].title()
>>> print(f"\nSorry, {name} can't make it to dinner.")

Sorry, Lynn Hill can't make it to dinner.
>>> name = guests[3].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[3].title()
           ~~~~~~^^^
IndexError: list index out of range
>>> name = guests[4].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[4].title()
           ~~~~~~^^^
IndexError: list index out of range
>>> print(f"\nSorry, {name} can't make it to dinner.")

Sorry, Lynn Hill can't make it to dinner.
>>> # Jack can't make it! Let's invite Gary instead.

>>> >>> del(guests[1])
>>> guests.insert(1, 'gary snyder')
>>> # Print the invitations again.
>>> name = guests[0].title()
>>> print(f"\n{name}, please come to dinner.")

Guido Van Rossum, please come to dinner.
>>> name = guests[1].title()
>>> print(f"{name}, please come to dinner.")
Gary Snyder, please come to dinner.
>>> name = guests[2].title()
>>> print(f"{name}, please come to dinner.")
Lynn Hill, please come to dinner.
>>> # We got a bigger table, so let's add some more people to the list.
>>> print(f"{name}, please come to dinner.")

Lynn Hill, please come to dinner.
>>> >>> name = guests[2].title()
>>> print(f"{name}, please come to dinner.")
Lynn Hill, please come to dinner.
>>> name = guests[3].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[3].title()
           ~~~~~~^^^
IndexError: list index out of range
>>> name = guests[4].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[4].title()
           ~~~~~~^^^
IndexError: list index out of range
>>> name = guests[5].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[5].title()
           ~~~~~~^^^
IndexError: list index out of range
>>> name = guests[6].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[6].title()
           ~~~~~~^^^
IndexError: list index out of range
>>> name = guests[7].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[7].title()
           ~~~~~~^^^
IndexError: list index out of range
>>> print(f"{name}, please come to dinner.")
Lynn Hill, please come to dinner.
>>> name = guests[6].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[6].title()
           ~~~~~~^^^
IndexError: list index out of range
>>> name = guests[8].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[8].title()
           ~~~~~~^^^
IndexError: list index out of range
>>> name = guests[9].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[9].title()
           ~~~~~~^^^
IndexError: list index out of range
>>> # Oh no, the table won't arrive on time!

>>> >>> print("\nSorry, we can only invite two people to dinner.")

Sorry, we can only invite two people to dinner.
>>> name = guests.pop()

>>> >>> print(f"Sorry, {name.title()} there's no room at the table.")
Sorry, Lynn Hill there's no room at the table.
>>> name = guests.pop()
>>> print(f"Sorry, {name.title()} there's no room at the table.")
Sorry, Gary Snyder there's no room at the table.
>>> name = guests.pop()
>>> print(f"Sorry, {name.title()} there's no room at the table.")

Sorry, Guido Van Rossum there's no room at the table.
>>> >>> name = guests.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests.pop()
IndexError: pop from empty list
>>> name = guests.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests.pop()
IndexError: pop from empty list
>>> print(f"Sorry, {name.title()} there's no room at the table.")

Sorry, Guido Van Rossum there's no room at the table.
>>> >>> # There should be two people left. Let's invite them.
>>> name = guests[0].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[0].title()
           ~~~~~~^^^
IndexError: list index out of range
>>> name = guests[1].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[1].title()
           ~~~~~~^^^
IndexError: list index out of range
>>> name = guests[2].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[2].title()
           ~~~~~~^^^
IndexError: list index out of range
>>> name = guests[3].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[3].title()
           ~~~~~~^^^
IndexError: list index out of range
>>> name = guests[4].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[4].title()
           ~~~~~~^^^
IndexError: list index out of range
>>> name = guests[5].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[5].title()
           ~~~~~~^^^
IndexError: list index out of range
>>> name = guests[6].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[6].title()
           ~~~~~~^^^
IndexError: list index out of range
>>> name = guests[7].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[7].title()
           ~~~~~~^^^
IndexError: list index out of range
>>> name = guests[8].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[8].title()
           ~~~~~~^^^
IndexError: list index out of range
>>> name = guests[9].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[9].title()
           ~~~~~~^^^
IndexError: list index out of range
>>> name = guests[10].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[10].title()
           ~~~~~~^^^^
IndexError: list index out of range
>>> name = guests[11].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[11].title()
           ~~~~~~^^^^
IndexError: list index out of range
>>> name = guests[12].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[12].title()
           ~~~~~~^^^^
IndexError: list index out of range
>>> name = guests[13].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[13].title()
           ~~~~~~^^^^
IndexError: list index out of range
>>> print(f"{name}, please come to dinner.")

guido van rossum, please come to dinner.
>>> >>> name = guests[1].title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    name = guests[1].title()
           ~~~~~~^^^
IndexError: list index out of range
>>> print(f"{name}, please come to dinner.")
guido van rossum, please come to dinner.
>>> # Empty out the list.

>>> >>> del(guests[0])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    del(guests[0])
        ~~~~~~^^^
IndexError: list assignment index out of range
>>> del(guests[0])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    del(guests[0])
        ~~~~~~^^^
IndexError: list assignment index out of range
>>> # Prove the list is empty.
>>> print(guests)
[]
>>> print(guests)
[]
>>> 