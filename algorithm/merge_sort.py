def mergeSort(lst):
    ln = len(lst)
    if ln == 1:
        return lst
    mid = ln//2
    left_partition = mergeSort(lst[:mid])
    right_partition = mergeSort(lst[mid:])
    return merge(left_partition, right_partition)

def merge(arr1, arr2):
    i = 0
    j = 0
    sorted_list = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_list.append(arr1[i])
            i += 1
        else:
            sorted_list.append(arr2[j])
            j += 1
    sorted_list.extend(arr1[i:])
    sorted_list.extend(arr2[j:])
    return sorted_list


if __name__ == '__main__':
    print(mergeSort([30, 32, 10, 8, 18, 1, 2, 3, 5, 4]))