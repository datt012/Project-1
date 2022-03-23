import ctypes
i=3
p=hex(id(i))
print(p) #laydiachicua'i'
print(ctypes.cast(int(p,base=16),ctypes.py_object).value) #laygiatritrotoi





i=3
j=6
p1=hex(id(1))
p2=hex(id(2))
p1=p2
print(p1)
print(p2)




x=21
y=34.34
p=hex(id(x))
q=hex(id(y))
print(p)
print(q)