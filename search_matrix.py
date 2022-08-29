def searchMatrix(matrix, target):
    start, end = 0, len(matrix) - 1

    while start <= end:
        for m1 in matrix:
            left, right = 0, len(m1) - 1
            mid = (left + right) // 2

            while left < right and m1[mid] != target:
                if m1[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                mid = (left + right) // 2
            if m1[mid] == target:
                return True
            else:
                return False


if __name__ == '__main__':
    print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
