factor=1

myNumber = int(input("Enter the number whose factorial you want!\n"))

if myNumber < 0: 
    print("Number should be zero or above")
else: 
    while(myNumber > 1):
        factor = factor * myNumber
        myNumber = myNumber - 1

print("Factorial of the number is: ")
print(factor)