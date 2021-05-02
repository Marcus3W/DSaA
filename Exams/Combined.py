# Exam Summer 2020

# Exercise 1

# For the purpose of writing this program, you can use functions max(L) and min(L)
# that respectively return the largest and the smallest elements of a list L of integers.
# Let A be an nxn square matrix.
# For example, consider the 3x3 matrix below.
# [ [1,2,3],
# [5,3,4]
# [6,7,2]]

# (a) Write a program that computes the largest element of each row and then prints
# the smallest one of these largest elements.
# For example, these largest row elements of the above matrix are 3, 5, 7 and the
# smallest of them is obviously 3.

def bigSmall(A):
    largest = []

    for i in range(0, len(A)):
        maxEl = max(A[i])
        largest.append(maxEl)

    return min(largest)


A = [[1, 2, 3], [5, 3, 4], [6, 7, 2]]

print(bigSmall(A))


# -------------------------------------------------------------------------------

# (b) Write a program that computes the largest element of each column and then
# prints the smallest one out of these largest elements.
# For example, these largest column elements for the above matrix are 6, 7, 4 and
# the smallest is 4.

def getColumnArray(matrix, j):
    column = []
    for i in range(0, len(matrix)):
        column.append(matrix[i][j])
    return column


def largestColumnElement(A):
    largest_col = []

    for j in range(0, len(A[0])):
        cur_column_max = max(getColumnArray(A, j))
        largest_col.append(cur_column_max)

    return min(largest_col)


print(largestColumnElement(A))


# -------------------------------------------------------------------------------

# Exam Autumn 2020

# Exercise 1

# For the purpose of writing this program, you can use functions max(L) and min(L)
# that respectively return the largest and the smallest elements of a list L of integers.
# Let A be an n x n square matrix.

# [ [1,2,3],
# [5,3,4]
# [6,7,2] ]

# (a) Write a program that computes the smallest element of each column and then
# prints the largest one out of these smallest elements.#

# For example, these smallest column elements for the above matrix are 1; 2; 2
# while the largest is 2.

def getColumn(A, j):
    column = []

    for i in range(0, len(A)):
        column.append(A[i][j])
    return column


def smallestLargest(A):
    array = []

    for j in range(0, len(A)):
        current_column = min(getColumn(A, j))
        array.append(current_column)
    print(max(array))


A = [[1, 2, 3],
     [5, 3, 4],
     [6, 7, 2]]

smallestLargest(A)


# -------------------------------------------------------------------------------

# (b) Write a program that prints 'YES' if in each column of A all the values are
# distinct and 'NO' otherwise. For example, for the matrix above, the answer
# should be 'YES'. If for instance we change the bottom-right element to 3 then
# the answer becomes 'NO' as the last column has repeated elements. (10 marks)

# NOTES - The answer here is to get the COLUMN FIRST - create a new array
#         once you have the column, check this new 'array' using isDistinct function.
#         cycle through these two auxillary functions until you get a result.


def getColumnArray(matrix, j):
    column = []
    for i in range(0, len(matrix)):
        column.append(matrix[i][j])
    return column


def isDistinct(L):
    #         **THIS IS HOW YOU CHECK ALL THREE WITHOUT THE OUT OF BOUNDS ERROR**
    for i in range(0, len(L) - 1):
        if L[i] == L[i + 1]:
            return False
    return True


def NoRepeatColumns(A):
    for i in range(0, len(A)):
        current_column = getColumnArray(A, i)

        if (isDistinct(current_column) == 0):
            return False
    return True


A = [[1, 2, 3], [5, 3, 4], [6, 7, 2]]
print(NoRepeatColumns(A))
B = [[1, 2, 3], [1, 3, 4], [1, 7, 2]]
print(NoRepeatColumns(B))


# -------------------------------------------------------------------------------

# Exam Summer 2020

# Exercise 2

# (a) Let A be a list sorted in the increasing order. Design an O(log n) algorithm that
# returns the following:

# If there is an element different from both the first and the last element of
#   A, return the index of this element in A. If there are several such elements,
#   any can be returned. For example if A = [1, 1, 2, 4, 5] then 2 and 3 are both
#   legitimate returned values.

# If A has no elements different from both the first and the last one then return -1.

# Hint: this question is a minor modification of a question given in Coursework 2.


# -------------------------------------------------------------------------------

# Exam Autumn 2020

# Exercise 2

# (a) Let A be an array sorted in the increasing order. Design an O(n) algorithm that
# prints 'YES' if all the elements of A are distinct and 'NO' otherwise. (5 marks)

def areElementsDistinct(A):
    if A[0] == A[-1]:
        return "NO"

    for i in range(0, len(A) - 1):

        if A[i] == A[i + 1]:
            return "NO"

    return "YES"


A = [10, 10, 11, 11, 12, 13, 15]
print(areElementsDistinct(A))
B = [10, 11, 12, 13, 15]
print(areElementsDistinct(B))


# -------------------------------------------------------------------------------

# A way to formally define a sorted array A of n elements is to say that for each i between 0 and n - 2, A[i] <= A[i + 1].

