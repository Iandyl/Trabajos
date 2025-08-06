Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> animals = ["cat", "dog", "hamster"]
>>> 
>>>for animal in animals:

...   File "<stdin>", line 2
    
    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>> print(animal + " will make a great pet!")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(animal + " will make a great pet!")
          ^^^^^^
NameError: name 'animal' is not defined. Did you mean: 'animals'?
>>> print("All these have tails")
All these have tails
>>> animals = ["cat", "dog", "hamster"]
>>> for animal in animals:
...     print(animal + " will make a great pet!")

... cat will make a great pet!
dog will make a great pet!
hamster will make a great pet!
>>> 