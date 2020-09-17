def Bubble_sort(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list

if __name__ == "__main__":
    arr = [7, 5, 2, 4, 3, 9]
    sol = Bubble_sort(arr)
    print(sol)