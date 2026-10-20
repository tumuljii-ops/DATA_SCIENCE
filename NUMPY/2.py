# np.arrange
import numpy as np

#initial,end (not included),gap or stride
array=np.arange(1,11,2)

print(array)

#range==arange

# changing shape(reshape)

array=np.arange(1,11).reshape(2,5)

print(array)

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr=arr.reshape(1,9)

print(arr)

#np.ones and np.zeros (to create matrix of 1 or 0)
array=np.ones((3,4))
array1=np.zeros((5,6))

print(array)
print(array1)

#to create random number  np.random

ar1=np.random.random((3,4))

print(ar1)

# to create custom random number between any range 

# Generate a 2x2 array of random floats between 1 and 2
arr = np.random.uniform(low=1.0, high=2.0, size=(2, 2))

print(arr)


#np.linspace or linear space

arr=np.linspace(-10,10,10) #defalut is float 
 # this linspace is generating linear space number between give two range 
 
 
# np.identity helpfull to create identity matrix

array=np.identity(3)
print(array)



 

