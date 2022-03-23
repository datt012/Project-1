def fibo(k):
    if(k==0):return 0
    if(k==1):return 1
    else:return fibo(k-1)+fibo(k-2)
n=int(input("Nhap n : "))
print("So fibonaci thu",n,"la:",fibo(n))
print("Day so fibonaci")
for i in range(0,n+1):
    print(fibo(i),end=' ')