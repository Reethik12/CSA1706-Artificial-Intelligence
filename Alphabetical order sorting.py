#Alphabetical order sorting
sentence="Basics of artificial intelligence"
lower=sentence.lower()
words=lower.split()
words.sort()
print("Words in alphabetical order:")
for i in words:
    print(i,end=" ")

