import os
import sys

#Bước 1:import module csv
import csv 

#Bước 2:mở file csv
with open(os.path.join(sys.path[0],'country.csv'),'r') as f: #mở file nằm cùng thư mục file py
#Bước 3:sử dụng hàm csv.reader()
    r=csv.reader(f) 
#Bước 4:hiển thị nội dung
    for i in r:
       print(i)


#Hiển thị nội dung 1 cột bất kì
    for line in r:
        print(line[0])#hiển thị cột name

#Tách tiêu đề và dữ liệu
    for line_no,line in enumerate(r,1):#line_no:chỉ số
        if line_no==1:                 #line:nội dung
            print('Header:')
            print(line)#header
            print('Data:')
        else:
            print(line)#data





        

