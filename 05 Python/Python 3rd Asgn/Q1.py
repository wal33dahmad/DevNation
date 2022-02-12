str = input("Enter an Alphabe(s) ")

evenSum = 0
oddSum = 0

for i in range(1,len(str)+1):
    ascii = ord(str[i-1]) 
    if (i % 2) == 0:
        evenSum +=ascii
    else:
        oddSum += ascii

sum = evenSum + oddSum 

print("Total ASCII Sum:", sum)
print("ASCII Sum of odd-numbered characters:", oddSum)
print("ASCII Sum of even-numbered characters:", evenSum)