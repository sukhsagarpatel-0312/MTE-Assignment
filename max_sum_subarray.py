def max_sum_subarray(arr,k):
    n=len(arr)
    
    
    if n<k:
        return print("Seriously Bro !! ")
    
    current_sum=sum(arr[:k])
    max_sum=current_sum
    
    for  i in range(k,n):
        current_sum += arr[i]-arr[i-k]
        max_sum=max(max_sum,current_sum)
    return max_sum
    
    
arr=list(map(int,input("Enter element of the list separated with space : ").split()))
k=eval(input("Enter size of subarray : "))
print(max_sum_subarray(arr,k))