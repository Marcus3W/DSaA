import math

# WEEK 2 - MATRICES

# -------------------------------------------------------------------------------

# Exercise 1

# Write a function whose input is a matrix A.
# This function returns true if each row and each column have no repeated occurrences and false otherwise.

A = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]  # true
B = [[2, 2, 3], [3, 1, 2], [2, 3, 1]]  # false - duplicate in row 0
C = [[3, 2, 1], [2, 1, 1], [1, 3, 2]]  # false - duplicate in row 1
D = [[1, 3, 2], [3, 1, 2], [1, 3, 1]]  # false - duplicate in columns 2 (the '2's')


def isNotRepeated(A):
    for i in range(0, len(A)):
        current_row = A[i]  #
        for j in range(0, len(current_row)):
            current_value = current_row[j]
            if isInRow(current_value, current_row, j) and isInColumn(current_value, A, j, i):
                return False
    return True


def isInRow(current_value, current_row, j):
    # Checks if the next item in the row is the same
    for k in range(0, len(current_row)):
        # We skip the element that matches the current one at A[k]
        # We just check the previous and next values in this row
        # This avoids false positives
        if k == j:
            continue
        if current_value == current_row[k]:
            return True
    return False


def isInColumn(current_value, A, j, i):
    for k in range(0, len(A)):
        # We skip the row that matches the current one
        # We just check the previous and next values in this column
        # This avoids false positives
        if k == i:
            continue
        if current_value == A[k][j]:
            return True
    return False


print(isNotRepeated(A))
print(isNotRepeated(B))
print(isNotRepeated(C))
print(isNotRepeated(D))


## ALTERNATIVE SOLUTION ##

def isRepeat(A):  # from week 1
    for i in range(0, len(A) - 1):  # minus 1 because it needs to be 0,1,2 and not length of 3
        for j in range(i + 1, len(A)):
            if A[i] == A[j]:
                return True
    return False


def noRepeat(A):
    for i in range(len(A)):
        column = []
        if isRepeat(A[i]):  # takes the current 'row' of the first array
            return False
        for j in range(len(A[i])):
            column.append(A[i][j])
        if isRepeat(column):
            return False
    return True


print(noRepeat(A))
print(noRepeat(B))
print(noRepeat(C))
print(noRepeat(D))

# -------------------------------------------------------------------------------

# Exercise 2

# The input of the tasks of this exercise is a matrix MARKS whose rows correspond to students and columns correspond
# to modules. The entries of the matrix are marks of the corresponding student for the corresponding module.

MARKS = [[40, 40, 40, 40, 20], [50, 60, 20, 10, 20], [20, 40, 20, 30, 30], [20, 20, 30, 20, 20]]


# Exercise 2.1

# Write a function returning the list of average marks of all students.
# Assume that all modules are taken and have marks

def ST_Average(MARKS):
    student_Average = []

    for i in range(0, len(MARKS)):
        curAvg = aveRowMarks(MARKS[i])
        student_Average.append(curAvg)

    return student_Average


def aveRowMarks(row):
    avg = 0
    count = 0

    for element in range(0, len(row)):
        avg += row[element]
        count += 1

    return round(avg / count, 2)


print(ST_Average(MARKS))


## ALTERNATIVE SOLUTION ## - This works - but doesnt use RANGE or LEN

def student_averages(C):
    studentAve = []

    for results in C:
        studentTotal = 0
        modulesTaken = 0

        for total in results:
            studentTotal = studentTotal + total
            modulesTaken = modulesTaken + 1

        else:
            average = studentTotal / modulesTaken
            studentAve.append(average)

    return studentAve


print(student_averages(MARKS))


# -------------------------------------------------------------------------------

# Exercise 2.2
# Write a function returning the list of average marks of all modules.
# Assume that all modules are taken and have marks

def getColumn(A, j):
    column = []

    for i in range(0, len(A)):
        column.append(A[i][j])
    return column


def avgMarks(A):
    avg = 0
    count = 0

    for i in range(0, len(A)):
        avg += A[i]
        count += 1

    return round(avg / count, 2)


def MODAverages(marks):
    averages = []

    for i in range(0, len(marks[0])):
        curCol = getColumn(marks, i)
        curAvg = avgMarks(curCol)
        averages.append(curAvg)

    return averages


print(MODAverages(MARKS))

# -------------------------------------------------------------------------------
