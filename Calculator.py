#Calculator Program
num1=int(input("Enter the number 1:"))
num2=int(input("Enter the number 2:"))
print("Operation to perform:\n1. Addition\n2. Subtraction\n3. Multplication\n4. Division")
choice=int(input("Enter the choice: "))
if choice==1:
    sum=num1+num2
    print("The addition of",num1,"and",num2,"is",sum)
elif choice==2:
    diff=num1-num2
    print("The subtraction of",num1,"and",num2,"is",diff)
elif choice==3:
    prod=num1*num2
    print("The multiplication of",num1,"and",num2,"is",prod)
else:
    if num2==0:
        print("Number cannot be divided by zero")
    else:
        div=num1/num2
        print("The division of",num1,"and",num2,"is",div)
