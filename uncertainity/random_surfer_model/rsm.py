
import numpy as np

threshold = 0.0000000000001
beta =0.85

'''
# Our Good Network
A=[[0,0,1,0],
   [1,0,0,1],
   [1,1,0,1],
   [1,0,0,0]]
'''

# Our Spider Trap Network
A=[[0,0,1,0],
   [1,0,0,0],
   [1,1,0,0],
   [1,1,0,1]]

arr=np.array(A, dtype=float)

s=[]

for i in range(0, len(A)):
    s.append(np.sum(arr[:,i]))



print("Summation of columns: ", s)   

M=arr

for j in range(0, len(A)):
    M[:,j]=M[:,j]/s[j]

print("Column stochastic probability matrix, M:")
print(M)

r=(1.0+np.zeros([len(M), 1]))/len(M)

print("Initial rank vector:")
print(r)

uniformR=(1.0-beta)*r

r_prev=r

for i in range(1, 1001):
    print("Iteration: ", i)
    r=beta*np.matmul(M, r_prev)+uniformR
    
    print("The rank vector: ")
    print(r)
    
    diff=np.sum(abs(r-r_prev))
    if (diff<threshold):
        break
    
    r_prev=r

print("The final rank vector: ")
print(r[:, 0])