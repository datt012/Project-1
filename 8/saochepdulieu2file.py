#Ví dụ 2 : Sao chép dữ liệu giữa 2 file
#bài 8 trang 36
import os
import sys
print("Nhap ten file moi: ",end=' ')
filename=input()
with open(os.path.join(sys.path[0],'my_float.dat'),'br') as f1:#mở file f1 để đọc
    buffer=f1.read()
buffer=bytes(buffer)
with open(os.path.join(sys.path[0],filename),'bw') as f2:#mở file f2 để ghi 
    f2.write(buffer)
f1.close()
f2.close()






