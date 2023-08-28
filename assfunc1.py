#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Which keyword is used to create a function? Create a function to return a list of odd numbers in the
range of 1 to 25."""


# In[2]:


def odd_numbers():
    odd_nums = []
    for num in range(1, 26):
        if num % 2 != 0:
            odd_nums.append(num)
    return odd_nums

result = odd_numbers()
print(result)


# In[3]:


"""Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs
to demonstrate their use."""


# In[4]:


def func(*args):
    return args


# In[5]:


func()


# In[6]:


def func(**kwargs):
    return kwargs


# In[7]:


func()


# In[8]:


"""What is an iterator in python? Name the method used to initialise the iterator object and the method
used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14,
16, 18, 20]."""


# In[9]:


s = [2,4,6,8,10,12,14,16,18,20]


# In[10]:


s1 = iter(s)


# In[11]:


next(s1)


# In[12]:


next(s1)


# In[13]:


next(s1)


# In[14]:


next(s1)


# In[15]:


next(s1)


# In[16]:


next(s1)


# In[17]:


next(s1)


# In[18]:


next(s1)


# In[19]:


next(s1)


# In[20]:


next(s1)


# In[21]:


"""What is a generator function in python? Why yield keyword is used? Give an example of a generator
function."""


# In[22]:


def fibb(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b, a+b


# In[23]:


for i in fibb(10):
    
    print(i)


# In[24]:


"""Create a generator function for prime numbers less than 1000. Use the next() method to print the
first 20 prime numbers."""


# In[3]:


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_generator(limit):
    num = 2
    while num < limit:
        if is_prime(num):
            yield num
        num += 1

prime_gen = prime_generator(1000)

for _ in range(20):
    prime = next(prime_gen)
    print(prime)


# In[4]:


"""Write a List Comprehension to iterate through the given string: ‘pwskills’.
Expected output: ['p', 'w', 's', 'k', 'i', 'l', 'l', 's']"""


# In[5]:


s = "pwskills"


# In[18]:


output_list = [char for char in input_string if char in 'wskil']
print(output_list)


# In[19]:


"""Write a code to print odd numbers from 1 to 100 using list comprehension."""


# In[20]:


odd_numbers = [num for num in range(1, 101) if num % 2 != 0]
print(odd_numbers)


# In[21]:


"""Write a python program to check whether a given number is Palindrome or not using a while loop."""


# In[22]:


def is_palindrome(number):
    original_number = number
    reversed_number = 0
    
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    
    return original_number == reversed_number

# Input from the user
num = int(input("Enter a number: "))

if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")


# In[ ]:




