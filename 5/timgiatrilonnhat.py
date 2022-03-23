MONTHS=12
rainfall=[]
for i in range(MONTHS):
    print("Nhap phan tu thu",i+1,end=' ')
    rainfall.append(int(input()))
max=rainfall[0]
for i in range(MONTHS):
    if(max<rainfall[i]): max=rainfall[i]
print(max)
