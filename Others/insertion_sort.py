def Insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        key = arr[i]
        while j>0 and arr[j-1] > key:
            arr[j] = arr[j-1]
            j-=1
        arr[j] = key
    return arr
if __name__ == "__main__":
    arr = [29, 64, 73, 34, 20]
    arr2 = [7, 5, 2, 4, 3, 9]
    res = Insertion_sort(arr2)
    print(res)