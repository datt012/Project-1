n=int(input("Cho so phan tu cua mang: "))
while(n>100 or n<0):
    n=int(input("Cho so phan tu cua mang: "))
a=[]
for i in range(n):
    a.append(int(input()))
print(a)
