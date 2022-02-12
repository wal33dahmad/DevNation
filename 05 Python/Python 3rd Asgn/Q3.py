# You need to write a script that can do the following:
# Read a DNA string input by the user (check it is a valid DNA string!)
# Reverse the string
# Go through the reversed string and complement each character
# Display the final result (the reverse complement string)

def verifyDNA(usrDNA, DNA):
    for i in usrDNA:
        found = False
        for j in DNA:
            if i == j:
                found = True
        if found == False:
            break
    return found

def reverse(usrDNA):
    revDNA = ""
    for i in usrDNA:
        revDNA = i + revDNA
    return revDNA

def complement(usrDNA):
    compDNA = ""
    for i in usrDNA:
        if i == "A":
            compDNA += "T"
        if i == "T":
            compDNA += "A"
        elif i == "C":
            compDNA += "G"
        elif i == "G":
            compDNA += "C"
    return compDNA

def DNA():
    UserInputDNA = input("Enter a DNA: ")
    UserInputDNA = UserInputDNA.upper()
    validDNA = "ACGT"

    while verifyDNA(UserInputDNA, validDNA) == False:
        UserInputDNA = input(
            "Invalid DNA sequence\n Enter a Valid DNA: ")
        UserInputDNA = UserInputDNA.upper()
    reversedDNA = reverse(UserInputDNA)
    complementedDNA = complement(reversedDNA)

    print("The Reversed complemented DNA: ", complementedDNA)

if __name__ == "__main__":
    DNA()