class toado:
    ten=""
    x=0
    y=0

t=toado()
print("Nhap thong tin toa do")
t.ten=input("Ten diem : ")
t.x=int(input("Toa do x : "))
t.y=int(input("Toa do y : "))
print("Gia tri cac truong:",end=' ')
print(t.ten,t.x,t.y)
