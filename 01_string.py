#String in python are the sequence of Charachers that are 
# enclosed in quotes

# In python we can create Single quoted, and Multi quoted strings

a = 34
b ="Mahesh"
c = " Mahesh's "  #We can use double quote strings in python
print(a,b)

print(type(a))

print(type(b))


# Slicing of String in Python
# Meaning of slice is as to make parts or divide in parts

name = "Mahesh"   #My Name is Mahesh

print(name[0:3])

print(name[1:4])

print(name [:4])  #It is same as name[0:4]

print(name[1:])  # It is same as name[1:5]

# Negative Indices in python

# Negative indices always starts from -1 and it work in a reverse way

print(name[-4:-1])

# Slicing with the skip value in python

#We can provide a skip value 
name1 = "MaheshIsCool"
print("This is prvious value : ", name1[0:13])

d = name1[0::2]  # Every 2nd character in string is skiped

d = name1[0: : 3] # Every 3rd character in string is skiped

print("This is new value : ", d)

