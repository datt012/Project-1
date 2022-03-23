n=int(input("Nhap so phan tu cua mang : "))
m=[]
for i in range(n):
    print("Nhap gia tri cua m[",i,"]",end=' ')
    m.append(int(input()))
print("Nhap vi tri can chen",end=' ')
k=int(input())
print("Nhap gia tr can chen",end=' ')
p=int(input())
if(k<n-1):m.insert(k,p)
print("Noi dung cua mang")
print(m)