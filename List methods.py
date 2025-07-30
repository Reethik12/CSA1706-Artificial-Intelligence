#List methods
#Add
lst=[10,20,30]
print("Original list:",lst)
print("1. Adding element into the list")
lst.append(40)
print("List after adding 40:",lst)
#Insert
print("2. Inserting element(s) into the list")
lst.insert(50,60)
print("List after inserting 50 & 60:",lst)
#Extend
print("3. Extending the list")
lst.extend([70,80])
print("List after extending [70,80]:",lst)
#Remove
print("4. Removing element from the list")
print("Element removed:",lst.pop())
print("List after removing an element:",lst)
