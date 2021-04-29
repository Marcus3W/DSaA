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

# 0-regular graph
A = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0]]
# 1-regular graph
B = [[0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 1, 0]]
# 2-regular graph
C = [[0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1], [0, 0, 0, 1, 0, 1],
     [0, 0, 0, 1, 1, 0]]
# 3-regular graph
D = [[0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 0, 1], [0, 1, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 0, 1, 1, 0, 1],
     [1, 1, 0, 0, 1, 0]]
# Not regular graph
E = [[0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 0, 1], [1, 1, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 0, 1, 1, 0, 1],
     [1, 1, 0, 0, 1, 0]]
# Lecture matrix
I = [[0, 1, 1, 0, 0], [1, 0, 1, 1, 0], [1, 1, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 1, 1, 0]]
# bipartite graph
BG = [[0, 0, 0, 1, 1, 1], [0, 0, 0, 1, 1, 1], [0, 0, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0],
      [1, 1, 1, 0, 0, 0]]


# Exercise 3

# A graph is regular if the degrees of all the vertices are the same.
# Write a function whose input is an adjacency matrix A of a graph G.
# The function returns true if G is a regular graph and false otherwise.

def isRegularGraph(A):
    # get list of degrees

    d0 = sum(A[0])  # gets the sum of the FIRST ROW

    if d0 == 0:  # checks if FIRST ROW is zero
        return False

    # Do comparisons from i to i -1
    for i in range(1, len(A)):  # checks from SECOND ROW until end
        d = sum(A[i])  # gets the sum of each of the NEXT ROWS
        if d0 != d:  # if FIRST ROW total doesn't match the other rows then return False
            return False
    return True  # if ALL ROWS match


print(isRegularGraph(A))  # It is not a regular graph
print(isRegularGraph(E))  # It is not a regular graph
print(isRegularGraph(I))  # It is not a regular graph

print(isRegularGraph(B))  # It is a regular graph
print(isRegularGraph(C))  # It is a regular graph
print(isRegularGraph(D))  # It is a regular graph
print(isRegularGraph(BG))  # It is a regular graph


# -------------------------------------------------------------------------------

# Exercise 4

# Three different vertices i; j; k
# are called a triangle if i is adjacent to j, j is adjacent to k, and i is adjacent to k.
# In other words, a triangle is just a clique of size 3.

# Write a function TrianglesCount. The input of this function is the adjacency matrix A of a graph G and the output
# is the number of triangles of G.

def TrianglesCount(adj_matrix):
    total = 0

    for i in range(len(adj_matrix)):

        for j in range(len(adj_matrix[i])):

            if adj_matrix[i][j]:

                for k in range(len(adj_matrix[i])):

                    if adj_matrix[i][j] and adj_matrix[j][k] and adj_matrix[i][k]:
                        total += 1
    return total // 6


A = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
print(TrianglesCount(A))

B = [[0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1], [0, 0, 0, 1, 0, 1],
     [0, 0, 0, 1, 1, 0]]
print(TrianglesCount(B))


# -------------------------------------------------------------------------------

# Exercise 5
# Let S be a subset of vertices of G. We say that S is a dominating set of G if each vertex of G is either contained in S or dominated by S.
# Write a function IsDominatingSet whose input is the adjacency matrix A of a graph G and a list S containing a subset of vertices of G.
# The function must return true if S is a dominating set of G and false otherwise.

def isDominated(adj_matrix, subset, v):
    for element_subset in range(0, len(subset)):
        vert = subset[element_subset] # this is the number in the subset (not index) // this PICKS THE ROW BASE ON THE VERTICES
        if adj_matrix[vert][v] == 1: # Using vert to get the ROW and isDominateSet to get the 'COLUMN' shown by 'v'
            return True
    return False

def isDominatingSet(adj_matrix, subset):
    count = 0
    for element_matrix_idx in range(0, len(adj_matrix)): # use this section to check through the COLUMNS of each row
        if isDominated(adj_matrix, subset, element_matrix_idx): # [matrix, subset and the index of the matrix]
            count += 1
    return count == len(adj_matrix) - len(subset)


#    -- 1 -> 3
#  /   |   / |
# 0    |  /  |
#  \   | v   |
#    -- 2 -- 4

# Valid sets
# [1, 4]
# [1, 3]
# [0, 3]
# [0, 4]

# Invalid sets
# [2, 3]
# [0, 1]
# [1, 2]

matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 1, 0]
]

subSet0 = [1, 4]
print(isDominatingSet(matrix, subSet0))

subSet1 = [0, 3]
print(isDominatingSet(matrix, subSet1))

subSet2 = [2, 4]
print(isDominatingSet(matrix, subSet2))

invalidSubSet0 = [2, 3]
print(isDominatingSet(matrix, invalidSubSet0))

