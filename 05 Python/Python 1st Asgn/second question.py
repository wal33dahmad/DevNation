# Print the following patterns using loop :

# Part (a).
# *
# **
# ***
# ****

i = 1
x="*"

for i in range(1, 5, 1):
    print(i * x)


# Part (b).
#   *  
#  *** 
# *****
#  *** 
#   *

#Adding new line
print("\n")

row = 1
#loop for rows
while row <= 3:
    # loop for spaces
    space = 1
    while space <= 3-row :
        print(" ",end="")
        space = space + 1
    # end loop for spaces
    #loop for column
    column = 1
    while (column <= row*2-1):
        print("*",end="")
        column = column + 1
    print()
    row = row + 1

#reverse loop
row = 2
while row >= 1:
    #reverse space loop
    space = 1
    while space <= 3-row:
        print(" ", end="")
        space = space + 1
    #reverse column loop
    column = 0
    while column < row * 2 - 1:
        print("*",end="")
        column = column + 1
    print()
    row = row - 1

#Adding new line
print("\n")

# Part (c).
# 1010101
#  10101 
#   101  
#    1   

#loop for rows
for r in range(7,0,-2):
    #loop for spaces
    sp = 6
    while sp >= r:
        print(" ",end="")
        sp = sp - 2

    #loop for column 
    col = 1
    while col <= r:
        print(col%2, end="")
        col = col+1

    print()