print("Nhap N",end=' ')
N=int(input())
S=0
while(N>0):
    S=S+(N%10)
    N=N/10
print(S)