from array import *

vals=array('i',[1,2,3,-4,5,9])
print(vals)
print(vals.buffer_info())

for e in vals:
    print(e)
#===================================
from array import *
vals=array('i',[1,2,3,3])
for i in range(len(vals)):
    print(vals[i])
