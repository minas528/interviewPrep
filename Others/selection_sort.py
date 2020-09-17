def Selection_Sort(arr):
    
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] >= arr[j]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    return arr

if __name__ == "__main__":
    arr = [29, 64, 73, 34, 20]
    arr2 = [7, 5, 2, 4, 3, 9]
    res = Selection_Sort(arr2)
    print(res)