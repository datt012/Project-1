def giai_thua(a):
    if(a<0):ket_qua=-1
    if(a==0):ket_qua=1
    else:
        ket_qua=1
        for i in range(1,a+1):
            ket_qua=ket_qua*i
    return ket_qua

print(giai_thua(5))

