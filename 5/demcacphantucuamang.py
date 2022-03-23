n=int(input("Nhap so phan tu cua mang : "))
m=[]
for i in range(n):
    print("Nhap gia tri cua m[",i,"]",end=' ')
    m.append(int(input()))
c1=0
c2=0
for i in range(n):
    if(m[i]%2==0):c1=c1+1
    else:c2=c2+1
print("So cac phan tu le",c1)
print("So cac phan tu chan",c2)