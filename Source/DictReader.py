import os
import sys

#Bước 1:import module csv
import csv 

#Bước 2:mở file csv
with open(os.path.join(sys.path[0],'country.csv'),'r') as f: #mở file nằm cùng thư mục file py
#Bước 3:sử dụng hàm csv.DictReader()
    r=csv.DictReader(f)
    next(r) #bỏ qua dòng tiêu đề
    for line in r: #hiển thị nội dung
        print(f"The area of {line['name']} is {line['area']} km2")