# Dictionary In Python

'''
Python Dictionary is the unordered colliction of items
Each iteam of the dictionary has a key/value pair

Dictionaries are optimized to retrive values
when the key is known



 Creating a Python Dictionary

In order to create the dictionary in python we need 
Place the items inside curly braces {} seperated by commas.

An item has a key and corrosponding value and is 
expressed as a (key:value).

While value can be any data type and can be repeat
key must be immutable type(string, number or tuple with 
immutable elements) and must be unique.



'''

#Empty dictionary

my_dict = {}

#Dictionary with integer keys
my_dict = {1:'apple', 2:'ball'}

#Dictionary with mixed keys
my_dict1={'name':'John', 1:[2,3,4]}

#Using dict()

my_dict2 = dict({1:'apple',2:'ball'})

# Create dictionary from sequence having 
my_dict3 = dict([(1,'apple'),(2,'ball')])
