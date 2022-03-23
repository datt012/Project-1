def GT(n):
    if(n<0):return -1
    if(n==0):return 1
    ket_qua=1
    for i in range (1,n+1):
        ket_qua=ket_qua*i

    return ket_qua

def A(k,n):
    return GT(n)/GT(n-k)
def C(k,n):
    return GT(n)/(GT(k)*GT(n-k))
n=4
k=3
print(n,"!=",GT(n))
print(k,"!=",GT(k))
print("A(",k,n,")=",A(k,n))
print("C(",k,n,")=",C(k,n))