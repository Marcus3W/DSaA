# Exercise 1

# For the purpose of writing this program, you can use functions max(L) and min(L)
# that respectively return the largest and the smallest elements of a list L of integers.
# Let A be an nxn square matrix.
# For example, consider the 3x3 matrix below.

# (a) Write a program that computes the largest element of each row and then prints
# the smallest one of these largest elements.
# For example, these largest row elements of the above matrix are 3, 5, 7 and the
# smallest of them is obviously 3.

def bigSmall(A) :
    largest = []

    for i in range(0, len(A)) :

        maxEl = max(A[i])
        largest.append(maxEl)

    return min(largest)

A = [  [1,2,3],  [5,3,4],  [6,7,2]  ]

print(bigSmall(A))


---------------#### ALTERNATE SOLUTION ####------------

def printSmallest(matrix):
    largest = []

    for i in range(0, len(matrix)):
        row_largest = 0
        for j in range(1, len(matrix[i])):
            if matrix[i][j] > row_largest:
                row_largest = matrix[i][j]

        largest.append(row_largest)

    return min(largest)


A = [[1, 2, 3], [5, 3, 4], [6, 7, 2]]

print(printSmallest(A))

# -------------------------------------------------------------------------------

# (b) Write a program that computes the largest element of each column and then
# prints the smallest one out of these largest elements.
# For example, these largest column elements for the above matrix are 6, 7, 4 and
# the smallest is 4.

def getColumn(matrix, j):
    column = []
    for i in range(0, len(matrix)):
        column.append(matrix[i][j])
    return column


def largestColumnElement(matrix):
    largest_col = []

    for j in range(0, len(A[0])):  # gets each row
        cur_column_max = max(getColumn(matrix, j))
        largest_col.append(cur_column_max)

    return min(largest_col)


print(largestColumnElement(A))

A = [[1, 2, 3], [5, 3, 4], [6, 7, 2]]

# -------------------------------------------------------------------------------

# Exercise 2

# (a) Let A be a list sorted in the increasing order. Design an O(log n) algorithm that
# returns the following:
#
# If there is an element different from both the first and the last element of
#   A, return the index of this element in A. If there are several such elements,
#   any can be returned. For example if A = [1, 1, 2, 4, 5] then 2 and 3 are both
#   legitimate returned values.
#
# If A has no elements different from both the first and the last one then return -1.
#   Hint: this question is a minor modification of a question given in Coursework
#   2.

def findMiddle(A):
    length = len(A)
    if A[0] >= A[length - 1]:
        return - 1

    # Now implement a standard binary-search

    # GET INDEXES
    first = 0
    last = length - 1
    mid = first + last // 2

    while mid != first and mid != last:  # loop check to ensure mid doesnt equal first and last elements

        if A[mid] != A[first] and A[mid] != A[last]:
            return mid

        if A[mid] == A[first]:
            first = mid + 1
        else:
            last = mid - 1

        mid = (first + (last - first)) // 2

    return -1


A = [1, 1, 2, 4, 5]
print(findMiddle(A))
A = [1, 1, 1, 1, 3, 4, 5]
print(findMiddle(A))

# -------------------------------------------------------------------------------

# (b) Design an algorithm returning 'YES' if A has 4 different elements and 'NO'
# otherwise.
#
# Hint: It is possible to use the solution of part a) of this question as a function
# and to run this function at most three times.

def findMiddleFour(A):
    mid = findMiddle(A)

    if mid == -1:
        return "NO"

    mid1 = findMiddle(A[ 0 : mid+1 ])  # from first index to mid
    mid2 = findMiddle(A[ mid+1 :  ])  # from mid+1 to last index

    if mid1 == -1 or mid2 == -1 :
        return "NO"

    return "YES"

A = [1, 2, 3, 4, 5, 6]
print(findMiddleFour(A))

# -------------------------------------------------------------------------------

# Exercise 3

# -------------------------------------------------------------------------------

# Exercise 4

# Let G be a graph on vertices 0, ..., n - 1. Let A be the adjacency matrix of G.

# (a) Design an algorithm whose input is A. The algorithm should print the maximum
# degree of a vertex of G.

def maxDegree(A) :
    degreeArray = []
    for i in range(0, len(A)) :
        degrees = sum(A[i])
        degreeArray.append(degrees)
    print (max(degreeArray))

