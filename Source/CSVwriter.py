import os
import sys
#Bước 1:import module csv
import csv
#Bước 2:thiết lập tiêu đề,dữ liệu
header = ['name', 'area', 'country_code2', 'country_code3']
data = [
    ['Albania', 28748, 'AL', 'ALB'],
    ['Algeria', 2381741, 'DZ', 'DZA'],
    ['American Samoa', 199, 'AS', 'ASM'],
    ['Andorra', 468, 'AD', 'AND'],
    ['Angola', 1246700, 'AO', 'AGO']
]
#Bước 3:mở file csv
with open(os.path.join(sys.path[0],'abc.csv'),'w',newline='') as f:#mở file nằm cùng thư mục file py
                                                                   #chế độ w cho phép ghi
#Bước 4:sử dụng hàm csv.writer()
    w=csv.writer(f)
    w.writerow(header)
    w.writerows(data)