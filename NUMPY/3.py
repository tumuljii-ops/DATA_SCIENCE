import numpy as np

a1=np.arange(10)
a2=np.arange(12,dtype='float').reshape(3,4)
a3=np.arange(8).reshape(2,2,2)

#ndim

print(a2.ndim) # tells us about dimension of array 

print(a3.ndim) # output is 3

#shape 
print(a2.shape)
print(a1.shape)

#size (tells us about total number of element present in an array)
print(a1.size)
print(a2.size)
print(a3.size)


#itemsize (tells us about size occupied in memory)
print(a1.itemsize)
print(a3.itemsize)

#dtype 
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)

#astype

a3.astype(np.int32)
print(a3)
print(a3.dtype)



 