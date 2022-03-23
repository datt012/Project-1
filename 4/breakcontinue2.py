flag=1
print("Nhap gia tri n:",end=' ')
n=int(input())
if(n<2):print("So",n,"khong la so nguyen to va khong la hop so")
else:
    for i in range(2,n):
        if n%i==0:
            flag=0
            break
    if flag:
        print("So",n,"la so nguyen to")
    else:
        print("So",n,"la hop so")

