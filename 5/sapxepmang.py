n=int(input("Cho biet so phan tu cua mang : "))
m=[]
for i in range(n):
    print("Nhap gia tri cua m[",i,"]",end=' ')
    m.append(int(input()))
print("Mang truoc khi sap xep")
print(m)
for i in range(n-1):
    for j in range(i+1,n):
        if(m[j]<m[i]):
            temp=m[j]
            m[j]=m[i]
            m[i]=temp
    print("Mang o luot sap xep thu",i+1)
print(m)
