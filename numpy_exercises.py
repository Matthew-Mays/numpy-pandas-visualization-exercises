#!/usr/bin/env python
# coding: utf-8

# In[136]:


import numpy as np


# In[137]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# ### 1. How many negative numbers are there?

# In[139]:


# Find the length of the list a where numbers are negative
len(a[a < 0])


# ### 2. How many positive numbers are there?

# In[140]:


# Find the length of the list a where numbers are positive
len(a[a > 0])


# ### 3. How many even positive numbers are there?

# In[9]:


# Find the length of the list a where numbers are both positive and even
len(a[(a > 0) & (a % 2 == 0)])


# ### 4. If you were to add 3 to each data point, how many positive numbers would there be?

# In[141]:


# Find the length of the list a where numbers are positive after adding 3
len(a[(a + 3) > 0])


# ### 5. If you squared each number, what would the new mean and standard deviation be?

# In[18]:


# print out the mean of list a
print((a ** 2).mean())
# print out the standard deviation of list a
print((a ** 2).std())


# ### 6. A common statistical operation on a dataset is centering. 
# ### This means to adjust the data such that the center of the data is at 0. This is done by subtracting the mean from each data point. Center the data set.

# In[142]:


# print out the list of a after subtracting the mean of list a from each number
print(a - a.mean())


# ### 7. Calculate the z-score for each data point.

# In[143]:


# To find z score subtract the mean from each value in a and then divide them by the standard deviation
print(((a - a.mean()) / a.std()))


# In[145]:


# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[146]:


# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
# initialize sum_of_a variable
sum_of_a = 0
# loops through every number in a
for num in a:
    # adds every number to sum_of_a
    sum_of_a += num
print(sum_of_a)


# In[147]:


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
# initialize min_of_a
min_of_a = 200
# loops through every number in a
for num in a:
    # check to see if num is less than current value of min_of_a
    if num < min_of_a:
        # if num is less than min_of_a set min_of_a to num
        min_of_a = num
print(min_of_a)


# In[148]:


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
# initialize max_of_a
max_of_a = 0
# loops through every number in a
for num in a:
    # check to see if num is greater than current value of max_of_a
    if num > max_of_a:
        # if num is greater than max_of_a set it to num
        max_of_a = num
print(max_of_a)


# In[149]:


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
#initialize mean_of_a
mean_of_a = 0
#loops through every number in a
for num in a:
    #sum up a list
    mean_of_a += num
# set mean_of_a to sum of a divided by how many numbers in a (ie. the mean)    
mean_of_a = mean_of_a / len(a)
print(mean_of_a)


# In[29]:


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = 1
for num in a:
    product_of_a *= num
product_of_a


# In[32]:


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = []
for num in a:
    squares_of_a.append(num ** 2)
squares_of_a


# In[34]:


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = []
for num in a:
    if num % 2 == 1:
        odds_in_a.append(num)
odds_in_a


# In[35]:


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = []
for num in a:
    if num % 2 == 0:
        evens_in_a.append(num)
evens_in_a


# In[45]:


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

sumb = 0
for lst in b:
    for num in lst:
        sumb += num
print(f'The sum of b is: {sumb}')

minb = 100
maxb = 0
for lst in b:
    for num in lst:
        if num < minb:
            minb = num
        if num > maxb:
            maxb = num
print(f'The min of b is: {minb}')
print(f'The max of b is: {maxb}')

avgb = 0
count = 0
for lst in b:
    for num in lst:
        avgb += num
        count += 1
avgb = avgb / count
print(f'The avg of b is: {avgb}')

prodb = 1
for lst in b:
    for num in lst:
        prodb *= num
print(f'The product of b is: {prodb}')

bsquare = []
for lst in b:
    for num in lst:
        bsquare.append(num ** 2)
print(f'The list of squares for b is: {bsquare}')


# In[48]:


# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
b = np.array(b)
# sum_of_b = 0
# for row in b:
#     sum_of_b += sum(row)
sum_of_b = b.sum()
sum_of_b


# In[49]:


# Exercise 2 - refactor the following to use numpy. 
# min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])
min_of_b = b.min()
min_of_b


# In[51]:


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
# max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
max_of_b = b.max()
max_of_b


# In[52]:


# Exercise 4 - refactor the following using numpy to find the mean of b
# mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
mean_of_b = b.mean()
mean_of_b


# In[54]:


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
# product_of_b = 1
# for row in b:
#     for number in row:
#         product_of_b *= number

product_of_b = b.prod()
product_of_b


# In[63]:


# Exercise 6 - refactor the following to use numpy to find the list of squares 
# squares_of_b = []
# for row in b:
#     for number in row:
#         squares_of_b.append(number**2)

squares_of_b = [b ** 2]
print(squares_of_b)


# In[64]:


# Exercise 7 - refactor using numpy to determine the odds_in_b
# odds_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 != 0):
#             odds_in_b.append(number)
odds_in_b = b[b % 2 == 1]
print(odds_in_b)


# In[65]:


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
# evens_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 == 0):
#             evens_in_b.append(number)
evens_in_b = b[b % 2 == 0]
print(evens_in_b)


# In[67]:


# Exercise 9 - print out the shape of the array b.
print(b.shape)


# In[150]:


# Exercise 10 - transpose the array b.
print(b.T)


# In[77]:


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
reshape_b = np.reshape(b, 6)
print(reshape_b)


# In[80]:


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
reshape_b = np.reshape(b, (6, 1))
print(reshape_b)


# In[81]:


## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# In[85]:


# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
c = np.array(c)

print(c.min())
print(c.max())
print(c.sum())
print(c.prod())


# In[86]:


# Exercise 2 - Determine the standard deviation of c.
print(c.std())


# In[88]:


# Exercise 3 - Determine the variance of c.
print(round(c.var(), 2))


# In[92]:


# Exercise 4 - Print out the shape of the array c
print(c.shape)


# In[94]:


# Exercise 5 - Transpose c and print out transposed result.
print(c.transpose())


# In[99]:


# Exercise 6 - Get the dot product of the array c with c. 
print(c.dot(c))


# In[106]:


# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
sum_c_times_c_trans = np.sum(c * np.transpose(c))
print(sum_c_times_c_trans)


# In[109]:


# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
prod_c_times_c_trans = np.prod(c * c.transpose())
print(prod_c_times_c_trans)


# In[134]:


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

d = np.array(d)


# In[118]:


# Exercise 1 - Find the sine of all the numbers in d
sine_d = np.sin(d)
print(sine_d)


# In[121]:


# Exercise 2 - Find the cosine of all the numbers in d
cos_d = np.cos(d)
print(cos_d)


# In[120]:


# Exercise 3 - Find the tangent of all the numbers in d
tan_d = np.tan(d)
print(tan_d)


# In[122]:


# Exercise 4 - Find all the negative numbers in d
print(d[d < 0])


# In[126]:


# Exercise 5 - Find all the positive numbers in d
print(d[d > 0])


# In[127]:


# Exercise 6 - Return an array of only the unique numbers in d.
print(np.unique(d))


# In[128]:


# Exercise 7 - Determine how many unique numbers there are in d.
print(len(np.unique(d)))


# In[129]:


# Exercise 8 - Print out the shape of d.
print(d.shape)


# In[132]:


# Exercise 9 - Transpose and then print out the shape of d.
d_transpose = d.transpose()
print(d_transpose)


# In[133]:


# Exercise 10 - Reshape d into an array of 9 x 2
reshape_d = d.reshape(9, 2)
print(reshape_d)


# In[ ]:




