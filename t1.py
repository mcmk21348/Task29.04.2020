
A = list(map(int, input('Введите список через пробел:').split()))
l = len(A)
B = []
result = 0
n = 0
for i in range(l):
    if A[i] >=1:
        B.append(A[i]) 
if B ==[]:
    print(1)
else:    
    B.sort() 
    B = list(dict.fromkeys(B))
    n = len(B)
    for j in range(n-1):
        if B[j+1]>B[j]+1:
            result = (B[j]+1)
    if result != 0:
        print(result)
    else:
        print(B[n-1]+1)
