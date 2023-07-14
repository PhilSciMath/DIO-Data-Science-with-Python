#!/bin/python

# This is about Python dictinaries

# A dictionary is a not ordered set of pairs key/value.
# The keys must be immutable objects. Values can be any object.
# Keys cannot be repeated.


# Creating dictionaries:
person = {"name": "John", "age": 39}
car = dict(brand="Ford", used=False, km_per_litter=50)


# Adding a new key:value pair to person:
person["phone"] = 45321262
print(person)


# Accessing data from a dictionary, use the key as index:
print(person["phone"])
print(car["brand"])


# Nested dictionaries.
students = {
    "student1": {"name": "Sauron", "age": "??", "phone": 66666666},
    "student2": {"name": "Gandalf", "age": "??", "phone": 11111111},
    "student3": {"name": "Frodo", "age": 30, "phone": 22222222}
}
print(students["student2"])
print(students["student2"]["name"])
for i in students: print(students[i], end='\n')

print("\n")
for key, value in students.items():
    print(key, value)

for key in students:
    print(key, students[key]) # same as above


# Methods for dictionaries.


# .copy(), creates a copy:
temp = students.copy()
print('\ncontents of temp:\n', temp)
print('is temp == students? ->', temp == students)


# .clear(), makes a dictionary empty:
print('\nbefore .clean():\n', temp)
temp.clear()
print('\nafter .clean():\n', temp)


# .fromkeys(), creates keys given as arguments with value 'None'
cars = dict.fromkeys(["brand", "year", "color"])
print("\ncars created with dict.fromkeys():\n", cars)


# .get(), returns the value passed as argument, if it exists:
cars["color"] = "yellow"
print("\nchanges color to yellow:\n", cars)
print("\nusing .get('color'):\n", cars.get("color"))


# .items(), returns a list o tuples from the dictionary's items:
print("\ncars.items():\n", cars.items())


# .keys() returns only the dictionary's keys:
print("\ncars.keys():\n", cars.keys())


# .pop(), removes a pair from a dictionary
# .pop("key") is the default, .pop("key", {}) returns the removed pair.
result = students.pop("student2")
print("\nstudents.pop('student2'):\n", students)
print("\nresult:\n", result)


# .popitem() removes a pair, if there is one, doesn't take arguments
result.popitem()
print("\nresult.popitem():\n", result)
result.popitem()
print("\nresult.popitem():\n", result)


# .setdefault() adds a key/value pair if it doesn't exist, else it
# keeps the key/value pair as it is:
result.setdefault("name", "Aragorn")
print("\nresult.setdefault('name', 'Aragorn'):\n", result)
result.setdefault("class", "Wizard")
print("\nresult.setdefault('class', 'Wizard'):\n", result)


# .update() allows to change a value if it exists, else adds it.
result.update({"class": "Mage"})
print("\nresult.update({'class': 'Mage'}):\n", result)
result.update({'age': 80})
print("\nresult.update({'age': 80}):\n", result)


# .values() returns only the values from a dictionary:
print("\nresult.values():\n", result.values())


# we may use 'in' to check if a key exists:
print("\n'name' in result:\n", 'name' in result)


# del -  removes a key/value pair:
del result['age']
print("\ndel result['age']\n", result)
# del result remove the whole result dictionary






