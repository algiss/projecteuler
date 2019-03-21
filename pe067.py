import time
start_time=time.time()

import re

matrix=[]

#reading file to list
with open("p067_triangle.txt") as ftxt:
    for line in ftxt:
        matrix.append(line)

#converting strings to int
for i in range(len(matrix)):
    matrix[i] = re.findall(r"\d\d",matrix[i])
    for j in range(len(matrix[i])):
        matrix[i][j]=int(matrix[i][j])


for i in range(len(matrix)-1):
    for j in range(len(matrix[-i-1])-1):
        if matrix[-i-1][j] > matrix[-i-1][j+1]:
            matrix[-i-2][j] += matrix[-i-1][j]
        else:
            matrix[-i-2][j] += matrix[-i-1][j+1]

        
answ=matrix[0][0]

print("Answ:",answ)
print("Time:",time.time()-start_time)
