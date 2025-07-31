#Removing punctuations from a string
s="Py@t!h,on&"
s1=""
for i in s:
    if i not in "!@#$%^&*.,":
        s1+=i
print("Original string:",s)
print("String after removing punctutations:",s1)
