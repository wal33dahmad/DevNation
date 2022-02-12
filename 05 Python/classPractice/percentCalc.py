totalClass = int(input("Total Number of classes\n"))

classAttended = int(input("Classes attended by the student\n"))

# Calculating Percentage of class attended

percent = classAttended / totalClass * 100
print(percent, "%")

# eligibility to sit in exam

if percent < 75:
    print("Student is not allowed to sit in exam\n")
else: 
     print("Student is allowed to sit in exam\n")