def MergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = MergeSort(arr[:mid])
    right = MergeSort(arr[mid:])

    sol = merge(left, right)
    return sol

def merge(left, right):
    i = j = 0
    result = []
    while i <len(left) and j <len(right):
        if left[i]<= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result += left[i:]
    result += right[j:]
    return result

if __name__ == "__main__":
    arr = [29, 64, 73, 34, 20]
    arr2 = [7, 5, 2, 4, 3, 9]
    res = MergeSort(arr2)
    print(res)