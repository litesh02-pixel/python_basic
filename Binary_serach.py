#binary search

pos=-1

def search(list,n):

    L=0
    u=len(list)-1

    while L <= u:
        mid=(L+u)//2

        if list[mid] == n:
            globals()['pos']=mid
            return True
        else:
            if list[mid] < n:
                L=mid+1
            else:
                u=mid-1

    return False

list=[4,5,6,7,10,8,9]
n=6
if search(list,n):
    print("found at ", pos+1)
else:
    print("Not fund")

        
