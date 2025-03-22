## Exercise 1
Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

```python
def conditional_product(num1, num2):
    product = num1 * num2
    sum = num1 + num2
    
    if product <= 1000:
        return product
    else:
        return sum

number1 = 40
number2 = 30
result = conditional_product(number1, number2)

print(result)
```

## Exercise 2
Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

```python
def sum_previous_current(count):
    previous = 0

    for i in range(count):
        print(f'Current Number {i} Previous Number {previous} Sum: {i + previous}')
        previous = i

sum_previous_current(10)
```

## Exercise 3
Write a Python code to accept a string from the user and display characters present at an even index number.

```python
# range(start : stop : step)을 사용

def display_even_idx_char(input):
    for i in range(0, len(input), 2):
        print(input[i])

input = input()
display_even_idx_char(input)
```
```python
# list[start:stop:step]을 사용하는 방법도 있음

def display_even_idx_char(input):
    input_list = list(input)
    for char in input_list[::2]:
        print(char)

input = input()
display_even_idx_char(input)
```

## Exercise 4
Write a Python code to remove characters from a string from 0 to n and return a new string.

```python
def remove_n_string(input, count):
    return input[count:]

input = 'PYnative'
result = remove_n_string(input, 4)

print(result)
```

## Exercise 5
Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.
```python
def is_first_last_same(input):
    if input[0] == input[-1]:
        return True
    else:
        return False
    
input = [10, 20, 30, 40, 10]
result = is_first_last_same(input)
print(result)
```

## Exercise 6
Write a Python code to display numbers from a list divisible by 5
```python
def is_divided_five(input):
    for i in input:
        if i % 5 == 0:
            print(i)

input = [10, 20, 33, 46, 55]
is_divided_five(input)
```

## Exercise 7
Write a Python code to find how often the substring “Emma” appears in the given string.
```python
import re

input = "Emma is good developer. Emma is a writer"

p = re.compile('Emma')
m = p.findall(input)

print(len(m))
```
```python
# 간단하게 문자열의 count 메소드를 사용하는 방법도 있다.
input = "Emma is good developer. Emma is a writer"

print(input.count('Emma'))
```

## Exercise 8
Print the following pattern

1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
```python
for i in range(1, 6):
    for j in range(i):
        print(i, end=' ')
    print()
```

## Exercise 9
Write a Python code to check if the given number is palindrome. A palindrome number is a number that is the same after reverse. For example, 545 is the palindrome number.
```python
input = 151
input = str(input)
isPalindrome = True

for i in range(len(input)):
    if input[i] != input[2-i]:
        isPalindrome = False
        break

if isPalindrome:
    print('Number is Palindrome')
else:
    print('Number is not Palindrome')
```
```python
# 역수를 만든 다음 비교하는 방법도 있다.
def palindrome(number):
    original_num = number
    
    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")
```

## Exercise 10
Given two lists of numbers, write a Python code to create a new list such that the latest list should contain odd numbers from the first list and even numbers from the second list.
```python
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

new_list = []

# odd numbers from first list
for i in list1:
    if i % 2 == 1:
        new_list.append(i)

# even numbers from first list
for i in list2:
    if i % 2 == 0:
        new_list.append(i)

print(new_list)
```

## Exercise 11
For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
```python
input = 7536
input = str(input)
input_list = []

for i in input:
    input_list.append(i)

input_list.reverse()

for i in input_list:
    print(i, end=' ')
```
```python
# 나머지를 사용하는 방법도 있다.
number = 7536
print("Given number", number)
while number > 0:
    digit = number % 10
    number = number // 10
    print(digit, end=" ")
```

## Exercise 12
Calculate income tax for the given income by adhering to the rules below
```python
income = 45000
sum_tax = 0

f_rate = 0
s_rate = 0.1
r_rate = 0.2

# first tax
if income > 10000:
    sum_tax += 10000 * f_rate
    income -= 10000

# second tax
if income > 10000:
    sum_tax += 10000 * s_rate
    income -= 10000

# remain tax
sum_tax += income * r_rate

print(f'Total tax is {sum_tax:.0f}')
```

