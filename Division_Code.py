nums=[12,14,15,17,20]

for num in nums:
    if num%5==0:
        print(num)
        break
else:
    print("not found")

print('_________________________________')

#======================================================
#Prime number 
num=7

for i in range(2,num):
    if num %i==0:
        print("not Prime")
        break
else:
        print("prime Number")
