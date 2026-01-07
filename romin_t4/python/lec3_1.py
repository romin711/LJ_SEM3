import numpy as np

a1 = np.array([1,2,3,4,5,6])
a2 = np.array([[1,2,3,4,5] , [6,7,8,9,0]])
a7 = np.array([[11,12,13,14,15] , [16,17,18,19,20]])
a8 = np.array([[1,2,3,4,5] , [6,7,8,9,0] , [14,12,5,7,2]])
a9 = np.array([[21,22,32,24,52] , [62,27,28,29,2] , [146,122,56,76,42]])


# array.rehshape(2,-1) -> -1 is behave like fill. ex: 2 * _ = 12

# np.nditer
# for i in np.nditer(a2[:,::2]):
#     print(i)


# for i in a2[:,::2]:
#     print(i)

# for i,j in np.ndenumerate(a2):
#     print(i,'--',j)


a4 = np.array([1,2,3])
a5 = np.array([4,5,6])

a = np.concatenate((a4,a5),axis=0)
# print(a)

b = np.concatenate((a2,a7),axis=1)
# print(b)


c = np.concatenate((a8,a9),axis=1)
# print(c)
# d = np.concatenate((a8,a9),axis=2)
# print(d)

s1 = np.array([1,2,3,4,5,6,7,8,9])
z = np.array_split(s1 , 2 , axis=0)
# print(z)

