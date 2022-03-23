def giaithua(k):
    if(k==1):return 1
    else:return k*giaithua(k-1)
n=int(input("Nhap n : "))
print(n,"!=",giaithua(n))