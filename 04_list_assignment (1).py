# LIST DATATYPE ASSIGNMENT - 50 QUESTIONS
# ======================================

# SOLVED EXAMPLE
# --------------
# Question: Find the maximum and minimum values in a list
print("SOLVED EXAMPLE:")
print("Find the maximum and minimum values in a list")
numbers = [23, 45, 12, 67, 34, 89, 56]
max_val = max(numbers)
min_val = min(numbers)
print(f"List: {numbers}")
print(f"Maximum: {max_val}")
print(f"Minimum: {min_val}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Create a list of first 10 square numbers
print("Question 1: Create a list of first 10 square numbers")
# Your code here
square_list = []
for i in range(1,11):
  square_list.append(i*2)
print(square_list)
#-----------------------------------------------------------------------------------------
# Question 2: Find the sum of all even numbers in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nQuestion 2: Find the sum of all even numbers in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
# Your code here
list_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []
sum_value = 0
for i in list_values:
  if i % 2 ==0:
    even_list.append(i)
    sum_value = sum_value + i
print("sum of even numbers",sum_value)  
print(even_list)
#-----------------------------------------------------------------------------------------
# Question 3: Remove duplicates from [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
print("\nQuestion 3: Remove duplicates from [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]")
# Your code here
list_duplicates = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
x = list(set(list_duplicates))
print(x)
#-----------------------------------------------------------------------------------------
# Question 4: Sort the list [64, 34, 25, 12, 22, 11, 90] in descending order
print("\nQuestion 4: Sort the list [64, 34, 25, 12, 22, 11, 90] in descending order")
# Your code here
sort_list = [64, 34, 25, 12, 22, 11, 90]
sorted(sort_list,reverse=True)
#-----------------------------------------------------------------------------------------
# Question 5: Find the average of numbers in [15, 23, 31, 42, 56, 78, 91]
print("\nQuestion 5: Find the average of numbers in [15, 23, 31, 42, 56, 78, 91]")
# Your code here
avg_list = [15, 23, 31, 42, 56, 78, 91]
sum(avg_list)/len(avg_list)
#-----------------------------------------------------------------------------------------
# Question 6: Create a list of first 15 Fibonacci numbers
print("\nQuestion 6: Create a list of first 15 Fibonacci numbers")
# Your code here
fibonacci = []
a = 0
b = 1

for i in range(15):
  #print(i)
  a = b
  b = a+b
  fibonacci.append(a)
print(fibonacci)
#-----------------------------------------------------------------------------------------
# Question 7: Find the second largest number in [45, 67, 23, 89, 12, 34, 78]
print("\nQuestion 7: Find the second largest number in [45, 67, 23, 89, 12, 34, 78]")
# Your code here
second_largest = [45, 67, 23, 89, 12, 34, 78]
second_largest.sort()
second_largest[-2]
#-----------------------------------------------------------------------------------------
# Question 8: Reverse the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nQuestion 8: Reverse the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
# Your code here
reverse_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse_list.sort(reverse=True)
print(reverse_list)

reverse_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse_list.sort()
reverse_list[::-1]
#-----------------------------------------------------------------------------------------
# Question 9: Count how many times 5 appears in [1, 5, 2, 5, 3, 5, 4, 5, 6]
print("\nQuestion 9: Count how many times 5 appears in [1, 5, 2, 5, 3, 5, 4, 5, 6]")
# Your code here
count_list = [1, 5, 2, 5, 3, 5, 4, 5, 6]
count_list.count(5)

count = 0

for i in  count_list:
  if i == 5:
    count = count + 1
print(count)
#-----------------------------------------------------------------------------------------
# Question 10: Create a list of prime numbers between 1 and 50
print("\nQuestion 10: Create a list of prime numbers between 1 and 50")
# Your code here
prime_numbers = []

for i in range(1,51):
  if i > 1:
    for j in range(2,i):
      if i%j == 0:
        #print(i,"is not a prime number")
        break
    else:
      #print(i,"is a prime number")
      prime_numbers.append(i)
print(prime_numbers)
#-----------------------------------------------------------------------------------------
# Question 11: Flatten nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 11: Flatten nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here
empty_list = []
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in nested_list:
  for items in i:
    empty_list.append(items)
print(empty_list)
#-----------------------------------------------------------------------------------------
# Question 12: Find common elements between [1, 2, 3, 4, 5] and [4, 5, 6, 7, 8]
print("\nQuestion 12: Find common elements between [1, 2, 3, 4, 5] and [4, 5, 6, 7, 8]")
# Your code here
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]

