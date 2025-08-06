Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> # Invite some people to dinner.
>>> guests = ['Rex Bernal Valdez', 'Ela del Carmen', 'Toby Bernal Valdez']
>>> name = guests[0].title()
>>> print(f"{name}, please come to dinner.")
Rex Bernal Valdez, please come to dinner.
>>> name = guests[1].title()
>>> print(f"{name}, please come to dinner.")
Ela Del Carmen, please come to dinner.
>>> name = guests[2].title()
>>> print(f"{name}, please come to dinner.")
Toby Bernal Valdez, please come to dinner.
>>> print(f"\nSorry, {name} can't make it to dinner.")


Sorry, Toby Bernal Valdez can't make it to dinner.
>>> >>> name = guests[0].title()
>>> name = guests[1].title()
>>> print(f"\nSorry, {name} can't make it to dinner.")

Sorry, Ela Del Carmen can't make it to dinner.
>>> print(f"\nSorry, {name} can't make it to dinner.")

Sorry, Ela Del Carmen can't make it to dinner.
>>> name = guests[2].title()
>>> print(f"\nSorry, {name} can't make it to dinner.")

Sorry, Toby Bernal Valdez can't make it to dinner.
>>> print(f"\nSorry, {name} can't make it to dinner.")

Sorry, Toby Bernal Valdez can't make it to dinner.
>>> name = guests[0].title()
>>> print(f"\nSorry, {name} can't make it to dinner.")

Sorry, Rex Bernal Valdez can't make it to dinner.
>>> # Print the invitations again.
>>> name = guests[0].title()
>>> print(f"\n{name}, please come to dinner.")


Rex Bernal Valdez, please come to dinner.
>>> >>> name = guests[1].title()

>>> >>> print(f"{name}, please come to dinner.")

Ela Del Carmen, please come to dinner.
>>> >>> name = guests[2].title()
>>> print(f"{name}, please come to dinner.")
Toby Bernal Valdez, please come to dinner.
>>> # We got a bigger table, so let's add some more people to the list.

>>> >>> print("\nWe got a bigger table!")


We got a bigger table!
>>> >>> guests.insert(0, 'frida kahlo')

>>> >>> guests.insert(2, 'reinhold messner')
>>> guests.append('elizabeth peratrovich')

>>> >>> name = guests[0].title()
>>> print(f"{name}, please come to dinner.")
Frida Kahlo, please come to dinner.
>>> name = guests[1].title()
>>> print(f"{name}, please come to dinner.")
Rex Bernal Valdez, please come to dinner.
>>> name = guests[2].title()

>>> >>> print(f"{name}, please come to dinner.")

Reinhold Messner, please come to dinner.
>>> >>> name = guests[3].title()

>>> >>> print(f"{name}, please come to .")

Ela Del Carmen, please come to .
>>> >>> name = guests[4].title()
>>> print(f"{name}, please come to dinner.")
Toby Bernal Valdez, please come to dinner.
>>> name = guests[5].title()
>>> print(f"{name}, please come to dinner.")
Elizabeth Peratrovich, please come to dinner.
>>> 