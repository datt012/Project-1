print("Nhap so phan tu cua mang",end=' ')
n=int(input())
m=[]
for i in range(n):
    print("Nhap gia tri cua m[",i,"]",end=' ')
    m.append(int(input()))
print("Nhap vi tri can xoa",end=' ')
k=int(input())
if(k<n-1):del m[k]
print("Noi dung cua mang")
print(m)