set1 = set(list1)
set2 = set(list2)

cmn_elements = set1.intersection(set2)
print(cmn_elements)
cmn_elements = list(cmn_elements)
print(cmn_elements)
#-----------------------------------------------------------------------------------------
# Question 13: Create a list of lists: [[1, 2], [3, 4], [5, 6]]
print("\nQuestion 13: Create a list of lists: [[1, 2], [3, 4], [5, 6]]")
# Your code here
nested_list = [[1, 2], [3, 4], [5, 6]]

print(nested_list)
#-----------------------------------------------------------------------------------------
# Question 14: Find the sum of each sublist in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 14: Find the sum of each sublist in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum_list = []

for  i in nested_list:
  #print(i)
  sum_list.append(sum(i))
print(sum_list)
#-----------------------------------------------------------------------------------------
# Question 15: Transpose the matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 15: Transpose the matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here
list_values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list(zip(*list_values))
#-----------------------------------------------------------------------------------------
# Question 16: Find the maximum value in each sublist of [[1, 5, 3], [9, 2, 7], [4, 8, 6]]
print("\nQuestion 16: Find the maximum value in each sublist of [[1, 5, 3], [9, 2, 7], [4, 8, 6]]")
# Your code here
list_values = [[1, 5, 3], [9, 2, 7], [4, 8, 6]]
max_list = []

for i in list_values:
  max_value = max(i)
  max_list.append(max_value)
print(max_list)
#-----------------------------------------------------------------------------------------
# Question 17: Create a 3D list: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print("\nQuestion 17: Create a 3D list: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]")
# Your code here
threeD_list = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(threeD_list)
#-----------------------------------------------------------------------------------------
# Question 18: Find the sum of all elements in 3D list [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print("\nQuestion 18: Find the sum of all elements in 3D list [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]")
# Your code here
list_values = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
sum_list = []

for i in list_values:
  for items in i:
    sum_value = sum(items)
    sum_list.append(sum_value)
print(sum(sum_list))
#-----------------------------------------------------------------------------------------
# Question 19: Extract all even numbers from nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 19: Extract all even numbers from nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here
list_value = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_1 = []

for i in list_value:
  for items in i:
    print(items)
    if items % 2 == 0:
      list_1.append(items)
    print(items)
  
print(list_1)
#-----------------------------------------------------------------------------------------
# Question 20: Create a list of mixed data types: [1, "hello", 3.14, True, [1, 2, 3]]
print("\nQuestion 20: Create a list of mixed data types: [1, 'hello', 3.14, True, [1, 2, 3]]")
# Your code here
mixed_list = [1, "hello", 3.14, True, [1, 2, 3]]
print(mixed_list)
#-----------------------------------------------------------------------------------------
# Question 21: Find the length of each string in ["apple", "banana", "cherry", "date"]
print("\nQuestion 21: Find the length of each string in ['apple', 'banana', 'cherry', 'date']")
# Your code here

string_list = ["apple", "banana", "cherry", "date"]

for i in string_list:
  print(len(i))
#-----------------------------------------------------------------------------------------
# Question 22: Create a list of tuples: [(1, 'a'), (2, 'b'), (3, 'c')]
print("\nQuestion 22: Create a list of tuples: [(1, 'a'), (2, 'b'), (3, 'c')]")
# Your code here
tuples_list = [(1, 'a'), (2, 'b'), (3, 'c')]
print(tuples_list)
#-----------------------------------------------------------------------------------------
# Question 23: Extract first element from each tuple in [(1, 'a'), (2, 'b'), (3, 'c')]
print("\nQuestion 23: Extract first element from each tuple in [(1, 'a'), (2, 'b'), (3, 'c')]")
# Your code here
list_tuple = [(1, 'a'), (2, 'b'), (3, 'c')]
for i in list_tuple:
  print(i[0])
