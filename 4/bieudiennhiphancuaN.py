import math
 
num=int(input("Nhap n : "))
rem=""
while num>=1:
    rem+=str(num%2)
    num=math.floor(num/2)
 
binary=""
for i in range(len(rem)-1,-1,-1):
    binary = binary + rem[i]
    
print("{0}".format(binary))