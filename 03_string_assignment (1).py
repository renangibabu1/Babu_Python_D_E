# STRING DATATYPE ASSIGNMENT - 50 QUESTIONS
# ========================================

# SOLVED EXAMPLE
# --------------
# Question: Count vowels in the string "Hello World"
print("SOLVED EXAMPLE:")
print("Count vowels in the string 'Hello World'")
text = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(f"String: {text}")
print(f"Number of vowels: {count}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Reverse the string "Python Programming"
print("Question 1: Reverse the string 'Python Programming'")
# Your code here
text =  "Python Programming"
text[::-1]
#######################################################
# Question 2: Check if "racecar" is a palindrome
print("\nQuestion 2: Check if 'racecar' is a palindrome")
# Your code here
text = "racecar"
if text == "racecar":
  print("palindrome")
else:
  print("Is not a palindrom")
#######################################################
# Question 3: Count the number of words in "Python is a great programming language"
print("\nQuestion 3: Count the number of words in 'Python is a great programming language'")
# 1)Your code here
words = "Python is a great programming language"
words1 = words.split(" ")
words2 = len(words1)
print(words2)
2)
words = "Python is a great programming language"
words_count = 0
for i in words.split(" "):
  #print(i)
  words_count = words_count+1
print(words_count)
#######################################################
# Question 4: Convert "hello world" to title case
print("\nQuestion 4: Convert 'hello world' to title case")
# Your code here
text = "hello world"
text.title()
#######################################################
# Question 5: Find the length of string "Data Science"
print("\nQuestion 5: Find the length of string 'Data Science'")
# Your code here
data = "Data Science"
len(data)
#######################################################
# Question 6: Replace all spaces with underscores in "Machine Learning"
print("\nQuestion 6: Replace all spaces with underscores in 'Machine Learning'")
# Your code here
course = "Machine Learning"
course.replace(" ","_")
#######################################################
# Question 7: Check if "python" is in "Python Programming Language"
print("\nQuestion 7: Check if 'python' is in 'Python Programming Language'")
# Your code here
text = "Python Programming Language"
if "python" in text:
  print("Yes")
else:
  print("No")
#######################################################
# Question 8: Extract the first 5 characters from "Artificial Intelligence"
print("\nQuestion 8: Extract the first 5 characters from 'Artificial Intelligence'")
# Your code here
course = "Artificial Intelligence"
course[0:6]
#######################################################
# Question 9: Convert "UPPERCASE" to lowercase
print("\nQuestion 9: Convert 'UPPERCASE' to lowercase")
# Your code here
text = "DATA ENGINEER"
text.lower()

#######################################################
# Question 10: Remove all vowels from "Computer Science"
print("\nQuestion 10: Remove all vowels from 'Computer Science'")
# Your code here
word = "Computer Science"
result = ""

for i in word:
  if i not in "aeiou":
    result = result+i
print(result)
#######################################################
# Question 11: Find the most frequent character in "mississippi"
print("\nQuestion 11: Find the most frequent character in 'mississippi'")
# Your code here
text = "mississippi"
max_count = 0
freq_string = ""

for i in text:
 # print(text.count(i))
  if text.count(i) > max_count:
    max_count = text.count(i)
    freq_string = i
print(freq_string)
########################################################
# Question 12: Check if two strings are anagrams: "listen" and "silent"
print("\nQuestion 12: Check if two strings are anagrams: 'listen' and 'silent'")
# Your code here
########################################################
# Question 13: Capitalize first letter of each word in "python programming language"
print("\nQuestion 13: Capitalize first letter of each word in 'python programming language'")
# Your code here
text = "python programming language"
text.capitalize()
#######################################################
# Question 14: Count consonants in "Hello World"
print("\nQuestion 14: Count consonants in 'Hello World'")
# Your code here
#######################################################
# Question 15: Find the longest word in "Python is a programming language"
print("\nQuestion 15: Find the longest word in 'Python is a programming language'")
# Your code here
word = "Python is a programming language"
words = word.split()
words
longest=max(words,key=len)
print(longest)

#######################################################
# Question 16: Remove all punctuation from "Hello, World! How are you?"
print("\nQuestion 16: Remove all punctuation from 'Hello, World! How are you?'")
# Your code here
text = "Hello, World! How are you?"
for i in text:
  if i.isalnum() or i ==" ":
    print(i,end="")
