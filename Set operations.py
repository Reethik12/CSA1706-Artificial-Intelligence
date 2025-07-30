# Set operations
A=[1,2,3,4]
B=[3,4,5,6]
# Union
union=[]
for x in A:
  if x not in union:
    union.append(x)
for x in B:
  if x not in union:
    union.append(x)
print("1. Union:",union)
# Intersection
intersection=[]
for x in A:
  if x in B and x not in intersection:
    intersection.append(x)
print("2. Intersection:",intersection)
# Difference A - B
difference=[]
for x in A:
  if x not in B:
    difference.append(x)
print("3. A-B Difference:",difference)
# Symmetric Difference
sym_diff=[]
for x in union:
  if x not in intersection:
    sym_diff.append(x)
print("4. Symmetric Difference:",sym_diff)
