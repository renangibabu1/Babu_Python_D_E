# DICTIONARY DATATYPE ASSIGNMENT - 50 QUESTIONS
# ============================================

# SOLVED EXAMPLE
# --------------
# Question: Find the key with maximum value in a dictionary
print("SOLVED EXAMPLE:")
print("Find the key with maximum value in a dictionary")
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95, 'Eve': 88}
max_key = max(scores, key=scores.get)
max_value = scores[max_key]
print(f"Dictionary: {scores}")
print(f"Key with maximum value: {max_key}")
print(f"Maximum value: {max_value}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Create a dictionary of student names and their ages
print("Question 1: Create a dictionary of student names and their ages")
# Your code here
students = {
    "Rahul": 21,
    "Anil": 22,
    "Priya": 20,
    "Sneha": 23
}
print(students)
print(students.keys())
students.values()
students.items()
#--------------------------------------------------------------------------------------------------
# Question 2: Add a new key-value pair to dictionary {'a': 1, 'b': 2, 'c': 3}
print("\nQuestion 2: Add a new key-value pair to dictionary {'a': 1, 'b': 2, 'c': 3}")
# Your code here
#--------------------------------------------------------------------------------------------------
# Question 3: Get all keys from dictionary {'name': 'John', 'age': 25, 'city': 'New York'}
print("\nQuestion 3: Get all keys from dictionary {'name': 'John', 'age': 25, 'city': 'New York'}")
# Your code here
students_name = {'name': 'John', 'age': 25, 'city': 'New York'}
students_name.keys()
#--------------------------------------------------------------------------------------------------
# Question 4: Get all values from dictionary {'python': 3, 'java': 2, 'c++': 1}
print("\nQuestion 4: Get all values from dictionary {'python': 3, 'java': 2, 'c++': 1}")
# Your code here
get_values = {'python': 3, 'java': 2, 'c++': 1}
get_values.values()
#--------------------------------------------------------------------------------------------------
# Question 5: Check if key 'age' exists in {'name': 'Alice', 'age': 30, 'city': 'London'}
print("\nQuestion 5: Check if key 'age' exists in {'name': 'Alice', 'age': 30, 'city': 'London'}")
# Your code here
check_keys =  {'name': 'Alice', 'age': 30, 'city': 'London'}
key_values = check_keys.keys()
if 'age' in key_values:
  print('Key "age" exists in the dictionary.')
else:
  print('Key "age" does not exist in the dictionary.')
#--------------------------------------------------------------------------------------------------
# Question 6: Remove key 'temp' from {'a': 1, 'b': 2, 'temp': 3, 'c': 4}
print("\nQuestion 6: Remove key 'temp' from {'a': 1, 'b': 2, 'temp': 3, 'c': 4}")
# Your code here
remove_key = {'a': 1, 'b': 2, 'temp': 3, 'c': 4}
remove_temp = remove_key.pop("temp")
print(remove_key)
#--------------------------------------------------------------------------------------------------
# Question 7: Find the sum of all values in {'math': 85, 'science': 92, 'english': 78}
print("\nQuestion 7: Find the sum of all values in {'math': 85, 'science': 92, 'english': 78}")
# Your code here
student_marks = {'math': 85, 'science': 92, 'english': 78}
sudents_values = student_marks.values()
print(sum(students_values))
#--------------------------------------------------------------------------------------------------
# Question 8: Create a dictionary with squares of numbers 1 to 5
print("\nQuestion 8: Create a dictionary with squares of numbers 1 to 5")
# Your code here
squares = {}
for in range(1,5):
  square[i]=i**2
print(squares)
#--------------------------------------------------------------------------------------------------
# Question 9: Count frequency of each character in string "hello"
print("\nQuestion 9: Count frequency of each character in string 'hello'")
# Your code here
text = "hello"
frequency_count = {}

for char in text:
  # print(char)
  if char in frequency_count:
    frequency_count[char] +=1
  else:
    frequency_count[char] = 1
print(frequency_count)
#--------------------------------------------------------------------------------------------------
# Question 10: Merge two dictionaries {'a': 1, 'b': 2} and {'c': 3, 'd': 4}
print("\nQuestion 10: Merge two dictionaries {'a': 1, 'b': 2} and {'c': 3, 'd': 4}")
# Your code here
dictionary1 = {'a': 1, 'b': 2}
dictionary2 = {'c': 3, 'd': 4}
dictionary1.update(dictionary2)
print(dictionary1)
#--------------------------------------------------------------------------------------------------
# Question 11: Create a nested dictionary: {'person': {'name': 'Alice', 'age': 25}}
print("\nQuestion 11: Create a nested dictionary: {'person': {'name': 'Alice', 'age': 25}}")
# Your code here
person_data={'person': {'name': 'Alice', 'age': 25}}
print(person_data)
person_data['person']['name']
#--------------------------------------------------------------------------------------------------
# Question 12: Access nested value 'name' from {'person': {'name': 'Alice', 'age': 25}}
print("\nQuestion 12: Access nested value 'name' from {'person': {'name': 'Alice', 'age': 25}}")
# Your code here
person_data={'person': {'name': 'Alice', 'age': 25}}
person_data['person']['name']
#--------------------------------------------------------------------------------------------------
# Question 13: Create a dictionary with list values: {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}
print("\nQuestion 13: Create a dictionary with list values: {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}")
# Your code here
dictionary_list = {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}
dictionary_list
#--------------------------------------------------------------------------------------------------
# Question 14: Add 'orange' to the 'fruits' list in nested dictionary
print("\nQuestion 14: Add 'orange' to the 'fruits' list in nested dictionary")
# Your code here
dictionary_list = {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}
dictionary_fruits = dictionary_list["fruits"]
dictionary_fruits.append("orange")
dictionary_list
#--------------------------------------------------------------------------------------------------
# Question 15: Create a dictionary with tuple values: {'coordinates': (10, 20), 'rgb': (255, 0, 0)}
print("\nQuestion 15: Create a dictionary with tuple values: {'coordinates': (10, 20), 'rgb': (255, 0, 0)}")
# Your code here
tuple_dict = {'coordinates': (10, 20), 'rgb': (255, 0, 0)}
print(tuple_dict)
#--------------------------------------------------------------------------------------------------
# Question 16: Extract first coordinate from nested tuple
print("\nQuestion 16: Extract first coordinate from nested tuple")
# Your code here
tuple_dict = {'coordinates': (10, 20), 'rgb': (255, 0, 0)}
tuple_dict['coordinates'][0]
#--------------------------------------------------------------------------------------------------
# Question 17: Create a dictionary with set values: {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}
print("\nQuestion 17: Create a dictionary with set values: {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}")
# Your code here
set_dict = {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}
print(set_dict)
#--------------------------------------------------------------------------------------------------
# Question 18: Add 'o' to vowels set in nested dictionary
print("\nQuestion 18: Add 'o' to vowels set in nested dictionary")
# Your code here
#--------------------------------------------------------------------------------------------------
# Question 19: Create a 3-level nested dictionary: {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}
print("\nQuestion 19: Create a 3-level nested dictionary: {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}")
# Your code here
nested_dict = {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}
print(nested_dict)
#--------------------------------------------------------------------------------------------------
# Question 20: Access employee name from 3-level nested dictionary
print("\nQuestion 20: Access employee name from 3-level nested dictionary")
# Your code here
nested_dict = {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}
nested_dict['company']['department']['employee']['name']
#--------------------------------------------------------------------------------------------------
# Question 21: Create a dictionary with mixed data types: {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}
print("\nQuestion 21: Create a dictionary with mixed data types: {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}")
# Your code here
multiple_dict = {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}
print(multiple_dict)
#--------------------------------------------------------------------------------------------------
# Question 22: Check data type of each value in mixed dictionary
print("\nQuestion 22: Check data type of each value in mixed dictionary")
# Your code here
multiple_dict = {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}
for key,value in multiple_dict.items():
  print(type(value))
#--------------------------------------------------------------------------------------------------
# Question 23: Create a dictionary with function values: {'len': len, 'str': str, 'int': int}
print("\nQuestion 23: Create a dictionary with function values: {'len': len, 'str': str, 'int': int}")
# Your code here
dictionary_function = {'len': len, 'str': str, 'int': int}
print(dictionary_function)
#--------------------------------------------------------------------------------------------------
# Question 24: Apply each function to "123" using dictionary
print("\nQuestion 24: Apply each function to '123' using dictionary")
# Your code here
dictionary_function = {'len': len, 'str': str, 'int': int}
for key, values in dictionary_function.items():
    print(key, values("123"))
#--------------------------------------------------------------------------------------------------
# Question 25: Create a dictionary with lambda functions: {'double': lambda x: x*2, 'square': lambda x: x**2}
print("\nQuestion 25: Create a dictionary with lambda functions: {'double': lambda x: x*2, 'square': lambda x: x**2}")
# Your code here
lambda_dict = {'double': lambda x: x*2, 'square': lambda x: x**2}
print(lambda_dict)
#--------------------------------------------------------------------------------------------------
# Question 26: Apply each lambda function to 5
print("\nQuestion 26: Apply each lambda function to 5")
# Your code here
lambda_dict = {'double': lambda x: x*2, 'square': lambda x: x**2}
for i in lambda_dict.values():
  print(i(5))
#--------------------------------------------------------------------------------------------------
# Question 27: Create a dictionary with class values: {'list': list, 'dict': dict, 'set': set}
print("\nQuestion 27: Create a dictionary with class values: {'list': list, 'dict': dict, 'set': set}")
# Your code here
class_values = {'list': list, 'dict': dict, 'set': set}
print(class_values)
#--------------------------------------------------------------------------------------------------
# Question 28: Create instances using class dictionary
print("\nQuestion 28: Create instances using class dictionary")
# Your code here
class_values = {'list': list,'dict': dict,'set': set}
instances = {}
for key, class_value in class_values.items():
    instances[key] = class_value()
print(instances)
#--------------------------------------------------------------------------------------------------
# Question 29: Create a dictionary with None values: {'a': None, 'b': None, 'c': None}
print("\nQuestion 29: Create a dictionary with None values: {'a': None, 'b': None, 'c': None}")
# Your code here
None_values = {'a': None, 'b': None, 'c': None}
print(None_values)
#--------------------------------------------------------------------------------------------------
# Question 30: Replace all None values with 0
print("\nQuestion 30: Replace all None values with 0")
# Your code here
None_values = {'a': None, 'b': None, 'c': None}
for key,value in None_values.items():
  if 'None' in str(value):
    None_values[key] = 0
print(None_values)
#--------------------------------------------------------------------------------------------------
# Question 31: Create a dictionary with boolean values: {'is_active': True, 'is_admin': False}
print("\nQuestion 31: Create a dictionary with boolean values: {'is_active': True, 'is_admin': False}")
# Your code here
boolean_values = {'is_active': True, 'is_admin': False}
boolean_values
#--------------------------------------------------------------------------------------------------
# Question 32: Count True values in boolean dictionary
print("\nQuestion 32: Count True values in boolean dictionary")
# Your code here
boolean_values = {'is_active': True, 'is_admin': False}
count = 0
for key,values in boolean_values.items():
  if 'True' in str(values):
    count = count+1
print(count)
#--------------------------------------------------------------------------------------------------
# Question 33: Create a dictionary with complex numbers: {'z1': 3+4j, 'z2': 1+2j}
print("\nQuestion 33: Create a dictionary with complex numbers: {'z1': 3+4j, 'z2': 1+2j}")
# Your code here
complex_numbers = {'z1': 3+4j, 'z2': 1+2j}
print(complex_numbers)
#--------------------------------------------------------------------------------------------------
# Question 34: Find magnitude of each complex number
print("\nQuestion 34: Find magnitude of each complex number")
# Your code here
complex_numbers = {'z1': 3+4j, 'z2': 1+2j}
for key, value in complex_numbers.items():
    print(key, abs(value))
#--------------------------------------------------------------------------------------------------
# Question 35: Create a 4-level nested dictionary
print("\nQuestion 35: Create a 4-level nested dictionary")
# Your code here
data = {"company": {"department": {"team": {"employee": {"name": "John"}}}}}
print(data)
#--------------------------------------------------------------------------------------------------
# Question 36: Access deepest value in 4-level nested dictionary
print("\nQuestion 36: Access deepest value in 4-level nested dictionary")
# Your code here
data = {"company": {"department": {"team": {"employee": {"name": "John"}}}}}
print(data["company"]["department"]["team"]["employee"]["name"])
#--------------------------------------------------------------------------------------------------
# Question 37: Create a dictionary with range values: {'r1': range(3), 'r2': range(5)}
print("\nQuestion 37: Create a dictionary with range values: {'r1': range(3), 'r2': range(5)}")
# Your code here
range_values: {'r1': range(3), 'r2': range(5)}
print(range_values)
#--------------------------------------------------------------------------------------------------
# Question 38: Convert each range to list
print("\nQuestion 38: Convert each range to list")
# Your code here
range_values = {'r1': range(3), 'r2': range(5)}
for key,value in range_values.items():
  print(key,list(value))
#--------------------------------------------------------------------------------------------------
# Question 39: Create a dictionary with generator values
print("\nQuestion 39: Create a dictionary with generator values")
# Your code here
generator_values = {
    "g1": (x for x in range(3)),
    "g2": (x for x in range(5))
}
print(generator_values)
#--------------------------------------------------------------------------------------------------
# Question 40: Convert each generator to list
print("\nQuestion 40: Convert each generator to list")
# Your code here
generator_values = {
    "g1": (x for x in range(3)),
    "g2": (x for x in range(5))
}
for key, value in generator_values.items():
    print(key, list(value))
#--------------------------------------------------------------------------------------------------
# Question 41: Create a dictionary with iterator values
print("\nQuestion 41: Create a dictionary with iterator values")
# Your code here
iterator_values = {
    "i1": iter([1, 2, 3]),
    "i2": iter([4, 5, 6])
}
print(iterator_values)
#--------------------------------------------------------------------------------------------------
# Question 42: Extract all elements from each iterator
print("\nQuestion 42: Extract all elements from each iterator")
# Your code here
iterator_values = {
    "i1": iter([1, 2, 3]),
    "i2": iter([4, 5, 6])
}
for key, value in iterator_values.items():
    print(key, list(value))
#--------------------------------------------------------------------------------------------------
# Question 43: Create a dictionary with nested lists: {'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}
print("\nQuestion 43: Create a dictionary with nested lists: {'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}")
# Your code here
nested_lists = {'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}
print(nested_lists)
#--------------------------------------------------------------------------------------------------
# Question 44: Find sum of each nested list
print("\nQuestion 44: Find sum of each nested list")
# Your code here
nested_lists = {'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}

for key, value in nested_lists.items():
    if isinstance(value, list):
        if isinstance(value[0], list):
            total = 0
            for sublist in value:
                total += sum(sublist)
            print(key, total)
        else:
            print(key, sum(value))
#--------------------------------------------------------------------------------------------------
# Question 45: Create a dictionary with nested dictionaries: {'config': {'db': {'host': 'localhost', 'port': 5432}}}
print("\nQuestion 45: Create a dictionary with nested dictionaries: {'config': {'db': {'host': 'localhost', 'port': 5432}}}")
# Your code here
nested_dictionaries = {'config': {'db': {'host': 'localhost', 'port': 5432}}}
nested_dictionaries
#--------------------------------------------------------------------------------------------------
# Question 46: Access database port from nested configuration
print("\nQuestion 46: Access database port from nested configuration")
# Your code here
nested_dictionaries = {'config': {'db': {'host': 'localhost', 'port': 5432}}}
nested_dictionaries['config']['db']['port']
#--------------------------------------------------------------------------------------------------
# Question 47: Create a dictionary with nested tuples: {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}
print("\nQuestion 47: Create a dictionary with nested tuples: {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}")
# Your code here
nested_tuples = {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}
nested_tuples
#--------------------------------------------------------------------------------------------------
# Question 48: Extract first point coordinates
print("\nQuestion 48: Extract first point coordinates")
# Your code here
nested_tuples = {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}
nested_tuples['points'][0]
#--------------------------------------------------------------------------------------------------
# Question 49: Create a dictionary with nested sets: {'groups': {{1, 2, 3}, {4, 5, 6}}, 'categories': {{'a', 'b'}, {'c', 'd'}}}
print("\nQuestion 49: Create a dictionary with nested sets: {'groups': {{1, 2, 3}, {4, 5, 6}}, 'categories': {{'a', 'b'}, {'c', 'd'}}}")
# Your code here
nested_sets = {'groups': {{1, 2, 3}, {4, 5, 6}}, 'categories': {{'a', 'b'}, {'c', 'd'}}}
print(nested_sets)
#--------------------------------------------------------------------------------------------------
# Question 50: Find union of all nested sets
print("\nQuestion 50: Find union of all nested sets")
# Your code here 
nested_sets = {'groups': {{1, 2, 3}, {4, 5, 6}}, 'categories': {{'a', 'b'}, {'c', 'd'}}}
result = set()
for value in nested_sets['groups']:
    result = result.union(value)
print(result)
