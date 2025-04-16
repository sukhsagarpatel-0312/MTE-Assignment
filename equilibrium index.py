def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    result = []

    for i in range(len(arr)):
        if left_sum == (total_sum - arr[i] - left_sum):
            result.append(i)
        left_sum += arr[i]

    return result


arr=list(map(int,input("Enter element of the array separated with space").split()))


print(find_equilibrium_index(arr))