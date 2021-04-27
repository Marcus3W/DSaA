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

def largestIndex(A):
	
	largest_Index = 0
	largest_Number = A[0]
	
	for i in range(1, len(A)) :  ## this is 1 because we have already stored '0' as the largest number
		
		if A[i] > largest_Number :
			
			largest_Number = A[i]
			largest_Index = i
	
	return largest_Index

A = [1, 2, 3, 10]
print (largestIndex(A))

-------------------------------------------------------------------------------

# Exercise 4

# The input of all the functions considered in this exercise are two lists SALARIES and GENDERS. 
# The indices of these lists correspond to employees (you can think of the indices as IDs of employees). 
# SALARIES[i] is the early salary of employee i. 
# GENDERS[i] is the gender of employee i. 
# In particular, GENDER[i] = 'F' if employee i is female and GENDER[i] = 'M' if employee i is male.

# Exercise 4.1

# Write a program that returns tuple (FSAL;MSAL) that are respectively salaries of female and male employees.

def salaries(Salaries, Genders):
	
	FSAL = []
	MSAL = []
	
	
	for i in range(0, len(Salaries)) :
		
		if Genders[i] == 'F' :
			
			FSAL.append(Salaries[i])
		
		else :
			MSAL.append(Salaries[i])
	
	return (FSAL, MSAL)

# Exercise 4.2

# Write a program that returns tuple (avf; avm) that are respective average salaries of female and male employees.

def averageSalaries(Salaries, Genders):
    MSAL_Total = 0
    FSAL_Total = 0
    number_Of_Male_Employees = 0
    number_Of_Female_Employees = 0

    for i in range(0, len(Salaries)):
        if Genders[i] == 'F':
            FSAL_Total += Salaries[i]
            number_Of_Female_Employees += 1
        else:
            MSAL_Total += Salaries[i]
            number_Of_Male_Employees += 1
    
    return [FSAL_Total / number_Of_Female_Employees, MSAL_Total / number_Of_Male_Employees]

# Exercise 4.3

# Write a program that returns tuple (maxf;maxm) that are respectively the largest salaries of female and make employees.

def largestSalaries(Salaries, Genders):
    largest_MSAL = 0
    largest_FSAL = 0

    for i in range(0, len(Salaries)):
        if Genders[i] == 'F':
            if Salaries[i] > largest_FSAL:
                largest_FSAL = Salaries[i]
        else:
            if Salaries[i] > largest_MSAL:
                largest_MSAL = Salaries[i]
    
    return [largest_FSAL, largest_MSAL]

print(salaries([45000, 30000, 90000, 10000], ['M', 'F', 'F', 'M']), "Male and Female Salaries")
print(averageSalaries([45000, 30000, 90000, 10000], ['M', 'F', 'F', 'M']), "Average Salaries per Gender")
print(largestSalaries([45000, 30000, 90000, 10000], ['M', 'F', 'F', 'M']), "Largest Salaries per Gender")

-------------------------------------------------------------------------------

# Exercise 5

# Write a function that returns true if there is a female and a male employees that receive the same salary and false otherwise.

def isDifferentGenders(gender_1, gender_2):
	
  return (gender_1 == 'F' and gender_2 == 'M') or (gender_1 == 'M' and gender_2 == 'F')


def isEqualSalary(salary_1, salary_2):
	
  return salary_1 == salary_2


def hasCommonElement(Salaries, Genders):
	
    for i in range(0, len(Salaries)):
		
        for j in range(1, len(Salaries)):
			
            # Only check for salaries differences if genders are different
            if isDifferentGenders(Genders[i], Genders[j]): # checks to see if the genders are different, if true continue into next nest, if false next index
				
                if isEqualSalary(Salaries[i], Salaries[j]):
					
                    return True
				
    return False

print (hasCommonElement([30000, 30000, 15000, 10000], ['M', 'F', 'F', 'M']), "Has a common element"
print (hasCommonElement([30000, 31000, 15000, 10000], ['M', 'F', 'F', 'M']), "Hasnt got a common element"

