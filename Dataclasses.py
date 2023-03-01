# importing the dataclass modules to practice the dataclass functions

"""
default
default_factory
init
repr
hash
compare
metadata
"""

from dataclasses import dataclass,field

@dataclass
class Person:
    name:str
    city:str
    age:int

p1=Person("Aryan","Bareilly",34)
print(p1)    # Person(name='Aryan', city='Bareilly', age=34)

# Now let us also import the filed function which will help us to understand all functions

# Using the default keyword
@dataclass
class Person:
    name:str
    city:str
    age:int=field(default=34)

p3=Person("Aman","Bareilly")
#print(p3)  # Person(name='Aman', city='Bareilly', age=34)

# In default factory we have to provide a function which takes no arguements and return the value which will be taken as the property.

def default_age():
    ages=[1,34,45,65]
    return sum(ages)/len(ages)

@dataclass
class Person:
    name:str
    city:str
    age:int=field(default_factory=default_age)

p3=Person("Aman","Bareilly")
#print(p3)  # Person(name='Aman', city='Bareilly', age=36.25

# if we take off the init values as off then we dont have to initiate the value while creating the object

@dataclass
class Person:
    name:str
    city:str=field(init=False,default="Chandigarh")
    age:int=field(default_factory=default_age)

p3=Person("Aman",45)

#print(p3)  # Person(name='Aman', city='Chandigarh', age=45)

#repr function allow us to set the value of representation such that we can set it off and it will not be in the representation
@dataclass
class Person:
    name:str
    city:str=field(repr=False,default="Chandigarh")
    age:int=field(default_factory=default_age)


p3=Person("Aman")
#print(p3)   # Person(name='Aman', age=36.25)

# With hash function we can set whether the value will be associated or not associated with the hashing operation

@dataclass(unsafe_hash=True)
class Person:
    name:str
    city:str=field(hash=False,default="Chandigarh")
    age:int=field(default_factory=default_age)
p3=Person("Aman")   # Old Value -5603470275351019049

print(hash(p3))     # new values 3000593424381358270


# it means when we set hash=False it do not consider the property while calculating the hash value.

#compare is used in eq default function which will help us to selct column on the basis of which comparsions have to be done,

@dataclass
class Person:
    name:str
    city:str=field(init=False,default="Chandigarh")
    age:int=field(compare=False, default_factory=default_age)


p1=Person("Aman",35)
p3=Person("Aman",34)
#print(p1==p3)    # True


# metadata can be used by third parties to acces the data and format of the data from objects

@dataclass
class Person:
    name:str
    city:str=field(init=False,default="Chandigarh")
    age:int=field(compare=False, default_factory=default_age,metadata={'format':'year'})

p1=Person("Aman",35)
#print(p1.__dataclass_fields__['age'].metadata['format'])    #year
