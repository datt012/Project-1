def bin(k):
    if(k>1):
        bin(k//2)
    print(k%2,end='')
n=int(input("Nhap n : "))
print("Bieu dien nhi phan :",end=' ')
bin(n)