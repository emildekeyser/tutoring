#Initialise the matrix as an empty list.
matrix = []

#Ask the user for the amount of rows and the amount of columns the matrix should contain.
rows = int(input("How many rows should the matrix have?: "))
columns = int(input("How many columns should the matrix have?: "))

#Fill the matrix with rows containing integers that the user provides.
for i in range(rows):
    row = []
    for j in range(columns):
        row.append(int(input("What value would you like in the position in row " + str(i) + " and column "+ str(j) + " ?: ")))
    matrix.append(row)

#Initialise a list of saddle points as an empty list.
saddle_points = []

#Iterate over all elements of the matrix that are not in the first row, last row, first column or last column, since
#only such elements can be saddle points.
for i in range(1, rows-1):
    for j in range(1, columns-1):
        #Check for the two possible ways in which elements could be saddle points. If an element is a saddle point, add
        #its coordinates as a tuple to the list of saddle points.
        if((matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i+1][j] and matrix[i][j] > matrix[i][j-1] and matrix[i][j] > matrix[i][j+1])
        or matrix[i][j] > matrix[i-1][j] and matrix[i][j] > matrix[i+1][j] and matrix[i][j] < matrix[i][j-1] and matrix[i][j] < matrix[i][j+1]):
            saddle_points.append((i, j))

#Print the list of saddle points.
print("The saddle points are positioned on coordinates: " + str(saddle_points))