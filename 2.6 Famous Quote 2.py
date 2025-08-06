Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>  famous_person = "Rocko Pablo"

  File "<stdin>", line 1
    famous_person = "Rocko Pablo"
IndentationError: unexpected indent
>>> >>> message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'
                 ^^^^^^^^^^^^^
NameError: name 'famous_person' is not defined
>>> >>> famous_person = "Rocko Pablo"
>>> message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'
>>> print(message)
Rocko Pablo once said, "A person who never made a mistake never tried anything new."
>>> 