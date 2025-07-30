#List operations
#Nested list
print("1. Nested list")
nlist=[[1,2,3],['a','b','c'],[True,False]]
print("Nested list is:",nlist)
#Length of list
print("2. Length of list")
print("Length of the given list is:",len(nlist))
# Concatenation of list
print("3. Concatenation of list")
lst1=[1,2,3]
lst2=[4,5,6]
print("Concatenation of the list is: ",lst1+lst2)
#Membership
print("4. Membership operator")
n=2
if n in lst1:
    print("Yes",n,"is present in lst1")
else:
    print("No",n,"is present in lst1")
#Iteration
print("5. Iteration of list")
lst=[1,2,3,4,5]
print("Iteration of list:",end="")
for i in lst:
    print(i,end=" ")
#Indexing
print("\n6. Indexing of list")
m=3
index=0
for i in range(len(lst)):
    if lst[i]==m:
        index=i
print("Index of",m,"is:",index)
#Slicing
print("7. Slicing of list")
print("Slicing of the list is:",lst[::2])
    
