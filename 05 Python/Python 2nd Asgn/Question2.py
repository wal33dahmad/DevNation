# flagL = 5
# flagW = 10
# flagPL = 6
# flagPW = 2

#Taking input from user

flagL = int(input("How long is your flag? "))
flagW = int(input("How wide is your flag? "))
flagPL = int(input("How long is your flagPole? "))
flagPW = int(input("How wide is your flagPole? "))

for i in range(flagL):
    print(flagW*"*")
for j in range(flagPL):
    print(flagPW*"*")