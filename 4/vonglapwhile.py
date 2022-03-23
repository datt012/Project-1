print("Chuong trinh nhap diem sinh vien")
print("Nhap diem (0<=diem<=10)",end=' ')
diem=float(input())
while(diem<0 or diem>10):
    print("Ban nhap khong dung")
    print("Ban hay nhap lai",end=' ')
    diem=float(input())
print("Diem ban vua nhap :",diem)
