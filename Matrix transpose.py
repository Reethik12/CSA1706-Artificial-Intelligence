#Transpose of a matrix
matrix=[[1,4,7],[2,5,8],[3,6,9]]
transpose=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        transpose[i][j]=matrix[j][i]
print("The transpose of the matrix is:")
for i in range(len(transpose)):
    print(transpose[i])
