#Ví dụ 1 : Ghi dữ liệu từ file
#bài 8 trang 32
import os
import sys
print("Nhap diem thi Toan,Ly,Hoa:")
dToan=float(input())
dLy=float(input())
dHoa=float(input())


with open(os.path.join(sys.path[0],'my_score.txt'),mode='w') as f: #ghi file cùng thư mục với file py
    f.write(str(dToan)+"\n")
    f.write(str(dLy)+"\n")
    f.write(str(dHoa)+"\n")
f.close()