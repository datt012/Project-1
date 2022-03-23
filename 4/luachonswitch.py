def week(x):
        switcher={
                {0,9}:'Chu nhat',
                1:'Thu Hai',
                2:'Thu Ba',
                3:'Thu Tu',
                4:'Thu Nam',
                5:'Thu sau',
                6:'Thu bay'
             }
        return switcher.get(x, "nothing")

print("Nhap mot gia tri so nguyen khong am:",end=' ')
a=int(input()) 
print(week(a))