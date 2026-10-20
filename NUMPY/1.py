import numpy as np

# creating array in numpy

a=[1,2,3]

b=np.array(a)
print(b)

c=np.array([1,2,3,4])

print(type(c))

# creating 2 ,3  d array 

arr=[[1,2,3],
    [3,4,5]]

arr1=np.array(arr)

print(arr1)

arr2=[[1,2,3],[1,2,3],
      [1,3,5]]
arr2_numpy=np.array(arr2)
print(arr2_numpy)

# creating custom data type array

array=[[1,2,3],
       [4,5,6]]

array_numpy=np.array(array,dtype=float)

print(type(array_numpy))
print(array_numpy)

array_numpy=np.array(array,dtype=bool)
print(array_numpy)