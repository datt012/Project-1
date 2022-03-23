import os
import sys
#Bước 1:import module csv
import csv
#Bước 2:thiết lập tiêu đề,dữ liệu
header=['name', 'area', 'country_code2', 'country_code3']
data=[
    {'name': 'Albania',
    'area': 28748,
    'country_code2': 'AL',
    'country_code3': 'ALB'},
    {'name': 'Algeria',
    'area': 2381741,
    'country_code2': 'DZ',
    'country_code3': 'DZA'},
    {'name': 'American Samoa',
    'area': 199,
    'country_code2': 'AS',
    'country_code3': 'ASM'}
]
#Bước 3:mở file csv
with open(os.path.join(sys.path[0],'abc.csv'),'w',newline='') as f:#mở file nằm cùng thư mục file py
                                                                   #chế độ w cho phép ghi
#Bước 4:sử dụng hàm csv.Dictwriter()
    w=csv.DictWriter(f,fieldnames=header)#fieldnames được chỉ định bởi các key chứa trong từ điển là header
    w.writeheader()#ghi phần tiêu đề
    w.writerows(data)#ghi phần dữ liệu dùng writerows

