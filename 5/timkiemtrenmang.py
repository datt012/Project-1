n=int(input("Nhap so phan tu cua mang : "))
k=int(input("Nhap vao gia tri can tim : "))
dem=0
a=[]
chi_so=[]
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if(a[i]==k): 
        chi_so.append(i)
        dem=dem+1
if(dem>0):
    print("Trong mang co",dem,"phan tu co gia tri bang",k)
    print(chi_so)
else:
    print("Trong mang khong co phan tu nao co gia tri bang",k)

