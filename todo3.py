# Challenge 1
#Biggie Size
#Given an array, write a function that changes all positive numbers in the array to “big”.
#Example: makeItBig([-1,3,5,-5]) returns that same array, changed to [-1,"big","big",-5].

# def makeItBig(n):
#     for i in range(len(n)):
#         if n[i] > 0:
#             n[i] = 'big'
#     return n

# print(makeItBig([1,2,3,-2,-3,-4]))






#Challenge number 2
# Print Low, Return High
#Create a function that takes an array of numbers. 
#The function should print the lowest value in the array, and return the highest value in the array.

# def high_low(n):
#     print(min(n))
#     return max(n)


# print(high_low([4,8,1,5,9,0]))






#Challenge number 3
# Double Vision
# Given an array, create a function to return a new array where each value in the original has been doubled. 
# Calling double([1,2,3]) should return [2,4,6] without changing original.

# def new_list(n):
#     new = []
#     for i in n:
#         i += i
#         new.append(i)
#     return new

# print(new_list([3,5,6]))







# Challenge number 4
# Count Positives
# Given an array of numbers, create a function to replace last value with the number of positive values. 
# Example,  countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.

# def count_positive(n):
#     count = 0
#     for i, v in enumerate(n):
#         if v > 0:
#             count += 1
#         if count > 0:
#             n[-1] = count
#     return n

# print(count_positive([2,-1,3,5,9]))






# Challenge number 5
# Create a function that accepts an array. Every time that array has three odd values in a row, print "That’s odd!" 
# Every time the array has three evens in a row, print "Even more so!"
#Example [1,1,2,5,5,5,10,10,10]
# Output:
#That's Odd
# That's Even

# Loop through the list
# 
# def odd_even(n):
#     i = 0
#     index_1 = 1
#     index_2 = 2
#     index_3 = 3
#     while i < len(n):
#         if n[index_1] % 2 == 1:
#             if n[index_2] % 2 == 1:
#                 if n[index_3] % 2 == 1:
#                     print('Those are odd number')
#         elif n[index_1] % 2 == 0:
#             if n[index_2] % 2 == 0:
#                 if n[index_3] % 2 == 0:
#                     print('Those are even number')
#                     break
#         i += 1
#         index_1 += 1 
#         index_2 += 1
#         index_3 += 1
#     return n

# odd_even([1,5,5,5,2,2,2,8])







# Challenge number 6
# Increment the Seconds
# Given an array, add 1 to the value located at each odd indices of the array ([1], [3], etc.), 
# console.log all values and return arr.

# Example [1,2,3,4,5,6] would become [1,3,3,5,5,7]
# def odd(n):
#     for i in range(len(n)):
#         if n[i] % 2 == 0:
#             n[i] += 1
#     return n

# print(odd([1,2,3,4,5,6]))






# Challenge number 7
#Previous Lengths
# You are passed an array containing strings. 
# Working within that same array, replace each string with a number – the length of the string at previous array index, 
# replace the first value with the length of the last string – and return the array.
# Example ['this', 'is', 'an', 'array']
# Output [5,4,2,2]

# def convert_to_int(n):
#     temp = n[0]
#     n[0] = len(n[3]) # array
#     temp_1 = n[1]
#     n[1] = len(temp) # this
#     temp_2 = n[2]
#     n[2] = len(temp_1) # is
#     n[3] = len(temp_2) # an
#     return n

# print(convert_to_int(['This', 'is', 'an', 'array']))







# Challenge number 8
# Add Seven to Most
#Build a function that accepts an array. Return a new array with all values except the first index, adding 7 to each. 
#Do not alter the original array.

# Example [1,2,3,4,5]
# Output [9,10,11,12]

# def seven(n):
#     new = []
#     for i in range(1,len(n)):
#         total = n[i] + 7
#         new.append(total)
#     return new
# print(seven([1,2,3,4,5]))







# Challenge number 9
#Reverse Array
#Given array, write a function to reverse values, in-place. 
#Example: reverse([3,1,6,4,2]) returns same array, containing [2,4,6,1,3].

# def revers(n):
#     n.reverse()
#     return n

# print(revers([3,1,6,4,2]))







# Challenge number 10 
#Outlook: Negative
#Given an array, create and return a new one containing all the values of the provided array, 
#made negative (not simply multiplied by -1). Given [1,-3,5], return [-1,-3,-5].

# def negative(n):
#     new = []
#     for i in range(len(n)):
#         if n[i] > 0:
#             n[i] = -n[i]
#         new.append(n[i])
#     return n


# print(negative([1, -3, 5]))







# Challenge number 11


#Always Hungry
#Create a function that accepts an array, and prints "yummy" each time one of the values is equal to "food".
#If no array elements are "food", then print "I'm hungry" once.
#Example [1,2,'food',5]
#Output: yummy

# def hungry(n):
#     for i in n:
#         if i == 'food':
#             print('Yummy')
#             return 
#     print('Im hungry')
# hungry([1,2,'food',5])






# Challenge number 12
# Swap Toward the Center
# Given array, swap first and last, third and third-to-last, etc. 
# Input[true,42,"Ada",2,"pizza"] becomes ["pizza",42,"Ada",2,true].  Change [1,2,3,4,5,6] to [6,2,4,3,5,1].

# def swap(n):
#     temp = n[0] # True
#     n[0] = n[-1] # 'pizza'
#     n[-1] = temp # 'True
#     temp_1 = n[2]
#     n[2] = n[-3]
#     n[-3] = temp_1
#     return n

# print(swap([1,2,3,4,5,6] ))






# Challenge number 13
#Scale the Array
#Given array arr and number num, multiply each arr value by num, and return the changed arr.
#Example scaleArr([1,2,3,4,5],3) = 3,6,9,12,15

# def scaleArr(num, mul):
#     for i,v in enumerate(num):
#         all = num[i] * mul
#         print(all)
#     return num

# scaleArr([1,2,3,4,5], 3)



