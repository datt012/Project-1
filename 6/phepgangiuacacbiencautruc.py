class sinhvien:
    hoten=""
    diem=0
a=sinhvien()
b=sinhvien()
c=sinhvien()
print("Nhap thong tin sinh vien")
a.hoten=input("Ho ten : ")
a.diem=int(input("Diem : "))
b=a
c.hoten=a.hoten
c.diem=a.diem
print("Bien a:",end=' ')
print(a.hoten,a.diem)
print("Bien b:",end=' ')
print(b.hoten,b.diem)
print("Bien c:",end=' ')
print(c.hoten,c.diem)