#-----------------------------------------------------------------------------------------
# Question 24: Create a list of dictionaries: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
print("\nQuestion 24: Create a list of dictionaries: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]")
# Your code here
dict_list = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
print(dict_list)
#-----------------------------------------------------------------------------------------
# Question 25: Extract all 'name' values from list of dictionaries
print("\nQuestion 25: Extract all 'name' values from list of dictionaries")
# Your code here
dict_list = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
for names in dict_list:
  print(names.get('name'))
#-----------------------------------------------------------------------------------------
# Question 26: Find the person with maximum age in list of dictionaries
print("\nQuestion 26: Find the person with maximum age in list of dictionaries")
# Your code here
dict_list = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
max_age = 0
name = ""

for i in dict_list:
  current_age = i.get('age')
  if current_age> max_age:
    max_age = current_age
    name = i.get('name')
print(name)
#-----------------------------------------------------------------------------------------
# Question 27: Create a 4D list: [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]
print("\nQuestion 27: Create a 4D list: [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]")
# Your code here
fourthD_list = [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]
print(fourthD_list)
#-----------------------------------------------------------------------------------------
# Question 28: Find the maximum value in 4D list
print("\nQuestion 28: Find the maximum value in 4D list")
# Your code here
fourthD_list = [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]

max_value = 0
for i in fourthD_list:
  for items in i:
    for j in items:
      for k in j:
        print(k,end=" ")
        # if k > max_value:
        #   max_value = k
print(max_value)
#-----------------------------------------------------------------------------------------
# Question 29: Create a list of sets: [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
print("\nQuestion 29: Create a list of sets: [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]")
# Your code here
sets_list = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
print(sets_list)
#-----------------------------------------------------------------------------------------
# Question 30: Find the union of all sets in list of sets
print("\nQuestion 30: Find the union of all sets in list of sets")
# Your code here
sets_list = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
set_union = set()

for i in sets_list:
  print(i)
  set_union = set_union.union(i)
print(set_union)
#-----------------------------------------------------------------------------------------
# Question 31: Create a list of complex numbers: [1+2j, 3+4j, 5+6j]
print("\nQuestion 31: Create a list of complex numbers: [1+2j, 3+4j, 5+6j]")
# Your code here
complex_list = [1+2j, 3+4j, 5+6j]
print(complex_list)
#-----------------------------------------------------------------------------------------
# Question 32: Find the magnitude of each complex number in list
print("\nQuestion 32: Find the magnitude of each complex number in list")
# Your code here
complex_list = [1+2j, 3+4j, 5+6j]

for i in complex_list:
  print(abs(i))
#-----------------------------------------------------------------------------------------
# Question 33: Create a nested list with different levels: [1, [2, 3], [4, [5, 6]], 7]
print("\nQuestion 33: Create a nested list with different levels: [1, [2, 3], [4, [5, 6]], 7]")
# Your code here
nested_list = [1, [2, 3], [4, [5, 6]], 7]
print(nested_list)
#-----------------------------------------------------------------------------------------
# Question 34: Count the depth of nesting in [1, [2, 3], [4, [5, 6]], 7]
print("\nQuestion 34: Count the depth of nesting in [1, [2, 3], [4, [5, 6]], 7]")
# Your code here
nested_list = [1, [2, 3], [4, [5, 6]], 7]
count = 1
for i in nested_list:
    if type(i) == list:
        count = 2
        for j in i:
            if type(j) == list:
                count = 3
print(count)
#-----------------------------------------------------------------------------------------
# Question 35: Create a list of functions: [len, str, int, float]
print("\nQuestion 35: Create a list of functions: [len, str, int, float]")
# Your code here
functions_list = [len, str, int, float]
print(functions)
#-----------------------------------------------------------------------------------------
# Question 36: Apply each function in list to string "123"
print("\nQuestion 36: Apply each function in list to string '123'")
# Your code here
string_value = "123"
functions_list = [len, str, int, float]

for i in functions_list:
  print(i(string_value))
