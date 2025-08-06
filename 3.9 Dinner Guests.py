Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> #3-9 Dinner Guests.py
>>> guests = ['nemuel', 'rico', 'orgado']

>>> >>> going = []

>>> >>> not_going = []
>>> dinnertable = []
>>> print(f"{guests[0].title()} is going for the dinner tonight.")
Nemuel is going for the dinner tonight.
>>> print(f"{guests[1].title()} is going for the dinner tonight.")
Rico is going for the dinner tonight.
>>> print(f"{guests[2].title()} is going for the dinner tonight.")
Orgado is going for the dinner tonight.
>>> going.append(guests[0])
>>> going.append(guests[1])
>>> not_going.append(guests[2])
>>> dinnertable.append(guests[0])
>>> dinnertable.append(guests[1])
>>> print(f"These 2 people are going {going[0].title()} and {going[1].title()}.")
These 2 people are going Nemuel and Rico.
>>> uninvited_guests = ['jana', 'alex', 'therese']
>>> party_crashers = []
>>> party_crashers.append(uninvited_guests[0])
>>> party_crashers.append(uninvited_guests[1])
>>> party_crashers.append(uninvited_guests[2])
>>> dinnertable.append(party_crashers[0])
>>> dinnertable.append(party_crashers[1])
>>> dinnertable.append(party_crashers[2])
>>> print(f"The dinner table now occupies more people. {dinnertable}")

The dinner table now occupies more people. ['nemuel', 'rico', 'jana', 'alex', 'therese']
>>> >>> print(f"The number of guests invited to the dinner party is {len(guests)}.")
The number of guests invited to the dinner party is 3.
>>> print(f"The number of people that are going to dine on the dinner table is {len(dinnertable)}.")
The number of people that are going to dine on the dinner table is 5.
>>> 