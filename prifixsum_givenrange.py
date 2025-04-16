def prefixsum(arr):
    n=len(arr)
    summ=0
    prefixsum=[0]*n
    for i in range(n):
        summ+=arr[i]
        prefixsum[i]=summ
    return prefixsum

def rangesum(prefixsum,l,r):
    return prefixsum[r]-prefixsum[l-1]
        

arr=list(map(int,input("Enter element of the array separated with space").split()))
l=int(input("Enter left entry"))
r=int(input("Enter right entry"))

print(rangesum(prefixsum(arr),l,r))