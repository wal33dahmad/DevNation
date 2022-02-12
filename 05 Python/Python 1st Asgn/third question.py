# Write a program that takes integer inputs from the user until he/she presses q ( Ask to press q to quit after every integer input ). Print average and product of all numbers.

average = 0
sum = 0
totalNum = 0
product = 1
state = True

while state:
    num = input("Enter number\n")
    num = int(num)
    sum = sum + num
    totalNum = totalNum + 1

    product = product * num

    print("AVERAGE of the numbers is: ", sum/totalNum,"\n")
    print("PRODUCT of all the numbers is: ", product, "\n")

    ask = input("Enter 'q' to exit (Press any key to continue)\n")
    if ask == "q":
        state = False
    else: 
        print("Enter integers only")