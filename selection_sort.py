#selection_sort

def sort(nums):
    for i in range(len(nums)):
        minpos=i
        for j in range(i,len(nums)):
            if nums[j]<nums[minpos]:
                minpos=j

        temp=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=temp
        #print(nums)



nums=[2,4,5,8,3,1]

sort(nums)
print(nums)
