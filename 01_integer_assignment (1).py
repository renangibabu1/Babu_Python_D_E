# INTEGER DATATYPE ASSIGNMENT
# ===========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the sum of first 5 even numbers
print("SOLVED EXAMPLE:")
print("Calculate the sum of first 5 even numbers")
first_5_even = [2, 4, 6, 8, 10]
sum_even = sum(first_5_even)
print(f"First 5 even numbers: {first_5_even}")
print(f"Sum: {sum_even}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the product of first 10 natural numbers
print("Question 1: Calculate the product of first 10 natural numbers")
# Your code here
product = 1

for i in range(1,11):
  product = product*i
product
#------------------------------------------------------------------------------
# Question 2: Find the remainder when 156 is divided by 7
print("\nQuestion 2: Find the remainder when 156 is divided by 7")
# Your code here
a = 156
b = 7

remainder = a%b
# remainder
print(remainder)
#------------------------------------------------------------------------------
# Question 3: Calculate the square of 25
print("\nQuestion 3: Calculate the square of 25")
# Your code here
a = 25
sqrt = a**2
print(sqrt)
#------------------------------------------------------------------------------
# Question 4: Find the cube root of 125
print("\nQuestion 4: Find the cube root of 125")
# Your code here
a = 125
cube_root = a**(1/3)
print(cube_root)
#------------------------------------------------------------------------------
# Question 5: Calculate the sum of digits in number 12345
print("\nQuestion 5: Calculate the sum of digits in number 12345")
# Your code here
sum_value = 0
a = 12345
for i in str(a):
  # print(type(i))
  i = int(i)
  # print(type(i))
  sum_value = sum_value + i
print(sum)
#------------------------------------------------------------------------------
# Question 6: Check if 97 is a prime number
print("\nQuestion 6: Check if 97 is a prime number")
# Your code here
a = 97
count=0

for i in range(1,a+1):
  if a%i==0:
    count=count+1
if count==2:
  print(f"{a} is a prime number")
else:
  print(f"{a} is not a prime number")
#------------------------------------------------------------------------------
# Question 7: Find the factorial of 8
print("\nQuestion 7: Find the factorial of 8")
# Your code here
a = 8
factorial = 1

for i in range(1, a+1):
  # print(i)
  factorial = factorial*i
factorial
#------------------------------------------------------------------------------
# Question 8: Calculate the average of numbers: 15, 23, 31, 42, 56
print("\nQuestion 8: Calculate the average of numbers: 15, 23, 31, 42, 56")
# Your code here
avg_numbers = 15,23,31,42,56
sum = 0
print(type(avg_numbers))
length = len(avg_numbers)
for i in avg_numbers:
  sum = sum +i

avg = sum/length
print(avg)
#------------------------------------------------------------------------------
# Question 9: Find the greatest common divisor (GCD) of 48 and 36
print("\nQuestion 9: Find the greatest common divisor (GCD) of 48 and 36")
# Your code here
a = 48
b = 36

gcd = 0

for i in range(1,min(a,b)+1):
  # print(i)
  if a%i==0 and b%i==0:
    gcd = i
print(gcd)
#------------------------------------------------------------------------------
# Question 10: Calculate the sum of first 20 odd numbers
print("\nQuestion 10: Calculate the sum of first 20 odd numbers")
# Your code here 
total = 0

for i in range(1, 40, 2):
    total = total + i
print("Sum:", total)
