import ctypes
a=[2,4,5,1,6]
p=id(a[0])
print(ctypes.cast(p,ctypes.py_object).value) #giatria[0]
p=p+32*(a[1]-a[0])
print(ctypes.cast(p,ctypes.py_object).value) #giatria[1]