A = [[0,1,1,0,0], # 0
     [1,0,1,1,0], # 1
     [1,1,0,0,1], # 2
     [0,1,0,0,1], # 3
     [0,0,1,1,0]] # 4

maxDegree(A)

# -------------------------------------------------------------------------------

# (b) A graph is regular if all its vertices have the same degree. Design an algorithm
# whose input is A. The algorithm should print 'YES' if G is regular and 'NO'
# otherwise.

def isRegular(A, end=None) :
    cur_degrees = sum(A[0])
    for i in range(1, len(A)) :
        degrees = sum(A[i])

        if degrees != cur_degrees :
            print ("NO")
            return

        else:
            cur_degrees = degrees

    print ("YES")

isRegular(A) # PRINTS NO

B = [[0,1,1,0,0], # 0
     [1,0,0,1,0], # 1
     [1,0,0,0,1], # 2
     [0,1,0,0,1], # 3
     [0,0,1,1,0]] # 4


# ------ ALTERNATE SOLUTION - Filipe ------ #

isRegular(B) # PRINTS YES

def isRegular2(A, end=None) :
    degreeArray = []
    for i in range(1, len(A)) :
        degrees = sum(A[i])
        degreeArray.append(degrees)

    degreeArray.sort()

    if degreeArray[0] != degreeArray[len(degreeArray)-1] :
        print("NO")
    else:
        print ("YES")

isRegular2(A) # PRINTS NO
isRegular2(B) # PRINTS YES

# -------------------------------------------------------------------------------

# Exercise 5

# Let G be a graph on vertices 0, ... , n - 1.
# Let A be the adjacency matrix of G.
# Let S be a subset of vertices of G (treat it like a list all of whose elements are numbers between 0 and n - 1 without repetitions).

# (a) Write a program whose input is A and S.
# The program must print all the edges of the subgraph of G induced by S (to print an edge means to print both its ends).

def printEdges(A,S):

    for i in range(0, len(S) - 1) :

        for j in range(i + 1, len(S)):

            end1 = S[i]
            end2 = S[j]

            # looks in the matrix, end1 is the row itself and end2 is looking for element
            # in said row that matches the next subset element, i.e. column (Row 1, column 2)
            if A[end1][end2] == 1:

                print(f'{end1}--{end2}')

#        1  2     4
A = [[0, 1, 1, 0, 0],
     [1, 0, 1, 1, 0],  # 1
     [1, 1, 0, 0, 1],  # 2
     [0, 1, 0, 0, 1],
     [0, 0, 1, 1, 0]]  # 4

S = [1,2,4]
printEdges(A,S)

# -------------------------------------------------------------------------------

# (b) Let Connect be a function whose input is the adjacency matrix of a graph. The
# function returns true if the graph is connected and false otherwise. Use the
# function (you do not need to write its code just call it when needed) to design
# an algorithm whose input is A and S. The program should print 'YES' if the
# subgraph of G induced by S is connected and 'NO' otherwise.

###################
# THIS BFS ISN'T TECHNICALLY NEEDED FOR THE QUESTION - BUT HAS BEEN ADDED TO SHOW IT WORKS
def connect(B): # BFS
    visited = [0] * len(B)
    q = [0]

    while (len(q) > 0):
        v = q.pop()
        visited[v] = 1

        for i in range(0, len(B)):
            if B[v][i] != 0 and not visited[i]:
                q.append(i)

    for i in range(0, len(visited)):
        if visited[i] == 0:
            return False

    return True
###################

# THIS IS THE ACTUAL ANSWER
def connectedSubGraph(A, S):
    B = []
    
    for i in range(0, len(S)) :
        end1 = S[i]
        rowB = []   #  initalizing the vertex end1

        for j in range(0, len(S)) :
            end2 = S[j]
            rowB.append(A[end1][end2])

        B.append(rowB)

    if connect(B):
        print("Connected")
    else:
        print("Not Connected")


#    -- 1 -- 3 --
#  /              \
# 0                5
#  \              /
#    -- 2 -- 4 --

# Valid set:
# [3, 4, 5]

A = [
  [0, 1, 1, 0, 0, 0],
  [1, 0, 0, 1, 0, 0],
  [1, 0, 0, 0, 1, 0],
  [0, 1, 0, 0, 0, 1],
  [0, 0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1, 0]
]

S = [3, 4, 5]

connectedSubGraph(A, S)
