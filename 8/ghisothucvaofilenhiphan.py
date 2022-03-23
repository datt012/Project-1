#Ví dụ 2 : Ghi số thực vào file nhị phân
#bài 8 trang 35
import os
import sys
a=[] #tạo mảng chứa 100 sô thực
for i in range(0,100):
    a.append(i*2+1)
buffer=bytes(a)
#lưu vào file nhị phân
with open(os.path.join(sys.path[0],'my_float.dat'),'bw') as f:
    f.write(buffer)
f.close()

