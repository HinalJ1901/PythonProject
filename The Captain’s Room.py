from collections import Counter
n=int(input())
A =list(map(int,input().strip().split()))
A=Counter(A)
B=list(A.keys())
C=list(A.values())
for i in range(len(B)):
    if C[i]==1:
        break
   
print(B[i])