#Ví dụ 2 : Đọc số thực biết trước vị trí
#bài 8 trang 38
import os
import sys
f=open(os.path.join(sys.path[0],'my_float.dat'),'br') #mở file để đọc
f.seek(0)
buf=f.read(1)
print("So thuc dau tien trong file:",end=' ')
for i in buf:print(i)
n=int(input("Nhap vi tri can doc: "))
f.seek(n-1)
buf=f.read(1)
print("So thuc thu",n,"trong file:",end=' ')
for i in buf:print(i)
f.close()
