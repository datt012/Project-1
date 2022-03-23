print("Nhap gia tri cho 3 so nguyen a,b,c")
a=int(input())
b=int(input())
c=int(input())
def tich():
    print("Gia tri cua cac bien tong the a,b,c:",end=' ')
    print("a=",a,"b=",b,"c=",c)
    return a*b*c
print("Tich cua 3 so la:",tich())
