#Matrix Addition
mat1=[[1,2,3],[1,2,3],[1,2,3]]
mat2=[[2,3,4],[2,3,4],[2,3,4]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(mat1)):
    for j in range(len(mat2)):
        result[i][j]=mat1[i][j]+mat2[i][j]
print("The resultant matrix is:")
for i in range(len(result)):
    print(result[i])