# Let us say that A is almost sorted if this rule is correct for all but one number k between 0 and n - 2.
# In other words, A[k] > A[k+1] but for each i such that i != k and 0 <= i <= n - 2, A[i] <= A[i+1].

# (b) Design an O(n) algorithm whose input is an almost sorted array A and that
# solves the same task as for the first part: prints 'YES' if all the elements of A
# are distinct and 'NO' if there are repetitions. (15 marks)

###################
# THIS MERGESORT ISN'T TECHNICALLY NEEDED FOR THE QUESTION - BUT HAS BEEN ADDED TO SHOW IT WORKS

def mergeSort(l, m):
    result = []
    i = j = 0
    total = len(l) + len(m)
    while len(result) != total:
        if len(l) == i:
            result += m[j:]
            break
        elif len(m) == j:
            result += l[i:]
            break
        elif l[i] < m[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(m[j])
            j += 1
    return result


# THIS IS THE ACTUAL ANSWER

def almostSorted(A):
    for i in range(0, len(A) - 1):
        if A[i] > A[i + 1]:
            k = i

    # merge sort list
    n = len(A)
    sorted = mergeSort(A[0: k + 1], A[k + 1: n])
    print(sorted)

    # check distinct
    return areElementsDistinct(sorted)


A = [10, 11, 20, 12, 13, 15]
print(almostSorted(A))  # SHOULD BE YES - ALL DISTINCT
B = [10, 10, 16, 13, 14]
print(almostSorted(B))  # SHOULD BE NO - DUPLICATE (10)


# -------------------------------------------------------------------------------

# Exam Autumn 2020

# Exercise 4

# Let G be a graph on vertices 0; : : : n - 1. Let A be the adjacency matrix of G. A
# triangle of G is a set of three distinct vertices i; j; k such that i is adjacent to j, i is
# adjacent to k and j is adjacent to k

# (a) Design a function whose input is A and three vertices i; j; k that returns true if
# i; j; k form a triangle and 'NO' otherwise. The runtime of the function must be O(1). (5 marks)

def isTriangle(A, i, j, k):
    if A[i][j] == 1 and A[i][k] == 1 and A[j][k] == 1:
        return True
    else:
        return "NO"


A = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 0]
]

print(isTriangle(A, 0, 1, 2), "should be yes")
print(isTriangle(A, 0, 1, 3), "should be no")


# -------------------------------------------------------------------------------

# (b) Use the function of the first part to design an algorithm whose input is A
# and that prints the number of triangles of G. Note that you need to take
# necessary precautions to avoid the same triangle being counted more than once. (15 marks)

# NOTES - What's important here is to keep k greater than j and j greater than i
#  think of it as creating 'subsets'
def number_of_triangles(A):
    count = 0
    n = len(A)
    for i in range(0, len(A) - 2):
        for j in range(i + 1, len(A) - 1):
            for k in range(j + 1, len(A)):
                if isTriangle(A, i, j, k) == True:
                    count += 1
    return count


print(number_of_triangles(A), "count of triangles")


# -------------------------------------------------------------------------------

# Exam Autumn 2020

# Exercise 5

# Let G be a graph on vertices 0; : : : n - 1. Let A be the adjacency matrix of G.
# Let S be a subset of vertices of G (treat it like a list all of whose elements are numbers
# between 0 and n - 1 without repetitions).

# (a) Write a program whose input is A and S.
# The program must print 'YES' if G has a vertex v, not contained in S such that v is adjacent to all the vertices of S.
# Otherwise the program must print 'NO'. (10 marks)

# Answer.
# We design a function dominates that tests whether the given vertex v is adjacent to all the vertices of S.
# The main program runs a loop through all vertices of A and uses the function to check whether the currently explored
# vertex v is adjacent to all of S.

# Note we do not need to apply an additional check as to whether v belongs to S because if it is,
# it will not be adjacent to all vertices of S because it is not adjacent to itself.

def isDominated(A, S, i):
    for j in S:
        if A[j][i] == 0:
            return False
    return True


def check(A, S):
    flag = 0
    for i in range(0, len(A)):
        if isDominated(A, S, i):
            flag = 1

    if flag == 1:
        print("YES")
    else:
        print("NO")


S = [0, 1, 2]
check(A, S)


# -------------------------------------------------------------------------------

# (b) Write a program whose input is A and S.
# The program must print 'YES' if G has two vertices v1, and v2, neither of them contained in S
# such that each vertex of S is adjacent either to v1 or to v2.
# Otherwise, the program must print 'NO'. (10 marks)

# Answer.
# The answer is similar to the previous one with two vertices explored instead of v.
# The main non-trivial point is that in the IsDominated function
# the AND must be used inside the main condition.

def isDominated(A, S, v1, v2):
    for u in S:
        if A[u][v1] == 0 and A[u][v2] == 0:
            return False
    return True


def check(A, S):
    flag = 0
    for v1 in range(0, len(A)):
        for v2 in range(0, len(A)):
            if isDominated(A, S, v1, v2):
                flag = 1

    if flag != 1:
        print("NO")
    else:
        print("YES")


S = [0, 1, 2]
check(A, S)
