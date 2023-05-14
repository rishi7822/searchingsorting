def Linear_Search(list1,n,key):

    #searching lsit1 sequentially
    for i in range(0,n):
        if(list1[i]==key):
            return i
        return -1
    
    #driver code
list1 = [1,3,4,5,6,2,1,1]
key = 5

n =len(list1)
res = Linear_Search(list1,n,key)

if(res == -1):
        
        print("Element not found")
else:
        print("Element found at index:",res)