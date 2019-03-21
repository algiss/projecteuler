import time
start_time=time.time()

n=20
matrix_line=[0]*(n+1)
matrix=[matrix_line]*(n+1)
for i in range(n+1):
     for j in range(n+1):
         if i==0 or j==0:
             matrix[i][j]=1
         else:
             matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]
answ=matrix[n][n]

print("Answ:",answ)
print("Time:",time.time()-start_time)
