print("Nhap N :",end=' ')
N=int(input())
S=0
P=1
for i in range(1,N):
    S+=i
    P*=i
print(S)
print(P)