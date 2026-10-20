import numpy as np

a1=np.arange(12).reshape((3,4))
a2=np.arange(12,24).reshape((3,4))

print(a1)
print(a2)

#SCALAR OPERATIONS

#ADDITION

a1=a1+2
print(a1)

a1=a1*2
print(a1)

a1=a1%3
print(a1)

a1=a1>5 
print(a1)

print(a1==15)


#VECTOR OPERATIONS 

a1=a1+a2  #addition 
a1**a2  #power 
a1=a1*a2  #multiplications
 

