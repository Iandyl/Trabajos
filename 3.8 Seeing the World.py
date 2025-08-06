Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> #3-8: Seeing the World

>>> >>> locations = ['himalaya', 'andes', 'tierra del fuego', 'labrador', 'guam', 'mazatlan']

>>> >>> print("Original order:")
Original order:
>>> print(locations)

['himalaya', 'andes', 'tierra del fuego', 'labrador', 'guam', 'mazatlan']
>>> >>> print("\nAlphabetical:")

Alphabetical:
>>> print(sorted(locations))
['andes', 'guam', 'himalaya', 'labrador', 'mazatlan', 'tierra del fuego']
>>> print("\nOriginal order:")


Original order:
>>> >>> print(locations)
['himalaya', 'andes', 'tierra del fuego', 'labrador', 'guam', 'mazatlan']
>>> print("\nReverse alphabetical:")


Reverse alphabetical:
>>> >>> print(sorted(locations, reverse=True))

['tierra del fuego', 'mazatlan', 'labrador', 'himalaya', 'guam', 'andes']
>>> >>> print("\nOriginal order:")

Original order:
>>> print(locations)
['himalaya', 'andes', 'tierra del fuego', 'labrador', 'guam', 'mazatlan']
>>> print("\nReversed:")

Reversed:
>>> locations.reverse()
>>> print(locations)
['mazatlan', 'guam', 'labrador', 'tierra del fuego', 'andes', 'himalaya']
>>> print("\nOriginal order:")

Original order:
>>> locations.reverse()
>>> print(locations)
['himalaya', 'andes', 'tierra del fuego', 'labrador', 'guam', 'mazatlan']
>>> print("\nAlphabetical")

Alphabetical
>>> locations.sort()
>>> print(locations)
['andes', 'guam', 'himalaya', 'labrador', 'mazatlan', 'tierra del fuego']
>>> print("\nReverse alphabetical")

Reverse alphabetical
>>> locations.sort(reverse=True)
>>> print(locations)
['tierra del fuego', 'mazatlan', 'labrador', 'himalaya', 'guam', 'andes']
>>> print("\nAlphabetical:")