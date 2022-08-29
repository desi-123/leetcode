def quickSort(array):

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]

        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)

        return quickSort(less)+equal+quickSort(greater)

    else:
        return array


if __name__ == '__main__':
    print(quickSort([30, 32, 10, 8, 18, 1, 2, 3, 5, 4]))