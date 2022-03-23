def month(x):
        switcher={
                1:'Thang 1 co 31 ngay',
                2:'Thang 2 co 28 hoac 29 ngay',
                3:'Thang 3 co 31 ngay',
                4:'Thang 4 co 30 ngay',
                5:'Thang 5 co 31 ngay',
                6:'Thang 6 co 30 ngay',
                7:'Thang 7 co 31 ngay',
                8:'Thang 8 co 31 ngay',
                9:'Thang 9 co 30 ngay',
                10:'Thang 10 co 31 ngay',
                11:'Thang 11 co 30 ngay',
                12:'Thang 12 co 31 ngay'
            }
        return switcher.get(x, "nothing")

print("Nhap vao thang trong nam:",end=' ')
thang=int(input())
print(month(thang))