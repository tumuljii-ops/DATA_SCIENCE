import numpy as np

#functions of numpy
a1=np.arange(12).reshape(3,4)
a2=np.arange(12,24).reshape(4,3)

print(np.max(a1))
print(np.min(a2))
print(np.sum(a1))
print(np.prod(a1))

# max/min/sum/prod 
# 0-> col and 1->row

x=np.max(a2,axis=0)
print(x)

y=np.prod(a1,axis=1)
print(y)

#mean/median/std/var (can be done in whole matrix as well as col wise and row wise)

#trignometric functions
np.sin(a1)


#dot product

z=np.dot(a1,a2)
print(z)

#log and exponent
np.log(a1)
np.exp(a2)

#round/floor/ceil

ran=np.random.random((3,4))

print(np.round(ran))
print(np.floor(ran))
print(np.ceil(ran))








 