#######################################################
# Question 17: Check if string starts with "Python"
print("\nQuestion 17: Check if string starts with 'Python'")
# Your code here
text = "Python"
text.startswith("Python")
#######################################################
# Question 18: Find the index of first occurrence of 'o' in "Hello World"
print("\nQuestion 18: Find the index of first occurrence of 'o' in 'Hello World'")
# Your code here
x = "Hello World"
x.index("o")
#######################################################
# Question 19: Split string "apple,banana,orange" by comma
print("\nQuestion 19: Split string 'apple,banana,orange' by comma")
# Your code here
fruits="apple,banana,orange"
fruits_comma= fruits.split(",")
print(fruits_comma)
#######################################################
# Question 20: Join list ['Python', 'is', 'awesome'] with spaces
print("\nQuestion 20: Join list ['Python', 'is', 'awesome'] with spaces")
# Your code here
1)
list_l= ['Python', 'is', 'awesome']
for i in list_l:
  print(i, end=" ")
2)
list_l1=" ".join(list_l)
print(list_l1)
#######################################################
# Question 21: Check if string contains only digits: "12345"
print("\nQuestion 21: Check if string contains only digits: '12345'")
# Your code here
number = "1234"
number.isdigit()

number = "1234"
number.isnumeric()

#######################################################
# Question 22: Check if string contains only letters: "HelloWorld"
print("\nQuestion 22: Check if string contains only letters: 'HelloWorld'")
# Your code here
text = "HelloWorld"
text.isalpha()
#######################################################
# Question 23: Convert "hello world" to "hElLo WoRlD" (alternating case)
print("\nQuestion 23: Convert 'hello world' to 'hElLo WoRlD' (alternating case)")
# Your code here
#######################################################
# Question 24: Find all positions of 'a' in "banana"
print("\nQuestion 24: Find all positions of 'a' in 'banana'")
# Your code here
text="banana"
empty_list = []

for index,value in enumerate(text):
  if value == "a":
    empty_list.append(index)
    print(index)
print(empty_list)
  
#######################################################
# Question 25: Remove leading and trailing whitespace from "  Hello World  "
print("\nQuestion 25: Remove leading and trailing whitespace from '  Hello World  '")
# Your code here
words = " Hello World "
words.strip()
#######################################################
# Question 26: Check if string ends with "ing": "programming"
print("\nQuestion 26: Check if string ends with 'ing': 'programming'")
# Your code here
word = "programming"
word.endswith("ing")
#######################################################
# Question 27: Replace first occurrence of 'o' with '0' in "Hello World"
print("\nQuestion 27: Replace first occurrence of 'o' with '0' in 'Hello World'")
# Your code here
text = "Hello World"
text = text.replace("o","0",1)
print(text)
#######################################################
# Question 28: Find the shortest word in "Python is a programming language"
print("\nQuestion 28: Find the shortest word in 'Python is a programming language'")
# 1) Your code here
word = "Python is a programming language"
words = word.split()

shortest = words[0]
for i in words:
   if len(i)<len(shortest):
    shortest=i
print(shortest)
2)
word = "Python is a programming language"
words = word.split()
shortest = min(words,key=len)
print(shortest)
3)
word = "Python is a programming language"
words = word.split()
words = sorted(words, key=len)
print(words[0])
#######################################################
# Question 29: Count words that start with 'p' in "Python programming is powerful"
print("\nQuestion 29: Count words that start with 'p' in 'Python programming is powerful'")
# Your code here
1.)
words = "Python programming is powerful"
#words=words.lower()
words.count("p",0)

2)
words = "Python programming is powerful"
count = 0
for i in words.split(" "):
  if i.startswith("p"):
    count=count+1
print(count)
#######################################################
# Question 30: Reverse words in "Hello World Python"
print("\nQuestion 30: Reverse words in 'Hello World Python'")
# Your code here
words = "Hello World Python"
words1=words.split()[::-1]
words_string = " ".join(words1)
print(words_string)
########################################################
# Question 31: Check if string is a valid email format: "user@example.com"
print("\nQuestion 31: Check if string is a valid email format: 'user@example.com'")
# Your code here

