def QuickSort(nums, start, end):
    if start >= end:
        return
    i, j = start+1, end
    while i <= j:
        while i <= j and nums[i] <= nums[start]:
            i += 1
        while i <= j and nums[j] >= nums[start]:    
            j-=1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
        print(nums)

    nums[start], nums[j] = nums[j], nums[start]
    print(nums)
    QuickSort(nums,start,j-1)
    QuickSort(nums, j+1, end)

if __name__ == "__main__":
    arr = [29, 64, 73, 34, 20]
    arr2 = [7, 5, 2, 4, 3, 9]
    QuickSort(arr2,0, len(arr)-1)
    print(arr2)