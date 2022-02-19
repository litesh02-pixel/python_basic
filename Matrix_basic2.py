from numpy import *

arr1=array([
            [1,2,3,4,5,6],
            [9,8,7,6,5,4]
            ])
arr2=arr1.flatten()
arr3=arr2.reshape(3,4)
print('1:',arr1)
print('2:',arr2)
print('3:',arr3)
