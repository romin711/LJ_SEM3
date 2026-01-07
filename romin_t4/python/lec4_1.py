import numpy as np
marks = np.array([[15,17,13,17],
                  [17,19,15,19],
                  [16,17,15,20],
                  [18,19,22,19],
                  [24,22,24,25]])
print('original array:\n',marks)

etc = np.array([21,22,23,24,22])
etc = etc.reshape(-1,1)
print(etc)

marks = np.concatenate((marks,etc), axis = 1)
print('after adding etc subject updated array:\n',marks)

s6 = np.array([19,18,17,21,24])
s7 = np.array([22,21,23,21,23])
s6 = s6.reshape(1,-1)
s7 = s7.reshape(1,-1)
marks = np.concatenate((marks,s6,s7) , axis = 0)
print('after adding s6 & s7 updated array:\n',marks)
total = marks.sum(axis = 1 , keepdims=True)

print(total)

marks = np.concatenate((marks,total),axis = 1)
print('after adding total updated array:\n',marks)
print('after sorting array:\n', np.array(sorted(marks,key=lambda x:x[-1],reverse=True)))