## Exercise 13
1  2 3 4 5 6 7 8 9 10 		
2  4 6 8 10 12 14 16 18 20 		
3  6 9 12 15 18 21 24 27 30 		
4  8 12 16 20 24 28 32 36 40 		
5  10 15 20 25 30 35 40 45 50 		
6  12 18 24 30 36 42 48 54 60 		
7  14 21 28 35 42 49 56 63 70 		
8  16 24 32 40 48 56 64 72 80 		
9  18 27 36 45 54 63 72 81 90 		
10 20 30 40 50 60 70 80 90 100 
```python
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=' ')
    print()
```

## Exercise 14
* * * * *  
* * * *  
* * *  
* *  
*
```python
for i in range(5, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()
```

## Exercise 15
Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
```python
def exponent(base, exp):
    return base**exp

base = 2
exp = 5

result = exponent(base, exp)
print(result)
```

## Exercise 16
Write a program to accept two numbers from the user and calculate multiplication
```python
def mul(num1, num2):
    return num1 * num2

num1 = int(input('input num1: '))
num2 = int(input('input num2: '))

result = mul(num1, num2)
print(result)
```

## Exercise 17
Use the print() function to format the given words in the mentioned format. Display the ** separator between each string.

For example: print('Name', 'Is', 'James') will display Name\*\*Is\*\*James
```python
print('Name', 'Is', 'James', sep='**')
```

## Exercise 18
Convert Decimal number to octal using print() output formatting
```python
num = 8
print(oct(num))
```
```python
# 문자열 포맷 코드를 사용하는 방법도 있다.
num = 8
print('%o' % num)
```

## Exercise 19
Display float number with 2 decimal places using print()
```python
num = 458.541315
print('%.2f' %num)
```

## Exercise 20
Accept a list of 5 float numbers as an input from the user
```python
user_input = input('input 5 number of float: ')
converted_list = user_input.split(sep=' ')
print(converted_list)
```

## Exercise 21
Write all content of a given file into a new file by skipping line number 5
```python
file_path = 'file.txt'
new_file_path = 'new_file.txt'

with open(file_path) as f:
    for idx, line in enumerate(f):
        if idx == 4:
            continue

        open(new_file_path, 'a').write(line)
```

## Exercise 22
Write a program to take three names as input from a user in the single input() function call.
```python
user_input = input('Input 3 number of name: ')
names = user_input.split(sep=' ')

print(names)
```
```python
# 리스트 형태를 다음과 같이 나눠서 할당 받을 수 있다.
user_input = input('Input 3 number of name: ')
name1, name2, name3 = user_input.split(sep=' ')

print(name1, name2, name3)
```

## Exercise 23
Write a program to use string.format() method to format the following three variables as per the expected output
```python
totalMoney = 1000
quantity = 3
price = 450

print('I have {0} dollars so I can buy {1} football for {2} dollars.'.format(totalMoney, quantity, price))
```

## Exercise 24
Write a program to check if the given file is empty or not
```python
file_path = 'file.txt'

with open(file_path) as f:
    contents = f.readlines()
    if contents:
        print('File is not empty')
    else:
        print('File is empty')
```
```python
import os

# 파일이나 디렉토리의 상태 정보를 가져오는 데 사용
size = os.stat("test.txt").st_size
if size == 0:
    print('file is empty')
```

## Exercise 25
Create a test.txt file and add the below content to it.
```python
with open('test.txt', mode='w') as f:
    for i in range(1, 8):
        f.write(f'line{i}\n')
```

## Exercise 26
Print first 10 natural numbers using while loop
```python
number = 1
while number <= 10:
    print(number)
    number += 1
```

## Exercise 27
Write a Python code to print the following number pattern using a loop.
```python
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
```

## Exercise 28
Calculate sum of all numbers from 1 to a given number
```python
user_input = int(input())
sum = 0

for i in range(1, user_input + 1):
    sum += i

print(sum)
```

## Exercise 29
Print multiplication table of a given number
```python
num = 2

for i in range(1, 11):
    print(num * i)
```

## Exercise 30
Write a Python program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five
- If the number is greater than 150, then skip it and move to the following number
- If the number is greater than 500, then stop the loop
```python
numbers = [12, 75, 150, 180, 145, 525, 50]

for number in numbers:

    if number > 500:
        break

    if number % 5 != 0:
        continue

    if number > 150:
        continue

    print(number)
```

## Exercise 31

```python

```