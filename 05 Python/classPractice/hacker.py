multiples = [6,12,18,24] 
b = [24,36]

count = 0

for i in range(len(multiples)):

    for j in range(len(b)):

        if (multiples[i]%b[j]==0):

            count = count + 1

print(count) 