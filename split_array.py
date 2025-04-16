def split_array(arr):
    
    tot_sum=sum(arr)
    left_sum=0
    right_sum=0
    
    for i in range(len(arr)):
        left_sum += arr[i]
        right_sum = tot_sum  - left_sum
        if left_sum == right_sum:
            return True
    return False
        
arr=list(map(int,input("Enter element of the array separated with space : ").split()))

print(split_array(arr))