#Binary Search function in Python. The data given must be an list in ascending order or else give sorted() while calling the function.
#Example: binarysearch(sorted(list),value to be found). The output will be the index number of first occurrence of value."

def binarysearch(data, value):
    low=0
    high=len(data)
    while(low<=high):
        mid=(low+high)//2
        if (data[mid]==value):
            print(mid)
            break
        elif(data[mid]<value):
            low=mid+1
        else:
            high=mid-1
    if (data[mid]!=value):
        print("Not Found")


binarysearch()