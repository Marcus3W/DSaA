import math

# WEEK 1 - LISTS

-------------------------------------------------------------------------------

# Exercise 1 

# Suppose that SALARIES is a list of yearly salaries of employees
# working for some organizations. Write a function that computes the average
# salary of those employees that earn more than 30K per year.

def salaries(A) :

	number_of_employees = 0
	total = 0
	
	for i in range(0, len(A)) :
	
		if A[i] > 30000 :
			
		    number_of_employees += 1
		    total += A[i]
	
	return total / number_of_employees 
			
A = [300002, 30001]

print (salaries(A))

-------------------------------------------------------------------------------

# Exercise 2.1

# Write a function whose input is a list A and whose output is
# as follows.

  # If A contains an element greater than 20 then the function returns the
  # index of such an element. (In case there are several suitable elements
  # an arbitrary index can be returned).

  # Otherwise, the output is -1.
  
def findIndex(A) :
	
	for i in range(0, len(A)) :
		
		if A[i] > 20 :
			
			return i
		
	return -1

A = [50,5,6,18,21]
print(findIndex(A))

A = [0,5,6,18,-10]
print(findIndex(A))

-------------------------------------------------------------------------------

# Exercise 2.2

# Write a function whose input are two lists A and B of the same length.
# The program should return true if these two lists are equal (that A[i] = B[i]
# for each index i) and false otherwise.

# Assume both lists are sorted

def isEqual(A, B):
	
	for i in range(0, len(A)) :
		
		if A[i] != B[i] :
			
			return False
	
	return True	

A = [1, 2]
B = [1, 2]
print (isEqual(A, B), "Lists are equal")

A = [1, 2]
B = [1, 3]
print (isEqual(A, B), "Lists are not equal")

-------------------------------------------------------------------------------

# Exercise 3.1

# Write a function computing the smallest odd element of A.

def isOdd(number) :
	
	return (number % 2 == 1)

def smallestOddElement(A) :
	
	smallest = A[0]
	
	for i in range(0, len(A)) :
		
		if A[i] < smallest and A[i] % 2 == 1 :
			
			smallest = A[i]
			
	if not isOdd (smallest) :	
		return - 1
	
	return smallest
	
A = [1, 3, 5, 7, 9, 11]
print (smallestOddElement(A))

A = [2, 4, 6, 8, 10, 12]
print (smallestOddElement(A))

-------------------------------------------------------------------------------
	
# Exercise 3.2

# Write a function computing the second largest element of A.

def secondLargest(A):
	
    largest = 0
    secondLargest = 0
	
    for i in range(0, len(A)):
		
        if A[i] > largest:
			
            secondLargest = largest
            largest = A[i]
			
        elif A[i] > secondLargest:
			
            secondLargest = A[i]
			
    return secondLargest

A = [1, 2, 3, 5, 10]
print (secondLargest(A))

-------------------------------------------------------------------------------

# Exercise 3.3

# Write a function computing an index of the largest element of A. If the
# largest element has several occurrences return the index of an arbitrary
# occurrence.





