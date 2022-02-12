inp1 = input("Enter 'TRUE' or 'FALSE': ")
inp2 = input("Enter 'TRUE' or 'FALSE': ")
result = None

if inp1 == inp2:
    result = False
else:
    result = True

print("XOR result:", result)