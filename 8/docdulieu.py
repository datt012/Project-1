#Ví dụ 1 : Đọc dữ liệu từ file
#bài 8 trang 33

import os
import sys
f=open(os.path.join(sys.path[0],'my_score.txt'),'r') #đọc file cùng thư mục với file py
dToan=f.readline()
dLy=f.readline()
dHoa=f.readline()
f.close()

dTB=(float(dToan)+float(dLy)+float(dHoa))/3
print("Diem trung binh:",dTB)


