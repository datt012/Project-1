n=int(input("Nhap so phan tu cua mang : "))
m=[]
for i in range(n):
    print("Nhap gia tri cua m[",i,"]",end=' ')
    m.append(int(input()))
s=0
p=1
for i in range(n):
    s+=m[i]
    p*=m[i]
print("Tong cua cac phan tu",s)
print("Tich cua cac phan tu",p)