# Question 32: Extract domain from "https://www.example.com/path"
print("\nQuestion 32: Extract domain from 'https://www.example.com/path'")
# Your code here
########################################################
# Question 33: Count lines in multi-line string
print("\nQuestion 33: Count lines in multi-line string")
# Your code here
multilines = """i am learning the python course
along with the sql
and Azure data factory and Azure data bricks
and pyspark and ETL pipeline"""

len(multilines.splitlines())
########################################################
# Question 34: Find common characters between "hello" and "world"
print("\nQuestion 34: Find common characters between 'hello' and 'world'")
# Your code here

# Question 35: Check if string is a valid phone number: "+1-555-123-4567"
print("\nQuestion 35: Check if string is a valid phone number: '+1-555-123-4567'")
# Your code here
#######################################################
# Question 36: Extract numbers from "abc123def456ghi789"
print("\nQuestion 36: Extract numbers from 'abc123def456ghi789'")
# Your code here
numbers = "abc123def456ghi789"
for i in numbers:
  #print(i)
  if i.isdigit():
    print(i)
#######################################################
# Question 37: Convert "snake_case" to "camelCase"
print("\nQuestion 37: Convert 'snake_case' to 'camelCase'")
# Your code here
words1="snake_case"
words2 = words1.split("_")
words2
print(words2[0]+words2[1].capitalize())
#######################################################
# Question 38: Check if string is a valid palindrome ignoring case: "A man a plan a canal Panama"
print("\nQuestion 38: Check if string is a valid palindrome ignoring case: 'A man a plan a canal Panama'")
# Your code here

# Question 39: Find the most common word in "the quick brown fox jumps over the lazy dog"
print("\nQuestion 39: Find the most common word in 'the quick brown fox jumps over the lazy dog'")
# Your code here

# Question 40: Generate acronym from "National Aeronautics and Space Administration"
print("\nQuestion 40: Generate acronym from 'National Aeronautics and Space Administration'")
# Your code here

# Question 41: Check if string contains balanced parentheses: "((()))"
print("\nQuestion 41: Check if string contains balanced parentheses: '((()))'")
# Your code here

# Question 42: Convert "hello world" to Morse code
print("\nQuestion 42: Convert 'hello world' to Morse code")
# Your code here
#######################################################
# Question 43: Find the longest common substring between "programming" and "grammar"
print("\nQuestion 43: Find the longest common substring between 'programming' and 'grammar'")
# Your code here
word1 = "programming"
word2 = "grammar"

longest = ""

for i in range(len(word1)):
    for j in range(i + 1, len(word1) + 1):
        substring = word1[i:j]

        if word2.find(substring) != -1:
            if len(substring) > len(longest):
                longest = substring

print(longest)
#######################################################
# Question 44: Check if string is a valid URL: "https://www.google.com"
print("\nQuestion 44: Check if string is a valid URL: 'https://www.google.com'")
# Your code here
#######################################################
# Question 45: Extract all words with length > 5 from "Python programming is amazing and powerful"
print("\nQuestion 45: Extract all words with length > 5 from 'Python programming is amazing and powerful'")
# Your code here
# 2 ways of solving the problems
words="Python programming is amazing and powerful"
words_list=words.split(" ")
for i in words_list:
  x = len(i)
  if x>5:
    print(i)
    
# #print(words_list)

for i in words.split():
  if len(i)>5:
    print(i)
---------------------------------------------------------------------------------------------------------------
# Question 46: Convert "hello world" to Pig Latin
print("\nQuestion 46: Convert 'hello world' to Pig Latin")
# Your code here
word = "hello world"
first = word[0]
remain = word[1:]
print(remain+" python program "+first)
--------------------------------------------------------------------------------------------------------------
# Question 47: Check if string is a valid IPv4 address: "192.168.1.1"
print("\nQuestion 47: Check if string is a valid IPv4 address: '192.168.1.1'")
# Your code here

# Question 48: Find all substrings of "abc"
print("\nQuestion 48: Find all substrings of 'abc'")
# Your code here

# Question 49: Convert "hello world" to ROT13 encoding
print("\nQuestion 49: Convert 'hello world' to ROT13 encoding")
# Your code here

# Question 50: Check if string is a valid credit card number: "4532015112830366"
print("\nQuestion 50: Check if string is a valid credit card number: '4532015112830366'")
# Your code here 