# -------------------------------------------------------------------------------

# Exercise 6

# A subset S of vertices of a graph G is called a vertex cover of G if each edge of G has at least one end in S.
# Write a function IsVertexCover whose input is the adjacency matrix A of a graph G and a subset of vertices of G
# (in the form of a list). The function returns true if S is a vertex cover of G and false otherwise.

def isCovered(edge, vx):
  i, j = edge
  if vx == i or vx == j:
    return True
  return False

# Delete covered edges
def deleteEdges(A, S,):
  for i in range(len(A)):
    for j in range(len(A[i])):
      edge = [i, j]
      for k in range(len(S)):
        vx = S[k]
        # if each edge of G has at least one end in S.
        # Delete the edge
        if isCovered(edge, vx):
          A[i][j] = 0
          A[j][i] = 0

def isVertexCover(A, S):
  deleteEdges(A, S)
  # If an edge still exists
  # It means that our subset of vertices doesn't cover the whole graph
  for i in range(len(A)):
    for j in range(len(A[i])):
      if A[i][j]:
        return False
  return True

#    -- 1 -- 3
#  /   |   / |
# 0    |  /  |
#  \   | /   |
#    -- 2 -- 4

# Valid subsets:

# [0, 1, 2, 4]
# [1, 2, 3]
# [1, 2, 4]

# Invalid subsets

# [0, 1]
# [0, 1, 3]
# [1, 2]

# Undirected graph
matrix = [
  [0,1,1,0,0],
  [1,0,1,1,0],
  [1,1,0,1,1],
  [0,1,1,0,1],
  [0,0,1,1,0]
]
subSet0 = [0, 1, 2, 4]
assert isVertexCover(matrix, subSet0), "It is not a Vertex Cover"

# Undirected graph
matrix = [
  [0,1,1,0,0],
  [1,0,1,1,0],
  [1,1,0,1,1],
  [0,1,1,0,1],
  [0,0,1,1,0]
]
subSet1 = [1, 2, 4]
assert isVertexCover(matrix, subSet1), "It is not a Vertex Cover"

# Undirected graph
matrix = [
  [0,1,1,0,0],
  [1,0,1,1,0],
  [1,1,0,1,1],
  [0,1,1,0,1],
  [0,0,1,1,0]
]
subSet2 =  [1, 2, 3]
assert isVertexCover(matrix, subSet2), "It is not a Vertex Cover"

# Undirected graph
matrix = [
  [0,1,1,0,0],
  [1,0,1,1,0],
  [1,1,0,1,1],
  [0,1,1,0,1],
  [0,0,1,1,0]
]
invalidSubSet0 = [0, 1]
assert not isVertexCover(matrix, invalidSubSet0), "It is a Vertex Cover"

# Undirected graph
matrix = [
  [0,1,1,0,0],
  [1,0,1,1,0],
  [1,1,0,1,1],
  [0,1,1,0,1],
  [0,0,1,1,0]
]
invalidSubSet1 = [0, 1, 3]
assert not isVertexCover(matrix, invalidSubSet1), "It is a Vertex Cover"

# Undirected graph
matrix = [
  [0,1,1,0,0],
  [1,0,1,1,0],
  [1,1,0,1,1],
  [0,1,1,0,1],
  [0,0,1,1,0]
]
invalidSubSet2 = [1, 2]
assert not isVertexCover(matrix, invalidSubSet2), "It is a Vertex Cover"

#     1
#     | \
#     |  \
# 0 --|-- 3
#     |  /
#     | /
#     2

# Valid subsets

# [0, 1, 3]
# [1, 3]

# Invalid subsets
# [0, 1]
# [1, 2]

matrix = [
  [0, 0, 0, 1],
  [0, 0, 1, 1],
  [0, 1, 0, 1],
  [1, 1, 1, 0],
]

subSet0 = [0, 1, 3]
assert isVertexCover(matrix, subSet0), "It is not a Vertex Cover"

matrix = [
  [0, 0, 0, 1],
  [0, 0, 1, 1],
  [0, 1, 0, 1],
  [1, 1, 1, 0],
]

subSet1 = [1, 3]
assert isVertexCover(matrix, subSet1), "It is not a Vertex Cover"

matrix = [
  [0, 0, 0, 1],
  [0, 0, 1, 1],
  [0, 1, 0, 1],
  [1, 1, 1, 0],
]

invalidsubSet0 = [0, 1]
assert isVertexCover(matrix, subSet0), "It is a Vertex Cover"

matrix = [
  [0, 0, 0, 1],
  [0, 0, 1, 1],
  [0, 1, 0, 1],
  [1, 1, 1, 0],
]

invalidsubSet1 = [1, 2]
assert isVertexCover(matrix, subSet1), "It is a Vertex Cover"