#-----------------------------------------------------------------------------------------
# Question 37: Create a list of lambda functions: [lambda x: x*2, lambda x: x**2, lambda x: x+1]
print("\nQuestion 37: Create a list of lambda functions: [lambda x: x*2, lambda x: x**2, lambda x: x+1]")
# Your code here
functions_list = [lambda x: x * 2,lambda x: x ** 2,lambda x: x + 1]
print(functions_list)
#-----------------------------------------------------------------------------------------
# Question 38: Apply each lambda function to 5
print("\nQuestion 38: Apply each lambda function to 5")
# Your code here
x = 5
functions_list = [lambda x: x * 2,lambda x: x ** 2,lambda x: x + 1]

for i in functions_list:
  print(i(x))
#-----------------------------------------------------------------------------------------
# Question 39: Create a list of classes: [list, dict, set, tuple]
print("\nQuestion 39: Create a list of classes: [list, dict, set, tuple]")
# Your code here
classes_list = [list, dict, set, tuple]
print(classes_list)
#-----------------------------------------------------------------------------------------
# Question 40: Create instances of each class in list
print("\nQuestion 40: Create instances of each class in list")
# Your code here
classes_list = [list, dict, set, tuple]
instances = []

for i in classes_list:
  print(i)
  instances.append(i())
print(instances)
#-----------------------------------------------------------------------------------------
# Question 41: Create a list of None values: [None, None, None, None]
print("\nQuestion 41: Create a list of None values: [None, None, None, None]")
# Your code here
none_list = [None, None, None, None]
print(none_list)
#-----------------------------------------------------------------------------------------
# Question 42: Replace all None values with 0 in list
print("\nQuestion 42: Replace all None values with 0 in list")
# Your code here
none_list = [None, None, None, None]

for i in range(len(none_list)):
  none_list[i] = 0
print(none_list)
#-----------------------------------------------------------------------------------------
# Question 43: Create a list of boolean values: [True, False, True, False]
print("\nQuestion 43: Create a list of boolean values: [True, False, True, False]")
# Your code here
boolean_list = [True, False, True, False]
print(boolean_list)
#-----------------------------------------------------------------------------------------
# Question 44: Count True values in boolean list
print("\nQuestion 44: Count True values in boolean list")
# Your code here
boolean_list = [True, False, True, False]
boolean_list.count(True)
#-----------------------------------------------------------------------------------------
# Question 45: Create a list of ranges: [range(3), range(5), range(2)]
print("\nQuestion 45: Create a list of ranges: [range(3), range(5), range(2)]")
# Your code here
ranges_list = [range(3), range(5), range(2)]
print(ranges_list)
#-----------------------------------------------------------------------------------------
# Question 46: Convert each range to list
print("\nQuestion 46: Convert each range to list")
# Your code here
ranges = [range(5), range(3), range(2)]
result = []

for i in ranges:
    result.append(list(i))
print(result)
#-----------------------------------------------------------------------------------------
# Question 47: Create a list of generators: [(x for x in range(3)), (x for x in range(5))]
print("\nQuestion 47: Create a list of generators: [(x for x in range(3)), (x for x in range(5))]")
# Your code here
generators_list = [(x for x in range(3)), (x for x in range(5))]
print(generators_list)
#-----------------------------------------------------------------------------------------
# Question 48: Convert each generator to list
print("\nQuestion 48: Convert each generator to list")
# Your code here
generators = [(x for x in range(3)), (x for x in range(5))]
result = []

for i in generators:
    result.append(list(i))
print(result)
#-----------------------------------------------------------------------------------------
# Question 49: Create a list of iterators: [iter([1, 2, 3]), iter([4, 5, 6])]
print("\nQuestion 49: Create a list of iterators: [iter([1, 2, 3]), iter([4, 5, 6])]")
# Your code here
list_iterators = [iter([1, 2, 3]), iter([4, 5, 6])]
print(list_iterators)
#-----------------------------------------------------------------------------------------
# Question 50: Extract all elements from each iterator
print("\nQuestion 50: Extract all elements from each iterator")
# Your code here
list_iters = [iter([1, 2, 3]), iter([4, 5, 6])]
result = []

for i in list_iters:
    for j in i:
        result.append(j)
print(result)
